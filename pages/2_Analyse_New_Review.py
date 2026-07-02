import streamlit as st
import pandas as pd
from utils.predictor import predict_sentiment,split_sentences

st.set_page_config(
    page_title="Analyse New Review",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Analyse New Review")
st.write("Enter a hotel review to predict the overall sentiment, detect mentioned aspects, and analyse the sentiment of each aspect.")

# Aspect dictionary
aspect_keywords={
    "Room":["room","bed","pillow","suite","balcony"],
    "Staff":["staff","reception","receptionist","employee","manager","service"],
    "Cleanliness":["clean","dirty","cleanliness","smell","dust"],
    "Location":["location","near","far","airport","station"],
    "Breakfast":["breakfast","buffet","food","meal","restaurant"],
    "WiFi":["wifi","internet","network"],
    "Parking":["parking","car park"],
    "Bathroom":["bathroom","toilet","shower"]
}

# Detect aspects
def detect_aspects(review):
    review_lower=review.lower()
    return [
        aspect
        for aspect,keywords in aspect_keywords.items()
        if any(keyword in review_lower for keyword in keywords)
    ]

# Predict aspect sentiment
def aspect_sentiment(review,aspect):
    keywords=aspect_keywords[aspect]

    related_sentences=[
        sentence
        for sentence in split_sentences(review)
        if any(keyword in sentence.lower() for keyword in keywords)
    ]

    if not related_sentences:
        related_sentences=[review]

    return predict_sentiment(" ".join(related_sentences))

# User input
review=st.text_area(
    "Enter Hotel Review",
    placeholder=(
        "Example:\n"
        "The room was spacious and clean. "
        "The receptionist was rude but breakfast was delicious."
    ),
    height=180
)

if st.button("Analyse Review",type="primary"):
    if review.strip()=="":
        st.warning("Please enter a hotel review.")
    else:
        aspects=detect_aspects(review)

        positive_count=neutral_count=negative_count=0
        confidence_list=[]
        results=[]

        for aspect in aspects:
            sentiment,conf=aspect_sentiment(review,aspect)

            confidence_list.append(conf)

            if sentiment=="Positive":
                positive_count+=1
                display_sentiment="😊 Positive"
            elif sentiment=="Negative":
                negative_count+=1
                display_sentiment="☹ Negative"
            else:
                neutral_count+=1
                display_sentiment="😐 Neutral"

            results.append({
                "Aspect":aspect,
                "Sentiment":display_sentiment,
                "Confidence":f"{conf:.2%}"
            })

        # Overall sentiment
        if positive_count>=negative_count and positive_count>=neutral_count:
            overall="Positive"
            overall_display="😊 Positive"
        elif negative_count>=positive_count and negative_count>=neutral_count:
            overall="Negative"
            overall_display="☹ Negative"
        else:
            overall="Neutral"
            overall_display="😐 Neutral"

        overall_confidence=sum(confidence_list)/len(confidence_list) if confidence_list else 0

        # Overall sentiment UI
        st.divider()
        st.subheader("Overall Sentiment")

        col1,col2=st.columns([3,1])

        with col1:
            if overall=="Positive":
                st.success(overall_display)
            elif overall=="Negative":
                st.error(overall_display)
            else:
                st.info(overall_display)

        with col2:
            st.metric("Confidence",f"{overall_confidence:.2%}")

        # Detected aspects
        st.divider()
        st.subheader("Detected Aspects")

        if not aspects:
            st.info("No predefined hotel aspects detected.")
        else:
            icons={
                "Room": "🏨",   
                "Staff": "🤝",         
                "Cleanliness": "✨",  
                "Location": "🗺️",     
                "Breakfast": "🥐",    
                "WiFi": "📡",       
                "Parking": "🅿️",      
                "Bathroom": "🛁"        
            }

            st.write(" | ".join(f"{icons[a]} **{a}**" for a in aspects))

        # Aspect sentiment analysis
        st.divider()
        st.subheader("Aspect Sentiment Analysis")

        st.dataframe(
            pd.DataFrame(results),
            use_container_width=True,
            hide_index=True
        )

        # Summary
        st.divider()
        st.subheader("Analysis Summary")

        st.markdown(f"""
### Prediction Summary

**Overall Sentiment:** {overall_display}

**Confidence:** {overall_confidence:.2%}

**Detected Aspects:** {", ".join(aspects) if aspects else "None"}

**Positive Aspects:** {positive_count}

**Neutral Aspects:** {neutral_count}

**Negative Aspects:** {negative_count}
""")