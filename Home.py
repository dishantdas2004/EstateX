import streamlit as st
from PIL import Image

# Page Config
st.set_page_config(page_title="EstateX | Home", page_icon="🏡", layout="wide")

# Branding
st.markdown("<h1 style='text-align: center; color:#2E8B57;'>🏡 Welcome to EstateX</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color:#555;'>Your AI-powered platform for Price Prediction, Smart Recommendations & Market Insights</h4>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar navigation info
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4221/4221423.png", width=100)
st.sidebar.title("🏠 EstateX")
st.sidebar.markdown("### Navigate:")
st.sidebar.markdown("- 💰 Price Prediction")
st.sidebar.markdown("- 📊 Market Analysis")
st.sidebar.markdown("- 🏙️ Property Recommendation")
st.sidebar.markdown("- 📌 Insights & Charts")

# Home page interactive buttons
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/2910/2910791.png", width=80)
    st.subheader("💰 Price Prediction")
    st.write("Predict housing prices using advanced ML models.")
    if st.button("Go to Price Prediction"):
        st.switch_page("pages/1_Price Predictor.py")

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/4148/4148460.png", width=80)
    st.subheader("📊 Market Analysis")
    st.write("Visualize pricing trends and understand key patterns.")
    if st.button("Go to Market Analysis"):
        st.switch_page("pages/2_Analysis App.py")

with col3:
    st.image("https://cdn-icons-png.flaticon.com/512/706/706830.png", width=80)
    st.subheader("🏙️ Property Recommendations")
    st.write("Get personalized property suggestions based on your needs.")
    if st.button("Go to Recommendations"):
        st.switch_page("pages/3_Recommend Apartments.py")

with col4:
    st.image("https://cdn-icons-png.flaticon.com/512/4341/4341139.png", width=80)
    st.subheader("📌 Insights & Charts")
    st.write("Explore location-based insights, price distributions & more.")
    if st.button("Go to Insights & Charts"):
        st.switch_page("pages/4_Insights.py")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center;'><h3 style='color:#2E8B57;'>Let EstateX be your guide to smart property decisions.</h3></div>", unsafe_allow_html=True)
