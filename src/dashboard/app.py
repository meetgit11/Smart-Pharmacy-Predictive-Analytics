#dashboard interface


import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

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

    st.header(" 🏥 Project Overview")

    st.markdown("""
    Smart Pharmacy Predictive Analytics System helps pharmacies
    predict medicine demand, monitor inventory levels, and analyze 
    medicine products using Machine Learning.
    """)

    #st.subheader("Modules")

    st.divider()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label="📈 Forecast Accuracy",
            value="99.97%"
        )

    with col2:
        st.metric(
            label="Critical Alerts",
            value="1607"
        )
    
    with col3:
        st.metric(
            label="💊 Products Available",
            value="2000"
        )
    
    st.divider()

    st.subheader("🎯 Core Modules")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
        Demand Forecasting
                
        Predict future medicine demand using ML.
        """)
    
    with col2:
        st.warning("""
        Inventory Monitoring
                   
        Detect low stock and critical inventory.
        """)

    with col3:
        st.success("""
        Product Intelligence
                   
        Analyse medicines, ratings and availability.
        """)
    
    st.divider()

    st.subheader("📋 Project Highlights")

    st.success("📈 AI-Powered Demand Forecasting model deployed")

    st.success("📦 Real-Time Inventory Monitoring dashboard")

    st.success("💊 Medicine Product Intelligence search engine")

    st.success("Interactive analytics dashboard")

#=============================================================
#Demand Forecasting Module
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
        predicted_qty=round(prediction[0],2)

        st.metric(
            "Predicted Quantity Sold",
            predicted_qty
        )

        if predicted_qty<8:
            st.warning(
                "Low demand expected. Avoid overstocking."
            )
        
        elif predicted_qty<18:
            st.success(
                "Normal demand expected."
            )
        
        else:
            st.error(
                "High demand expected. Increase stock availability."
            )
# ========================================================================
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

    warning_count=(
        inventory_df[
            inventory_df["Inventory_Status"] == "Warning"
        ].shape[0]
    )

    healthy_count=(
        inventory_df[
            inventory_df["Inventory_Status"] == "Healthy"
        ].shape[0]
    )

    col1, col2, col3 =st.columns(3)
    with col1:
        st.metric(
            "🚨 Critical",
            critical_count
        )
    
    with col2:
        st.metric(
            "⚠️ Warning",
            warning_count
        )
    
    with col3:
        st.metric(
            "✅ Healthy",
            healthy_count
        )



    st.subheader("Inventory Alerts")
    st.dataframe(
        inventory_df,
        use_container_width=True
    )

    status_counts =inventory_df["Inventory_Status"].value_counts()

    fig, ax = plt.subplots(figsize=(3,3))

    ax.pie(
        status_counts,
        labels=status_counts.index,
        autopct="%1.1f%%"
    )

    ax.set_title("Inventory Status Distribution")

    st.pyplot(fig)

    location_status = pd.crosstab(
        inventory_df["location"],
        inventory_df["Inventory_Status"]
    )

    st.bar_chart(location_status)

    
#===============================================================
#Product Intelligence
elif page == "Product Intelligence":

    st.header("Product Intelligence Module")

    product_df = pd.read_csv(
        "outputs/product_intelligence.csv"
    )

    #st.subheader("Product Intelligence Data")
    
    #st.dataframe(
    #    product_df,
    #   use_container_width=True
    #)

    #medicine_name = st.text_input("Search Product Brand ")
    
    #dataset preview
    st.subheader("Dataset Preview")

    st.dataframe(
        product_df.head(10),
        use_container_width=True
    )
    st.subheader("Search Medicine")

    medicine_name = st.text_input(
        "Enter Brand Name"
    )


    if medicine_name:
        
        filtered_df=product_df[
            product_df["brand_name"].str.contains(
                medicine_name,
                case=False,
                na=False
            )
        ]

        if not filtered_df.empty:

            #selected = filtered_df.iloc[0]
            avg_rating =filtered_df["rating"].mean()

            availability_count = (
                filtered_df["availability_status"]
                .mode()[0]
            )
            st.subheader("Medicine Summary")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Brand",
                    #selected["brand_name"]
                    medicine_name.title()
                )
            
            with col2:
                st.metric(
                    "Average Rating",
                    round(avg_rating,2)
                )

            with col3:
                st.metric(
                    "Most Common Availability",
                    availability_count
                )

            if len(filtered_df)>0:
                st.dataframe(
                    filtered_df,
                    use_container_width=True
                )

                availability = (
                    filtered_df["availability_status"]
                    .value_counts()
                )

                st.bar_chart(availability)

                fig, ax=plt.subplots()

                ax.hist(
                    filtered_df["rating"],
                    bins=10
                )

                ax.set_title(
                    "Rating Distribution"
                )

                st.pyplot(fig)

        else:

            st.warning(
                "No medicine found. Please enter correct data"
            )        