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

#st.title("💊 Smart Pharmacy Predictive Analytics System")
st.markdown("""
#💊 Smart Pharmacy Predictive Analytics System
### AI Powered Inventory Intelligence for Healthcare
Predict • Monitor • Optimize
""")

st.markdown("""
### IEEE EMBS Internship Project

Developed By:
- Ishwari Tapkir
- Arko Mistry
- Meet Patil
""")

#Sidebar
st.sidebar.title("Navigation")

st.sidebar.image(
    "https://img.icons8.com/color/96/pill.png",
    width=80
)

st.sidebar.markdown("## Smart Pharmacy")
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

    inventory_df = pd.read_csv(
        "outputs/inventory_alerts.csv"
    )

    product_df = pd.read_csv(
        "outputs/product_intelligence.csv"
    )

    critical_alerts = (
        inventory_df[
            inventory_df["Inventory_Status"] == "Critical"
        ].shape[0]
    )

    total_products = len(product_df)

    healthy_products = (
        inventory_df[
            inventory_df["Inventory_Status"] == "Healthy"
        ].shape[0]
    )

    health_score=round(
        (healthy_products/len(inventory_df))*100,
        2
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            label=" 🏥 Inventory Health",
            value=f"{health_score}%"
        )

    with col2:
        st.metric(
            label="Critical Alerts",
            value=critical_alerts
        )
    
    with col3:
        st.metric(
            label="💊 Products Available",
            value=total_products
        )

    with col4:
        st.metric(
            label="Healthy Inventory",
            value=healthy_products
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

    st.divider()

    st.subheader("📋 Recent Inventory Updates")

    recent_records = inventory_df.tail(5)

    st.dataframe(
        recent_records,
        use_container_width=True
    )

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

        from datetime import datetime

        history=pd.DataFrame({
            "date":[datetime.now()],
            "sku":[sku],
            "location":[location],
            "prediction":[predicted_qty]
        })

        history.to_csv(
            "outputs/prediction_history.csv",
            mode="a",
            header=False,
            index=False
        )

        st.metric(
            " 📦 Predicted Quantity Sold",
            predicted_qty
        )

        if predicted_qty<8:
            st.warning(
                " ⚠️ Low Demand Expected."
            )
            st.info(
                "Recommendation: Avoid overstocking."
            )
        
        elif predicted_qty<18:
            st.success(
                " ✅ Normal Demand Expected."
            )

            st.info(
                "Recommendation: Maintain current stock."
            )
        
        else:
            st.error(
                " 🚨 High Demand Expected."
            )

            st.info(
                "Recommendation: Increase inventory."
            )

        #prediction history
        st.subheader(
            " 📈 Prediction History"
        )

        history_df = pd.read_csv(
            "outputs/prediction_history.csv"
        )

        st.dataframe(
            history_df.tail(10),
            use_container_width=True
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

    product_df=pd.read_csv(
        "outputs/product_intelligence.csv"
    )

    total_products = product_df[
        "brand_name"
    ].nunique()

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
    
    critical_df=inventory_df[
        inventory_df["Inventory_Status"] == "Critical"
    ]

    st.subheader(
        " 🚨 Critical Stock Alerts"
    )

    st.dataframe(
        critical_df.head(10),
        use_container_width=True
    )

    st.subheader("➕ Add New Inventory Record")

    with st.form("inventory_form"):
        location = st.selectbox(
            "Location",
            inventory_df["location"].unique()
        )

        item = st.text_input(
            "Medicine Name"
        )

        stock = st.number_input(
            "Current Stock",
            min_value=0
        )

        supplier = st.text_input(
            "Supplier"
        )

        submitted = st.form_submit_button(
            "Add Record"
        )
    
    #if item=="":
    #if supplier=="":
    
    if submitted:
        if not item.strip():
            st.error("Medicine name required")
        elif not supplier.strip():
            st.error("Supplier name required")
        else:
            if stock<50:
                status = "Critical"
                recommendation = "Reorder Immediately"
                alert = "Low Stock Alert"
        
            elif stock<100:
                status = "Warning"
                recommendation = "Reorder Soon"
                alert = "OK"
        
            else:
                status = "Healthy"
                recommendation = "No Action Required"
                alert = "OK"

            new_row = pd.DataFrame(
                [{
                    "date": pd.Timestamp.now().date(),
                    "location": location,
                    "item": item,
                    "closing_stock": stock,
                    "Inventory_Status": status,
                    "Recommendation": recommendation,
                    "Alert": alert,
                    "supplier": supplier
                }]
            )

            inventory_df = pd.concat(
                [inventory_df, new_row],
                ignore_index=True
            )

            inventory_df.to_csv(
                "outputs/inventory_alerts.csv",
                index=False
            )

            st.success(
                "Inventory record added successfully."
            )

            st.rerun()


    st.subheader("Inventory Alerts")
    
    
    search_item = st.text_input(
        " 🔍 Search Medicine"
    )

    if search_item:
        inventory_df = inventory_df[
            inventory_df["item"].str.contains(
                search_item,
                case=False,
                na=False
            )
        ]

    st.dataframe(
        inventory_df,
        use_container_width=True
    )

    csv = inventory_df.to_csv(index=False)

    st.download_button(
        label=" 📥 Dashboard Inventory Report",
        data=csv,
        file_name="inventory_report.csv",
        mime="text/csv"
    )

    #Trend Analytics
    st.subheader(" 📈 Inventory Stock Trend")

    inventory_df["date"]=pd.to_datetime(
        inventory_df["date"],
        errors="coerce"
    )

    trend_df=(
        inventory_df.groupby("date")["closing_stock"]
        .sum()
        .reset_index()
        .sort_values("date")
    )

    st.line_chart(
        trend_df.set_index("date")
    )

    #Supplier Anaytics
    st.subheader(" 🏭 Supplier Distribution")

    supplier_counts=(
        inventory_df["supplier"]
        .value_counts()
    )

    st.bar_chart(
        supplier_counts
    )

    #Top Medicien Analysis
    st.subheader(
        " 💊 Top Medicines by Inventory Records"
    )

    medicine_counts = (
        inventory_df["item"]
        .value_counts()
        .head(10)
    )

    st.bar_chart(
        medicine_counts
    )


    status_counts =inventory_df["Inventory_Status"].value_counts()

    fig, ax = plt.subplots(figsize=(5,5))

    ax.pie(
        status_counts,
        labels=status_counts.index,
        autopct="%1.1f%%"
    )

    ax.set_title("Inventory Status Distribution")

    #st.pyplot(fig)

    location_status = pd.crosstab(
        inventory_df["location"],
        inventory_df["Inventory_Status"]
    )

    #st.bar_chart(location_status)

    col1, col2 =st.columns(2)

    with col1:
        st.pyplot(fig)
    
    with col2:
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

            #PI KPI
            total_found=len(filtered_df)

            avg_rating=round(
                filtered_df["rating"].mean(),
                2
            )

            manufacturers=(
                filtered_df["manufacturer"]
                .nunique()
            )

            col1,col2,col3=st.columns(3)

            with col1:
                st.metric(
                    "Products Found",
                    total_found
                )
            
            with col2:
                st.metric(
                    "Average Rating",
                    avg_rating
                )
            
            with col3:
                st.metric(
                    "Manufacturers",
                    manufacturers
                )


            st.subheader("Medicine Summary")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Brand",
                    #selected["brand_name"]
                    #medicine_name.title()
                    filtered_df["brand_name"].mode()[0]
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