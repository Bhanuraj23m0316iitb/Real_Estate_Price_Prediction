import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Gurgaon Real Estate Price Prediction App",
    page_icon="🏠",
    layout="wide"
)

# Main title
st.title("🏡 Gurgaon Real Estate Price Analysis")

# Load and display the image
image = Image.open(r"C:\Users\bhanu\OneDrive\Desktop\Real_est\Real_Estate_Price_Prediction\real-estate-app-master\image.jpg")
st.image(image, caption="Real Estate Deal in Action 🏘️", width=400, use_container_width=False)

# Welcome section
st.markdown("---")
st.markdown("""
## 👋 Welcome to the Gurgaon Property Insights Dashboard

This app empowers you to:
- 📈 Analyze real estate Price trends across Gurgaon
- 🏢 Explore property features like size, location, and amenities
- 📊 Visualize data for better investment decisions
""")

# Highlight box
st.success("🔍 Start exploring by selecting a page from the sidebar!")

