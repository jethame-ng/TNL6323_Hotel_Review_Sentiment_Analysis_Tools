import re
import streamlit as st
import pandas as pd
from utils.predictor import predict_sentiment,split_sentences

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

# Contrast words
contrast_words=[
    "but",
    "however",
    "although",
    "though",
    "yet",
    "whereas"
]

# Detect aspects
def detect_aspects(text):
    text=text.lower()
    detected=[]

    for aspect,keywords in aspect_keywords.items():
        for keyword in keywords:
            if re.search(rf"\b{re.escape(keyword)}\b",text):
                detected.append(aspect)
                break

    return detected

# Detect aspect positions
def get_aspect_positions(text):
    text_lower=text.lower()
    positions=[]

    for aspect,keywords in aspect_keywords.items():
        for keyword in keywords:
            for match in re.finditer(rf"\b{re.escape(keyword)}\b",text_lower):
                positions.append({
                    "aspect":aspect,
                    "position":match.start()
                })

    positions.sort(key=lambda x:x["position"])

    return positions

# Recursive contrast splitter
def split_contrast_clause(sentence):
    sentence=sentence.strip()

    if not sentence:
        return []

    # Handle sentences starting with "Although ..."
    m=re.match(
        r'(?i)^\s*although\s+(.+?),\s*(.+)$',
        sentence
    )

    if m:
        left=m.group(1).strip()
        right=m.group(2).strip()

        left_aspects=detect_aspects(left)
        right_aspects=detect_aspects(right)

        if left_aspects and right_aspects and left_aspects!=right_aspects:
            return split_contrast_clause(left)+split_contrast_clause(right)

    # Original logic
    positions=get_aspect_positions(sentence)

    if len(positions)<2:
        return [sentence]

    sentence_lower=sentence.lower()

    for word in ["but","however","though","yet","whereas"]:
        for match in re.finditer(rf"\b{word}\b",sentence_lower):
            split_pos=match.start()

            left_positions=[p for p in positions if p["position"]<split_pos]
            right_positions=[p for p in positions if p["position"]>split_pos]

            if not left_positions or not right_positions:
                continue

            if left_positions[-1]["aspect"]==right_positions[0]["aspect"]:
                continue

            left=sentence[:split_pos].strip(" ,")
            right=sentence[match.end():].strip(" ,")

            return (
                split_contrast_clause(left)+
                split_contrast_clause(right)
            )

    return [sentence]
# Aspect sentiment
def aspect_sentiment(review,aspect):
    clauses=[]

    for sentence in split_sentences(review):
        clauses.extend(split_contrast_clause(sentence))

    keywords=aspect_keywords[aspect]

    related=[
        clause
        for clause in clauses
        if any(
            re.search(rf"\b{re.escape(keyword)}\b",clause.lower())
            for keyword in keywords
        )
    ]

    if not related:
        related=[review]

    return predict_sentiment(" ".join(related))

# User input
review=st.text_area(
    "Enter Hotel Review",
    placeholder=(
        "Example:\n"
        "The room was spacious and clean, but the receptionist was rude "
        "although the breakfast was delicious."
    ),
    height=180
)

# Analyse review
if st.button("Analyse Review",type="primary"):
    if not review.strip():
        st.warning("Please enter a hotel review.")
    else:
        # Overall sentiment
        overall,confidence=predict_sentiment(review)

        st.divider()
        st.subheader("Overall Sentiment")

        col1,col2=st.columns(2)

        with col1:
            if "Positive" in overall:
                st.success(overall)
            elif "Negative" in overall:
                st.error(overall)
            else:
                st.info(overall)

        with col2:
            st.metric("Confidence",f"{confidence:.2%}")

        # Processed clauses
        processed_clauses=[]

        for sentence in split_sentences(review):
            processed_clauses.extend(split_contrast_clause(sentence))

        st.divider()
        st.subheader("Processed Clauses")

        for i,clause in enumerate(processed_clauses,1):
            st.write(f"**Clause {i}:** {clause}")

        # Detect aspects
        aspects=detect_aspects(review)

        st.divider()
        st.subheader("Detected Aspects")

        icons={
            "Room":"🏨",
            "Staff":"🤝",
            "Cleanliness":"✨",
            "Location":"🗺️",
            "Breakfast":"🥐",
            "WiFi":"📡",
            "Parking":"🅿️",
            "Bathroom":"🛁"
        }

        if not aspects:
            st.info("No predefined hotel aspects detected.")
        else:
            st.write(" | ".join(f"{icons.get(a,'📌')} **{a}**" for a in aspects))

        # Aspect sentiment
        st.divider()
        st.subheader("Aspect Sentiment Analysis")

        results=[]
        positive_count=neutral_count=negative_count=0

        for aspect in aspects:
            sentiment,conf=aspect_sentiment(review,aspect)

            if "Positive" in sentiment:
                positive_count+=1
            elif "Negative" in sentiment:
                negative_count+=1
            else:
                neutral_count+=1

            keywords=aspect_keywords[aspect]

            related_clause=next(
                (
                    clause
                    for clause in processed_clauses
                    if any(
                        re.search(rf"\b{re.escape(keyword)}\b",clause.lower())
                        for keyword in keywords
                    )
                ),
                ""
            )

            results.append({
                "Aspect":aspect,
                "Clause Used":related_clause,
                "Sentiment":sentiment,
                "Confidence":f"{conf:.2%}"
            })

        if results:
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

**Overall Sentiment:** {overall}

**Confidence:** {confidence:.2%}

**Detected Aspects:** {", ".join(aspects) if aspects else "None"}

**Positive Aspects:** {positive_count}

**Neutral Aspects:** {neutral_count}

**Negative Aspects:** {negative_count}

**Total Processed Clauses:** {len(processed_clauses)}
""")

        # Debug information
        with st.expander("🔍 View Aspect Detection Details"):
            for clause in processed_clauses:
                detected=detect_aspects(clause)

                st.markdown(f"""
**Clause**

> {clause}

**Detected Aspects**

{", ".join(detected) if detected else "None"}
""")