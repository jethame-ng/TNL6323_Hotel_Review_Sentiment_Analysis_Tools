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

st.subheader("Project Files")

total_size = 0

for folder in ["data", "model"]:
    if os.path.exists(folder):
        st.write(f"### {folder}")

        for file in os.listdir(folder):
            path = os.path.join(folder, file)

            if os.path.isfile(path):
                size = os.path.getsize(path) / (1024 * 1024)
                total_size += os.path.getsize(path)

                st.write(f"{file} : {size:.2f} MB")

st.success(f"Total Project Size: {total_size/(1024*1024):.2f} MB")

# Function to calculate memory usage
def get_memory_usage():
    process = psutil.Process(os.getpid())
    # Convert bytes to Megabytes
    return process.memory_info().rss / (1024 ** 2) 

st.title("My Streamlit App")

# Expandable Resource Monitor in the Sidebar
with st.sidebar.expander("📊 Live Resource Monitor"):
    current_ram = get_memory_usage()
    st.metric(label="Current RAM Usage", value=f"{current_ram:.2f} MB")
    
    # Progress bar mapping against the baseline 1024 MB (1GB) limit
    ram_percentage = min(int((current_ram / 1024) * 100), 100)
    st.progress(ram_percentage)
    
    if current_ram > 800:
        st.warning("⚠️ Approaching the 1 GB baseline RAM limit!")

total, used, free = shutil.disk_usage("/")

st.write(f"Total Disk : {total // (1024**3)} GB")
st.write(f"Used Disk  : {used // (1024**3)} GB")
st.write(f"Free Disk  : {free // (1024**3)} GB")
