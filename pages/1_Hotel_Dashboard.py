import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from chatbot.assistant import ask_llm

st.set_page_config(
    page_title="Hotel Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Hotel Comparison Dashboard")

review_df = pd.read_csv("data/Cleaned_Combined_Hotel_Reviews.csv")
aspect_df = pd.read_csv("data/Aspect_Hotel_Reviews.csv")

st.write("This page shows sentiment analysis results based on collected hotel reviews.")


# Hotel Selection
hotel_list = sorted(review_df["hotel"].dropna().unique())

selected_hotel = st.selectbox(
    "🏨 Select Hotel",
    hotel_list
)


# Filter Selected Hotel Only

filtered_review = review_df[
    review_df["hotel"] == selected_hotel
]

filtered_aspect = aspect_df[
    aspect_df["hotel"] == selected_hotel
]

# -------------------------------
# Overall Sentiment Summary
# -------------------------------

st.subheader("📌 Overall Sentiment Summary")

sentiment_counts = (
    filtered_review["sentiment"]
    .value_counts()
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "😊 Positive",
    sentiment_counts.get("Positive", 0)
)

col2.metric(
    "😐 Neutral",
    sentiment_counts.get("Neutral", 0)
)

col3.metric(
    "😞 Negative",
    sentiment_counts.get("Negative", 0)
)

# =====================================================
# Sentiment Analytics
# =====================================================

with st.expander("📈 Sentiment Analytics", expanded=True):

    st.subheader("📊 Sentiment Distribution")
    st.bar_chart(sentiment_counts)

    st.subheader("📈 Sentiment Trend")

    trend = (
        filtered_review
        .groupby(["review_year", "sentiment"])
        .size()
        .unstack(fill_value=0)
    )

    st.line_chart(trend)

    st.subheader("⭐ Aspect Positive Rate")

    aspect_positive = (
        filtered_aspect
        .groupby("aspect")["sentiment"]
        .apply(lambda x: (x == "Positive").mean() * 100)
        .sort_values(ascending=False)
        .round(1)
    )

    st.bar_chart(aspect_positive)

# =====================================================
# Benchmark Analysis
# =====================================================

