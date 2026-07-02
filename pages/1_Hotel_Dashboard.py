import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Hotel Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Hotel Comparison Dashboard")

df = pd.read_csv("data/Cleaned_Combined_Hotel_Reviews.csv")

st.write("This page shows sentiment analysis results based on collected hotel reviews.")

hotel_list = ["All Hotels"] + sorted(df["hotel"].dropna().unique().tolist())

selected_hotel = st.selectbox(
    "Select Hotel",
    hotel_list
)

if selected_hotel != "All Hotels":
    filtered_df = df[df["hotel"] == selected_hotel]
else:
    filtered_df = df.copy()

st.subheader("Overall Sentiment Summary")

sentiment_counts = filtered_df["sentiment"].value_counts()

col1, col2, col3 = st.columns(3)

col1.metric("Positive", sentiment_counts.get("Positive", 0))
col2.metric("Neutral", sentiment_counts.get("Neutral", 0))
col3.metric("Negative", sentiment_counts.get("Negative", 0))

st.subheader("Sentiment Distribution")

st.bar_chart(sentiment_counts)

st.subheader("Sentiment Trend by Year")

if "review_year" in filtered_df.columns:
    trend = (
        filtered_df
        .groupby(["review_year", "sentiment"])
        .size()
        .unstack(fill_value=0)
        .sort_index()
    )

    st.line_chart(trend)
else:
    st.warning("review_year column not found in dataset.")

st.subheader("Review Data Preview")

st.dataframe(filtered_df)