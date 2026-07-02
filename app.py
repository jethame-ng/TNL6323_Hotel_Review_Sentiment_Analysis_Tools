import streamlit as st
import os
import shutil

st.set_page_config(
    page_title="Hotel Review Sentiment Analysis Tools",
    page_icon="🏨",
    layout="wide"
)

st.title("🏨 Hotel Review Sentiment Analysis Tools")

st.write("""
This system helps hotel management analyse customer reviews, compare hotel performance,
identify sentiment trends, and support decision-making based on review data.
""")

st.subheader("Main Functions")

st.markdown("""
1. **Hotel Dashboard**  
   Compare overall sentiment, aspect-based sentiment, and review trends across hotels.

2. **Analyse New Review**  
   Enter a new hotel review to predict sentiment and detect related service aspects.
""")

st.info("Use the sidebar to navigate between pages.")

# st.subheader("Project Files")

# total_size = 0

# for folder in ["data", "model"]:
#     if os.path.exists(folder):
#         st.write(f"### {folder}")

#         for file in os.listdir(folder):
#             path = os.path.join(folder, file)

#             if os.path.isfile(path):
#                 size = os.path.getsize(path) / (1024 * 1024)
#                 total_size += os.path.getsize(path)

#                 st.write(f"{file} : {size:.2f} MB")

# st.success(f"Total Project Size: {total_size/(1024*1024):.2f} MB")

# total, used, free = shutil.disk_usage("/")

# st.write(f"Total Disk : {total // (1024**3)} GB")
# st.write(f"Used Disk  : {used // (1024**3)} GB")
# st.write(f"Free Disk  : {free // (1024**3)} GB")
