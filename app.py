import streamlit as st

st.set_page_config(
    page_title="Hotel Review Sentiment Analysis Tools",
    page_icon="🏨",
    layout="wide"
)

st.title("🏨 Hotel Review Sentiment Analysis Tools")

st.write("""
This system helps hotel management analyze customer reviews, compare hotel performance,
identify sentiment trends, and support decision-making based on review data.
""")

st.subheader("Main Functions")

st.markdown("""
1. **Hotel Dashboard**  
   Compare overall sentiment, aspect-based sentiment, and review trends across hotels.

2. **Analyze New Review**  
   Enter a new hotel review to predict sentiment and detect related service aspects.
""")

st.info("Use the sidebar to navigate between pages.")
