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

col1, col2 = st.columns(2)

with col1:
    selected_hotel = st.selectbox(
        "🏨 Select Hotel",
        hotel_list
    )

with col2:
    compare_hotel = st.selectbox(
        "🏨 Compare With",
        [h for h in hotel_list if h != selected_hotel]
    )


# Filter Both Datasets

filtered_review = review_df[
    review_df["hotel"] == selected_hotel
]

filtered_aspect = aspect_df[
    aspect_df["hotel"] == selected_hotel
]

compare_review = review_df[
    review_df["hotel"] == compare_hotel
]

compare_aspect = aspect_df[
    aspect_df["hotel"] == compare_hotel
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

