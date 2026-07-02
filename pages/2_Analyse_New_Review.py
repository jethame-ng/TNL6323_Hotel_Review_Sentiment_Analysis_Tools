import streamlit as st
import joblib
import re

st.set_page_config(
    page_title="Analyze New Review",
    page_icon="💬",
    layout="wide"
)

st.title("💬 Analyze New Review")

st.write(
    "Enter a hotel review to predict sentiment, detect related service aspects, "
    "and generate simple management recommendations."
)

# =========================
# Aspect keyword dictionary
# =========================

aspect_keywords = {
    "Room": ["room", "bed", "bathroom", "aircon", "shower", "toilet", "clean", "dirty"],
    "Staff": ["staff", "reception", "housekeeping", "service", "manager", "doorman"],
    "Food": ["breakfast", "buffet", "restaurant", "food", "coffee", "meal"],
    "Location": ["location", "near", "mall", "shopping", "klcc", "city", "walk"],
    "Facilities": ["pool", "gym", "wifi", "spa", "lift", "elevator", "parking"]
}

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def detect_aspects(text):
    detected = []
    text = text.lower()

    for aspect, keywords in aspect_keywords.items():
        for keyword in keywords:
            if keyword in text:
                detected.append(aspect)
                break

    return detected

def generate_recommendation(sentiment, aspects):
    if sentiment == "Negative":
        if "Food" in aspects:
            return "Recommendation: Improve food quality, breakfast variety, or restaurant service."
        elif "Staff" in aspects:
            return "Recommendation: Improve staff training and customer service response."
        elif "Room" in aspects:
            return "Recommendation: Improve room cleanliness, comfort, and maintenance."
        elif "Facilities" in aspects:
            return "Recommendation: Review hotel facilities such as pool, gym, lift, Wi-Fi, or parking."
        elif "Location" in aspects:
            return "Recommendation: Provide clearer location guidance or transport information."
        else:
            return "Recommendation: Review the negative feedback and identify the main cause of dissatisfaction."

    elif sentiment == "Positive":
        return "Recommendation: Maintain the current service quality and promote the highlighted strengths."

    else:
        return "Recommendation: Monitor this feedback and identify areas that can be improved."

# =========================
# Load model and vectorizer
# =========================

model_loaded = False

try:
    model = joblib.load("model/sentiment_model.pkl")
    vectorizer = joblib.load("model/vectorizer.pkl")
    model_loaded = True
except:
    st.warning("Model files not found. Please upload sentiment_model.pkl and vectorizer.pkl into the model folder.")

# =========================
# User input
# =========================

review_input = st.text_area(
    "Enter hotel review:",
    height=150,
    placeholder="Example: The room was excellent but the breakfast was cold."
)

if st.button("Analyze Review"):

    if review_input.strip() == "":
        st.error("Please enter a review first.")

    else:
        cleaned_review = clean_text(review_input)
        detected_aspects = detect_aspects(cleaned_review)

        if model_loaded:
            review_vector = vectorizer.transform([cleaned_review])
            predicted_sentiment = model.predict(review_vector)[0]
        else:
            predicted_sentiment = "Model not available"

        st.subheader("Analysis Result")

        st.write("**Cleaned Review:**")
        st.write(cleaned_review)

        st.write("**Predicted Sentiment:**")
        st.success(predicted_sentiment)

        st.write("**Detected Aspects:**")
        if detected_aspects:
            st.write(", ".join(detected_aspects))
        else:
            st.write("No specific aspect detected.")

        st.write("**Management Recommendation:**")
        st.info(generate_recommendation(predicted_sentiment, detected_aspects))