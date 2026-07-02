import streamlit as st
import pandas as pd
import re
import joblib

st.set_page_config(
    page_title="Analyse New Review",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Analyse New Review")

st.write(
    "Enter a hotel review to predict the overall sentiment, "
    "detect mentioned aspects, and analyse the sentiment of each aspect."
)

# ==========================================================
# Load Model
# ==========================================================

# Replace with your own model
# sentiment_model = joblib.load("models/sentiment_model.pkl")
# vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# ==========================================================
# Text Preprocessing
# ==========================================================

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# ==========================================================
# Aspect Dictionary
# ==========================================================

aspect_keywords = {
    "Room": [
        "room","bed","pillow","suite","balcony"
    ],
    "Staff": [
        "staff","reception","receptionist","employee",
        "manager","service"
    ],
    "Cleanliness": [
        "clean","dirty","cleanliness","smell","dust"
    ],
    "Location": [
        "location","near","far","airport","station"
    ],
    "Breakfast": [
        "breakfast","buffet","food","meal","restaurant"
    ],
    "WiFi": [
        "wifi","internet","network"
    ],
    "Parking": [
        "parking","car park"
    ],
    "Bathroom": [
        "bathroom","toilet","shower"
    ]
}

# ==========================================================
# Detect Aspects
# ==========================================================

def detect_aspects(review):

    detected = []

    review_lower = review.lower()

    for aspect, keywords in aspect_keywords.items():

        if any(keyword in review_lower for keyword in keywords):
            detected.append(aspect)

    return detected

# ==========================================================
# Aspect Sentiment (Simple Rule Version)
# ==========================================================

positive_words = [
    "good","great","excellent","clean","friendly",
    "comfortable","nice","amazing","love",
    "perfect","spacious","fast"
]

negative_words = [
    "bad","dirty","poor","slow","worst",
    "terrible","awful","small","noisy",
    "uncomfortable","disappointing"
]

def aspect_sentiment(review, aspect):

    text = review.lower()

    pos = sum(word in text for word in positive_words)
    neg = sum(word in text for word in negative_words)

    if pos > neg:
        return "😊 Positive"

    elif neg > pos:
        return "☹ Negative"

    else:
        return "😐 Neutral"

# ==========================================================
# Overall Sentiment
# ==========================================================

def predict_sentiment(review):

    # -------------------------
    # Replace this with your model
    # processed = preprocess(review)
    # vector = vectorizer.transform([processed])
    # prediction = sentiment_model.predict(vector)[0]
    # return prediction
    # -------------------------

    text = review.lower()

    pos = sum(word in text for word in positive_words)
    neg = sum(word in text for word in negative_words)

    if pos > neg:
        return "😊 Positive"

    elif neg > pos:
        return "☹ Negative"

    else:
        return "😐 Neutral"

# ==========================================================
# User Input
# ==========================================================

review = st.text_area(
    "Enter Hotel Review",
    height=180
)

if st.button("Analyse Review"):

    if review.strip() == "":
        st.warning("Please enter a review.")

    else:

        st.divider()

        overall = predict_sentiment(review)

        st.subheader("Overall Sentiment")

        st.success(overall)

        st.divider()

        st.subheader("Detected Aspects")

        aspects = detect_aspects(review)

        if len(aspects) == 0:

            st.info("No predefined aspect detected.")

        else:

            st.write(", ".join(aspects))

            st.divider()

            st.subheader("Aspect Sentiments")

            result = []

            for aspect in aspects:

                result.append({
                    "Aspect": aspect,
                    "Sentiment": aspect_sentiment(review, aspect)
                })

            result_df = pd.DataFrame(result)

            st.dataframe(
                result_df,
                use_container_width=True,
                hide_index=True
            )