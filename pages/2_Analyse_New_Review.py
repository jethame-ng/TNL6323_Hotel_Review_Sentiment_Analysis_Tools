import streamlit as st
import pandas as pd

from utils.predictor import predict_sentiment, split_sentences

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
# Aspect Dictionary
# ==========================================================

aspect_keywords = {

    "Room": [
        "room","bed","pillow","suite","balcony"
    ],

    "Staff": [
        "staff","reception","receptionist",
        "employee","manager","service"
    ],

    "Cleanliness": [
        "clean","dirty","cleanliness",
        "smell","dust"
    ],

    "Location": [
        "location","near","far",
        "airport","station"
    ],

    "Breakfast": [
        "breakfast","buffet",
        "food","meal","restaurant"
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
# Aspect Sentiment using DistilBERT
# ==========================================================

def aspect_sentiment(review, aspect):

    sentences = split_sentences(review)

    keywords = aspect_keywords[aspect]

    related_sentences = []

    for sentence in sentences:

        if any(keyword in sentence.lower() for keyword in keywords):
            related_sentences.append(sentence)

    if len(related_sentences) == 0:
        related_sentences.append(review)

    aspect_text = " ".join(related_sentences)

    sentiment, confidence = predict_sentiment(aspect_text)

    return sentiment, confidence


# ==========================================================
# User Input
# ==========================================================

review = st.text_area(
    "Enter Hotel Review",
    placeholder="Example:\nThe room was spacious and clean. The receptionist was rude but breakfast was delicious.",
    height=180
)


if st.button("Analyse Review", type="primary"):

    if review.strip() == "":

        st.warning("Please enter a hotel review.")

    else:

        # ----------------------------------------------------
        # Overall Sentiment
        # ----------------------------------------------------

        overall, confidence = predict_sentiment(review)

        st.divider()

        st.subheader("Overall Sentiment")

        col1, col2 = st.columns(2)

        with col1:

            if "Positive" in overall:
                st.success(overall)

            elif "Negative" in overall:
                st.error(overall)

            else:
                st.info(overall)

        with col2:

            st.metric(
                "Confidence",
                f"{confidence:.2%}"
            )

        # ----------------------------------------------------
        # Detected Aspects
        # ----------------------------------------------------

        st.divider()

        st.subheader("Detected Aspects")

        aspects = detect_aspects(review)

        if len(aspects) == 0:

            st.info("No predefined hotel aspects detected.")

        else:

            icons = {
                "Room":"🛏️",
                "Staff":"👨‍💼",
                "Cleanliness":"🧹",
                "Location":"📍",
                "Breakfast":"🍽️",
                "WiFi":"📶",
                "Parking":"🚗",
                "Bathroom":"🚿"
            }

            st.write(
                " | ".join(
                    f"{icons[a]} **{a}**"
                    for a in aspects
                )
            )

            # ------------------------------------------------
            # Aspect Sentiment
            # ------------------------------------------------

            st.divider()

            st.subheader("Aspect Sentiment Analysis")

            results = []

            for aspect in aspects:

                sentiment, conf = aspect_sentiment(review, aspect)

                results.append({

                    "Aspect": aspect,
                    "Sentiment": sentiment,
                    "Confidence": f"{conf:.2%}"

                })

            result_df = pd.DataFrame(results)

            st.dataframe(
                result_df,
                use_container_width=True,
                hide_index=True
            )