# import streamlit as st
# import pickle
# import pandas as pd
# import numpy as np
#
# st.set_page_config(
#     page_title="Viz Demo"
# )
#
# with open('df.pkl','rb') as file:
#     df = pickle.load(file)
#
# with open('pipeline.pkl','rb') as file:
#     pipeline = pickle.load(file)
#
# # property_type
# property_type = st.selectbox('Property Type',['flat', 'house'])
#
# # sector
# sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))
#
# bedrooms = float(st.selectbox('Number of Bedrooms', sorted(df['bedRoom'].unique().tolist())))
#
# bathrooms = float(st.selectbox('Number of bathrooms', sorted(df['bathroom'].unique().tolist())))
#
# balconies = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))
#
# property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))
#
# built_up_area = float(st.number_input('Built up area'))
#
# servant_room = float(st.selectbox('Servant Room', [0.0,1.0]))
#
# store_room = float(st.selectbox('Store Room', [0.0,1.0]))
#
# furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
#
# luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))
#
# floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))
#
# if st.button('Predict'):
#
#     # form a dataframe
#     data = [[property_type, sector, bedrooms, bathrooms, balconies, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
#     columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
#                'agePossession', 'built_up_area', 'servant room', 'store room',
#                'furnishing_type', 'luxury_category', 'floor_category']
#
#     # Convert to DataFrame
#     one_df = pd.DataFrame(data, columns=columns)
#
#     # predict
#     base_price = np.expm1(pipeline.predict(one_df))[0]
#     low = base_price -0.22
#     high = base_price + 0.22
#
#     # display
#     st.text('The price of the {} is between {} Cr and {} Cr'.format(property_type, round(low,2), round(high,2)))



import streamlit as st
import pickle
import pandas as pd
import numpy as np

# --------------------------- UI SECTION ---------------------------

def show_header():
    st.markdown("""
        <style>
            .main-title {
                font-size: 36px;
                font-weight: 700;
                color: #2C3E50;
                text-align: center;
                margin-bottom: 30px;
            }
        </style>
        <div class="main-title">🏠 Property Price Estimator</div>
    """, unsafe_allow_html=True)


def input_form(df):
    with st.form("price_prediction_form"):
        property_type = st.selectbox('Property Type', ['flat', 'house'])

        col1, col2 = st.columns(2)
        sector = col1.selectbox('Sector', sorted(df['sector'].unique()))
        property_age = col2.selectbox('Property Age', sorted(df['agePossession'].unique()))

        col1, col2, col3 = st.columns(3)
        bedrooms = float(col1.selectbox('Bedrooms', sorted(df['bedRoom'].unique())))
        bathrooms = float(col2.selectbox('Bathrooms', sorted(df['bathroom'].unique())))
        balconies = col3.selectbox('Balconies', sorted(df['balcony'].unique()))

        built_up_area = st.number_input('Built-up Area (in sq. ft)', min_value=100.0, step=10.0)

        col1, col2 = st.columns(2)
        servant_room = float(col1.selectbox('Servant Room', [0.0, 1.0]))
        store_room = float(col2.selectbox('Store Room', [0.0, 1.0]))

        col1, col2 = st.columns(2)
        furnishing_type = col1.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique()))
        luxury_category = col2.selectbox('Luxury Category', sorted(df['luxury_category'].unique()))

        floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique()))

        submitted = st.form_submit_button("Predict Price 💰")

        input_data = {
            'property_type': property_type,
            'sector': sector,
            'bedRoom': bedrooms,
            'bathroom': bathrooms,
            'balcony': balconies,
            'agePossession': property_age,
            'built_up_area': built_up_area,
            'servant room': servant_room,
            'store room': store_room,
            'furnishing_type': furnishing_type,
            'luxury_category': luxury_category,
            'floor_category': floor_category
        }

        return submitted, input_data

# --------------------------- LOGIC SECTION ---------------------------

# Page config
st.set_page_config(page_title="Price Prediction", layout="centered")

# Load model and data
with open('df.pkl','rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl','rb') as file:
    pipeline = pickle.load(file)

# Header
show_header()

# Get form input
submitted, input_data = input_form(df)

# Prediction logic
if submitted:
    one_df = pd.DataFrame([input_data])
    predicted_log_price = pipeline.predict(one_df)[0]
    base_price = np.expm1(predicted_log_price)

    low = round(base_price - 0.22, 2)
    high = round(base_price + 0.22, 2)

    st.success(f"💡 Estimated Price Range: **₹{low} Cr - ₹{high} Cr**")