with st.expander("🏆 Benchmark Analysis", expanded=True):

    st.subheader("🏆 Benchmark Analysis")

    compare_hotel = st.selectbox(
        "Compare Selected Hotel With",
        [h for h in hotel_list if h != selected_hotel]
    )

    compare_aspect = aspect_df[
        aspect_df["hotel"] == compare_hotel
    ]

    hotel_positive = (
        filtered_aspect
        .groupby("aspect")["sentiment"]
        .apply(lambda x: (x == "Positive").mean()*100)
    )

    competitor_positive = (
        compare_aspect
        .groupby("aspect")["sentiment"]
        .apply(lambda x: (x == "Positive").mean()*100)
    )

    comparison = pd.DataFrame({
        selected_hotel: hotel_positive,
        compare_hotel: competitor_positive
    }).fillna(0)

    comparison = comparison.round(1)

    comparison["Difference"] = (
        comparison[selected_hotel]
        - comparison[compare_hotel]
    ).round(1)

    comparison = comparison.reset_index()

    st.dataframe(
        comparison,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("💪 Top Strengths")

    strengths = comparison.sort_values(
        by="Difference",
        ascending=False
    ).head(3)

    for _, row in strengths.iterrows():
        st.success(
            f"{row['aspect']}: {row['Difference']:+.1f}% compared with {compare_hotel}"
        )


    st.subheader("⚠ Top Issues")

    issues = (
        comparison[
            comparison["Difference"] < 0
        ]
        .sort_values(by="Difference")
        .head(3)
    )

    if issues.empty:
        st.success("No major weaknesses were identified compared with the benchmark hotel.")
    else:
        for _, row in issues.iterrows():
            st.error(
                f"{row['aspect']}: {row['Difference']:.1f}% compared with {compare_hotel}"
            )


    # -------------------------------
    # Management Recommendations
    # -------------------------------

    st.subheader("💡 Management Recommendations")

    recommendations = []

    # Get best and worst rows
    worst_row = comparison.loc[
        comparison["Difference"].idxmin()
    ]

    best_row = comparison.loc[
        comparison["Difference"].idxmax()
    ]

    worst_aspect = worst_row["aspect"]
    worst_gap = worst_row["Difference"]

    best_aspect = best_row["aspect"]
    best_gap = best_row["Difference"]

    # Recommendation 1
    recommendations.append(
        f"Improve **{worst_aspect}** because it performs {abs(worst_gap):.1f}% lower than {compare_hotel}."
    )

    # Recommendation 2
    recommendations.append(
        f"Maintain **{best_aspect}** because it performs {best_gap:.1f}% better than {compare_hotel}."
    )

    # Recommendation 3
    positive = sentiment_counts.get("Positive", 0)
    negative = sentiment_counts.get("Negative", 0)

    if negative > positive * 0.5:
        recommendations.append(
            "Negative sentiment is relatively high. Focus on customer complaints and service recovery."
        )
    else:
        recommendations.append(
            "Overall customer satisfaction is positive. Continue maintaining strengths while improving weaker aspects."
        )

    # Display
    for i, rec in enumerate(recommendations, 1):
        st.info(f"Recommendation {i}: {rec}")

# =====================================================
# Hotel Management Assistant
# =====================================================

with st.expander("🤖 Hotel Management Assistant", expanded=True):

    st.info(
        "Ask questions about hotel performance, customer feedback, "
        "benchmark competitors and management recommendations."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    question = None


    # Chat History (Scrollable)

    chat_container = st.container(
        border=True,
        height=380
    )

    with chat_container:

        if len(st.session_state.messages) == 0:
            st.markdown(
                """
                👋 **Hello!**

                I am your AI Hotel Management Assistant.

                I can help you:
                - Summarize customer feedback
                - Compare hotels
                - Identify strengths and weaknesses
                - Recommend improvement strategies
                """
            )

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])


    # Quick Questions

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("📊 Executive Summary", use_container_width=True):
            question = "Summarize customer feedback."

        if st.button("⭐ Strengths", use_container_width=True):
            question = "What are our strengths?"

    with c2:
        if st.button("⚠ Improvement Priority", use_container_width=True):
            question = "Which aspect should we improve first?"

        if st.button("🏆 Benchmark Analysis", use_container_width=True):
            question = "Compare with competitor."

    with c3:
        if st.button("💡 Recommendations", use_container_width=True):
            question = "Generate management recommendations."

        if st.button("📈 Trend Analysis", use_container_width=True):
            question = "Summarize sentiment trend."

    # User Input

    col1, col2 = st.columns([6, 1])

    with col1:
        user_input = st.text_input(
            "",
            placeholder="Ask anything about hotel performance...",
            label_visibility="collapsed"
        )

    with col2:
        send = st.button("Send", use_container_width=True)


    if send and user_input.strip():
        question = user_input


    # Generate Response

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.spinner("Analysing hotel performance..."):

            try:
                answer = ask_llm(
                    selected_hotel,
                    compare_hotel,
                    sentiment_counts,
                    comparison,
                    recommendations,
                    question
                )

            except Exception as e:
                answer = (
                    "⚠️ The AI assistant is temporarily unavailable.\n\n"
                    "This is usually caused by the Gemini API quota or rate limit being exceeded. "
                    "Please try again later."
                )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        st.rerun()


# =====================================================
# Review Preview
# =====================================================

with st.expander("📝 Review Preview"):

    st.write("Browse the original customer reviews for the selected hotel.")

    col1, col2 = st.columns(2)

    with col1:
        sentiment_filter = st.selectbox(
            "Filter by Sentiment",
            ["All", "Positive", "Neutral", "Negative"]
        )

    with col2:
        keyword = st.text_input(
            "Search Review",
            placeholder="Enter keyword..."
        )

    preview_df = filtered_review.copy()

    # Filter by sentiment
    if sentiment_filter != "All":
        preview_df = preview_df[
            preview_df["sentiment"] == sentiment_filter
        ]

    # Search keyword
    if keyword:
        preview_df = preview_df[
            preview_df["review"]
            .str.contains(keyword, case=False, na=False)
        ]

    st.write(f"Showing **{len(preview_df)}** reviews")

    display_columns = [
        "review_date",
        "review",
        "sentiment"
    ]

    st.dataframe(
        preview_df[display_columns],
        use_container_width=True,
        hide_index=True
    )