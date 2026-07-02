import streamlit as st
import pandas as pd
import re
import joblib

st.title("📝 Analyse New Review")

st.write(
    "Enter a hotel review to predict the overall sentiment, "
    "detect mentioned aspects, and analyse the sentiment of each aspect."
)

review = st.text_area(
    "Enter Hotel Review",
    height=180
)

# Button directly below the text area
analyse = st.button("🔍 Analyse Review")

st.divider()

st.subheader("Overall Sentiment")

if analyse:
    st.success("😊 Positive")
else:
    st.info("Not analysed yet.")

st.divider()

st.subheader("Detected Aspects")

if analyse:
    st.write(["Room", "Breakfast"])
else:
    st.info("No aspects detected.")

st.divider()

st.subheader("Aspect Sentiments")

if analyse:
    st.dataframe(result_df, use_container_width=True)
else:
    st.dataframe(
        pd.DataFrame(columns=["Aspect", "Sentiment"]),
        use_container_width=True,
        hide_index=True
    )