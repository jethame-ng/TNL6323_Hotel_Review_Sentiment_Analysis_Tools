import streamlit as st

st.set_page_config(
    page_title="Intelligent Hotel Review Sentiment Analysis System",
    page_icon="🏨",
    layout="wide"
)

# =====================================================
# Header
# =====================================================

st.title("🏨 Intelligent Hotel Review Sentiment Analysis System")

st.markdown("""
### AI-Powered Hotel Review Analytics & Decision Support Platform

This intelligent system assists hotel management in analysing customer reviews using
**AI-powered sentiment analysis**, **aspect-based analytics**, **benchmark comparison**,
and an **LLM-powered management assistant** to support data-driven decision making.
""")

st.divider()

# =====================================================
# System Features
# =====================================================

st.header("🚀 System Features")

col1, col2 = st.columns(2)

# -----------------------
# Left Column
# -----------------------

with col1:

    with st.container(border=True):

        st.subheader("📊 Hotel Dashboard")

        st.markdown("""
- 📌 Overall sentiment summary
- 📈 Sentiment trend analysis
- ⭐ Aspect-based analytics
- 🏆 Hotel benchmark comparison
- 💡 Management recommendations
- 🤖 AI Hotel Management Assistant
""")

    st.write("")

    with st.container(border=True):

        st.subheader("🤖 AI Hotel Management Assistant")

        st.markdown("""
- 💬 Executive summary generation
- 🏆 Competitor benchmarking
- ⚠ Identify service weaknesses
- 💪 Highlight hotel strengths
- 💡 Management recommendations
- ❓ Interactive question answering
""")

# -----------------------
# Right Column
# -----------------------

with col2:

    with st.container(border=True):

        st.subheader("📝 Analyse New Review")

        st.markdown("""
- 😊 Overall sentiment prediction
- ⭐ Hotel aspect detection
- 📑 Clause segmentation
- 📊 Aspect-level sentiment analysis
- 🎯 Prediction confidence score
""")

    st.write("")

with st.container(border=True):

    st.subheader("🎯 Target Users")

    st.markdown("""
This system is intended for hotel management to:

- 📊 Monitor customer satisfaction
- ⭐ Analyse aspect-based feedback
- 🏆 Benchmark against competitors
- 💡 Identify service improvement opportunities
- 🤖 Obtain AI-powered management recommendations
""")

st.divider()

# =====================================================
# Technologies
# =====================================================

st.header("🛠 Technologies")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.metric("Sentiment Model", "DistilBERT")
tech2.metric("LLM Assistant", "Gemini 2.5 Flash")
tech3.metric("Framework", "Streamlit")
tech4.metric("Language", "Python")

st.divider()

st.success("👈 Use the sidebar to navigate between the system modules.")