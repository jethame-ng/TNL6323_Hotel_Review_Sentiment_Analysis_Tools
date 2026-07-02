import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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


# Overall Sentiment Summary

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


# Sentiment Distribution and Trend

st.subheader("📊 Sentiment Distribution")

st.bar_chart(sentiment_counts)

st.subheader("📈 Sentiment Trend")

trend = (
    filtered_review
    .groupby(["review_year","sentiment"])
    .size()
    .unstack(fill_value=0)
)

st.line_chart(trend)


# Aspect-Based Sentiment
st.subheader("⭐ Aspect-Based Sentiment")

aspect_summary = (
    filtered_aspect
    .groupby(["aspect","sentiment"])
    .size()
    .unstack(fill_value=0)
)

st.dataframe(aspect_summary)


# Benchmark Comparison

st.divider()

st.subheader("🏆 Benchmark Comparison")

compare_hotel = st.selectbox(
    "Compare Selected Hotel With",
    [h for h in hotel_list if h != selected_hotel]
)

# Filter Comparison Hotel
compare_aspect = aspect_df[
    aspect_df["hotel"] == compare_hotel
]

# Aspect Comparison Table
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

st.dataframe(comparison)

st.subheader("🏅 Benchmark Result")

comparison["Difference"] = (
    comparison[selected_hotel]
    - comparison[compare_hotel]
)

st.dataframe(comparison)

st.subheader("💪 Top Strengths")

strengths = comparison["Difference"].sort_values(
    ascending=False
).head(3)

for aspect, score in strengths.items():
    st.success(
        f"{aspect}: {score:+.1f}% compared with {compare_hotel}"
    )


st.subheader("⚠ Top Issues")

issues = comparison["Difference"].sort_values().head(3)

for aspect, score in issues.items():
    st.error(
        f"{aspect}: {score:+.1f}% compared with {compare_hotel}"
    )


# Review Preview

st.divider()

st.subheader("📝 Review Preview")

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