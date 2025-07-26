# 🏡 EstateX - Smart Real Estate Assistant

**EstateX** is a powerful and interactive web application built with Streamlit that helps users:
- Predict apartment prices 💰
- Analyze property features 📊
- Gain valuable insights from housing data 🔍
- Explore personalized apartment recommendations 🧠

---

## 🚀 Features

### 📈 Price Prediction
Accurately predict the price of an apartment using a trained machine learning model based on key features like location, BHK, square footage, etc.

### 📊 Data Analysis
Visualize property trends through charts, histograms, and interactive plots to better understand:
- Price vs. area
- Price distribution by location
- Location-wise comparisons

### 📌 Location-Based Recommendations
Using content-based filtering and cosine similarity, get recommendations for apartments similar to your preferences.

### 📚 Data Insights
Explore hidden insights and patterns in housing data, such as:
- Best-value localities
- Clusters of high-demand areas
- Affordability zones

---

## 🧠 Tech Stack

- **Python** 🐍
- **Streamlit** – Web UI
- **Scikit-learn** – Machine Learning
- **Pandas / NumPy** – Data manipulation
- **Matplotlib / Seaborn** – Visualization
- **Pickle** – Model & similarity storage
- **Git LFS** – For large `.pkl` files

---

## 📁 Project Structure

<pre> EstateX/ ├── datasets/ │ ├── cosine_sim1.pkl │ ├── cosine_sim2.pkl │ ├── cosine_sim3.pkl │ ├── data_viz1.csv │ ├── feature_text.pkl │ └── location_distance.pkl ├── pages/ │ ├── 1_Price Predictor.py │ ├── 2_Analysis App.py │ ├── 3_Recommend Apartments.py │ └── 4_Insights.py ├── Home.py ├── compress_pipeline.py ├── df.pkl ├── pipeline_compressed.pkl ├── requirements.txt ├── .gitignore ├── .gitattributes  </pre>

---

## 🧪 Running the App

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dishantdas2004/EstateX.git
   cd EstateX
   
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run the streamlit app:**
   ```bash
   streamlit run Home.py


