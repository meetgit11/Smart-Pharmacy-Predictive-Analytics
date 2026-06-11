#dashboard interface


import streamlit as st
import pandas as pd
import joblib

#loading model files
model = joblib.load("models/demand_forecasting_model.pkl")
sku_encoder = joblib.load("models/sku_encoder.pkl")
location_encoder = joblib.load("models/location_encoder.pkl")
risk_encoder = joblib.load("models/risk_encoder.pkl")

st.set_page_config(
    page_title="Smart Pharmacy Predictive Analytics",
    layout="wide"
)

st.title("💊 Smart Pharmacy Predictive Analytics System")

st.markdown("""
### IEEE EMBS Internship Project

Developed By:
- Ishwari Tapkir
- Arko Mistry
- Meet Patil
""")

#Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "Demand Forecasting",
        "Inventory Monitoring",
        "Product Intelligence"
    ]
)

#Home Page
if page == "Home":

    st.header("Project Overview")

    st.write("""
    Smart Pharmacy Predictive Analytics System uses
    Machine Learning and Inventory Analytics
    to improve pharmacy inventory management.
    """)

    st.subheader("Modules")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Forecast Accuracy",
            "99.97%"
        )

    with col2:
        st.metric(
            "Critical Alerts",
            "1607"
        )
    
    with col3:
        st.metric(
            "Products Available",
            "2000"
        )
    
    st.subheader("Project Highlights")

    st.success("AI-Powered Demand Forecasting")

    st.success("Real-Time Inventory Monitoring")

    st.success("Medicine Product Intelligence")

#Demand Forecasting
elif page == "Demand Forecasting":

    st.header("Demand Forecasting Module")

    sku = st.selectbox(
        "SKU",
        sku_encoder.classes_
    )

    location=st.selectbox(
        "Location",
        location_encoder.classes_
    )

    lead_time=st.number_input(
        "Lead Time",
        min_value=1,
        max_value=50,
        value=10
    )

    risk_level=st.selectbox(
        "Risk Level",
        risk_encoder.classes_
    )

    month = st.slider(
        "Month",
        1,
        12,
        6
    )

    day=st.slider(
        "Day",
        1,
        31,
        15
    )

    weekday = st.slider(
        "Weekday",
        0,
        6,
        2
    )

    if st.button("Predict Demand"):

        sku_encoded = sku_encoder.transform(
            [sku]
        )[0]

        location_encoded=(
            location_encoder.transform(
                [location]
            )[0]
        )

        risk_encoded = (
            risk_encoder.transform(
                [risk_level]
            )[0]
        )

        prediction = model.predict(
            [[
                sku_encoded,
                location_encoded,
                lead_time,
                month,
                day,
                weekday,
                risk_encoded
            ]]
        )

        st.success(
            f"Predicted Quantity Sold: {prediction[0]:.2f}"
        )

#Inventory Monitoring
elif page == "Inventory Monitoring":

    st.header("Inventory Monitoring Module")

    inventory_df = pd.read_csv(
        "outputs/inventory_alerts.csv"
    )
    critical_count=(
        inventory_df[
            inventory_df[
                "Inventory_Status"
            ] == "Critical"
        ].shape[0]
    )

    st.metric(
        "Critical Inventory Alerts",
        critical_count
    )


    st.subheader("Inventory Alerts")
    st.dataframe(
        inventory_df,
        use_container_width=True
    )

    

#Product Intelligence
elif page == "Product Intelligence":

    st.header("Product Intelligence Module")

    product_df = pd.read_csv(
        "outputs/product_intelligence.csv"
    )

    st.subheader("Product Intelligence Data")

    st.dataframe(
        product_df,
        use_container_width=True
    )

    medicine_name = st.text_input("Search Medicine by Brandname")

    if medicine_name:
        filtered_df=product_df[
            product_df[
                "brand_name"
            ].str.contains(
                medicine_name,
                case=False,
                na=False
            )
        ]

        st.dataframe(
            filtered_df,
            use_container_width=True
        )