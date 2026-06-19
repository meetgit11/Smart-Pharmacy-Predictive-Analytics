#dashboard interface


import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import os

from auth import login

#loading model files
model = joblib.load("models/demand_forecasting_model.pkl")
sku_encoder = joblib.load("models/sku_encoder.pkl")
location_encoder = joblib.load("models/location_encoder.pkl")
risk_encoder = joblib.load("models/risk_encoder.pkl")

st.set_page_config(
    page_title="Smart Pharmacy Predictive Analytics",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state["logged_in"]=False

if not st.session_state["logged_in"]:
    login()
    st.stop()

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
if "role" in st.session_state:
    st.sidebar.success(f"👤{st.session_state['role']}")
page = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "Demand Forecasting",
        "Inventory Monitoring",
        "Product Intelligence"
    ]
)

st.sidebar.divider()

if st.sidebar.button(" 🚪 Logout"):
    st.session_state["logged_in"]=False

    st.rerun()

#Home Page
if page == "Home":

    st.header(" 🏥 Project Overview")

    st.markdown("""
    Smart Pharmacy Predictive Analytics System helps pharmacies
    predict medicine demand, monitor inventory levels, and analyze 
    medicine products using Machine Learning.
    """)

    if "role" in st.session_state:
        st.info(f"Welcome {st.session_state['role']} to Smart Pharmacy Analytics Platform.")

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

    #executive kpi dashboard upgrade
    total_records = len(inventory_df)

    total_suppliers = (
        inventory_df["supplier"]
        .nunique()
    )

    if total_records>0:
        critical_percent = round(
            (critical_alerts / total_records)*100,
            2
        )
    else:
        critical_percent=0

    total_products = len(product_df)

    healthy_products = (
        inventory_df[
            inventory_df["Inventory_Status"] == "Healthy"
        ].shape[0]
    )
    if len(inventory_df)>0:
        health_score=round(
            (healthy_products/len(inventory_df))*100,
            2
        )
    else:
        health_score=0

    st.subheader(
        " 📊 Inventory Health Score"
    )

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=health_score,
            title={
                "text":"Inventory Health"
            },
            gauge={
                "axis":{
                    "range":[0,100]
                }
            }
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    col1, col2, col3, col4, col5, col6 = st.columns(6)
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

    with col5:
        st.metric(
            " 🏭 Suppliers",
            total_suppliers
        )
    
    with col6:
        st.metric(
            " 🚨 Critical % ",
            f"{critical_percent}%"
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

    #smart insights panel
    st.subheader(" 🧠 AI Insights")

    inventory_df=pd.read_csv(
        "outputs/inventory_alerts.csv"
    )

    critical_count=(
        inventory_df[
            inventory_df["Inventory_Status"] == "Critical"
        ].shape[0]
    )

    if critical_count>1500:
        st.error(f" ⚠️ {critical_count} products are in critical condition and require immediate replenishment.")

    warning_count=(
        inventory_df[
            inventory_df["Inventory_Status"] == "Warning"
        ].shape[0]
    )

    if warning_count>1000:
        st.warning(f" 📦 {warning_count} products may become low stock soon.")
    
    healthy_count=(
        inventory_df[
            inventory_df["Inventory_Status"]=="Healthy"
        ].shape[0]
    )

    st.success(
        f" ✅ {healthy_count} products are currently healthy"
    )


    st.subheader("📋 Recent Inventory Updates")

    recent_records = inventory_df.tail(5)

    st.dataframe(
        recent_records,
        use_container_width=True
    )

    st.subheader(" 📌 Executive Insights")

    if critical_percent>35:
        st.error(
            "Critical Inventory is above safe threshold."
        )

    elif critical_percent>20:
        st.warning(
            "Inventory requires attention."
        )

    else:
        st.success("Inventory is operating normally.")
    
    #Executive summary
    st.subheader(" 📑 Executive Summary")

    top_supplier=(
        inventory_df["supplier"]
        .value_counts()
        .idxmax()
    )

    top_medicine=(
        inventory_df["item"]
        .value_counts()
        .idxmax()
    )

    st.info(
        f""" 
        Top Supplier: {top_supplier}

        Most Recorded Medicine: {top_medicine}

        Total Inventory Records: {len(inventory_df)}
        
        Critical Alerts: {critical_alerts}
        """
    )

    st.subheader(" 🤖 Inventory Recommendation Center")

    critical_count=(
        inventory_df[inventory_df["Inventory_Status"]=="Critical"].shape[0]
    )

    warning_count=(
        inventory_df[inventory_df["Inventory_Status"] == "Warning"].shape[0]
    )

    if critical_count>1500:
        st.error(
            "Immediate bulk procurement required. Critical inventory exceeds safe limits."
        )
    
    elif critical_count>1000:
        st.warning("Inventory requires replenishment planning within 3 days.")
    
    else:
        st.success("Inventory levels are stable.")

    if warning_count>1200:
        st.info("Several medicines are approaching low stock condition.")

    st.divider()

    st.caption(
    """
    Smart Pharmacy Predictive Analysis System
    IEEE EMBS Internship Project 2026
        
    Developed using:
    Python | Pandas | Streamlit | Machine Learning
    """
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
        1,
        7,
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

        file_exists = os.path.exists(
            "outputs/prediction_history.csv"
        )
        history.to_csv(
            "outputs/prediction_history.csv",
            mode="a",
            header=not file_exists,
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

        csv = history_df.to_csv(
            index=False
        )

        st.download_button(
            " 📥 Download Prediction History",
            csv,
            "prediction_history.csv",
            "text/csv"
        )
    
    st.divider()
    st.caption("Smart Pharmacy Prediction Analytics System | IEEE EMBS Internship 2026")


# ========================================================================
#Inventory Monitoring


elif page == "Inventory Monitoring":

    st.header("Inventory Monitoring Module")

    if st.session_state.get(
        "record_added",
        False
    ):
        st.success("Inventory record added successfully.")

        st.session_state["record_added"]=False

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

            #st.toast("Inventory record added successfully.")

            st.session_state["record_added"]=True
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
    #trend_df=trend_df.tail(100) - for presentation

    #st.line_chart(
    #    trend_df.set_index("date")
    #)
    fig = px.line(
        trend_df,
        x="date",
        y="closing_stock",
        title="Inventory Stock Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    #Supplier Anaytics
    st.subheader(" 🏭 Supplier Distribution")

    supplier_counts=(
        inventory_df["supplier"]
        .value_counts()
    )

    #st.bar_chart(
    #   supplier_counts
    #)

    supplier_df = (
        supplier_counts
        .reset_index()
    )

    supplier_df.columns = [
        "Supplier",
        "Count"
    ]

    fig = px.bar(
        supplier_df,
        x="Supplier",
        y="Count",
        title="Supplier Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader(" ⚠️ Supplier Risk Analysis")

    supplier_risk=(
        inventory_df[inventory_df["Inventory_Status"]=="Critical"]
        .groupby("supplier")
        .size()
        .sort_values(ascending=False)   
    )

    if not supplier_risk.empty:
        risky_supplier=supplier_risk.index[0]
        risky_count=supplier_risk.iloc[0]
        st.error(f"Highest Critical Stock Dependency: {risky_supplier} ({risky_count} critical records)")

    
    #Top Medicien Analysis
    st.subheader(
        " 💊 Top Medicines by Inventory Records"
    )

    medicine_counts = (
        inventory_df["item"]
        .value_counts()
        .head(10)
    )

    #st.bar_chart(
    #   medicine_counts
    #)

    medicine_df=(
        medicine_counts
        .reset_index()
    )

    medicine_df.columns = [
        "Medicine",
        "Count"
    ]

    fig = px.bar(
        medicine_df,
        x="Medicine",
        y="Count",
        title="Top Medicines"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    #top critical medicines
    st.subheader(" 🚨 Lowest Stock Critical Medicines")

    critical_df=inventory_df[
            inventory_df["Inventory_Status"]=="Critical"
        ]
    
    top_critical=(
        critical_df.groupby("item")["closing_stock"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
    )
    if not top_critical.empty:
        st.bar_chart(top_critical)
        #st.dataframe(top_critical)
    else:
        st.info("No critical medicines found")

    #risk ranking
    st.subheader(" 🏥 Hospital Risk Ranking")

    risk_table=(
        inventory_df[
            inventory_df["Inventory_Status"]=="Critical"
        ]
        .groupby("location")
        .size()
        .reset_index(name="Critical_Count")
        .sort_values(
            "Critical_Count",
            ascending=False
        ) 
    )

    #st.dataframe(risk_table)

    #st.bar_chart(risk_table.set_index("location"))
    if len(risk_table)>=3:
        col1, col2, col3 =st.columns(3)

        with col1:
            st.error(f"🥇 Highest Risk \n\n{risk_table.iloc[0]['location']}\n\nCritical: {risk_table.iloc[0]['Critical_Count']}")
    
        with col2:
            st.warning(f"🥈 Second Risk\n\n{risk_table.iloc[1]['location']}\n\nCritical:{risk_table.iloc[1]['Critical_Count']}")

        with col3:
            st.info(f"🥉 Third Risk\n\n{risk_table.iloc[2]['location']}\n\nCritical: {risk_table.iloc[2]['Critical_Count']}")
    
        st.bar_chart(risk_table.set_index("location"))



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
    

    st.divider()
    st.caption("Smart Pharmacy Prediction Analytics System | IEEE EMBS Internship 2026")



    
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
                .mode()
                .iloc[0]
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

            avg_price = round(
                filtered_df["final_price"].mean(),
                2
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
                    "Average Price",
                    f"₹{avg_price}"
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
            
            #Product Intelligence analytics
            st.subheader(" 📊 Brand Analytics")
            col1,col2,col3=st.columns(3)

            with col1:
                st.metric(
                    "Average Price",
                    round(
                        filtered_df["price"].mean(),
                        2
                    )
                )
            
            with col2:
                st.metric(
                    "Average Reviews",
                    int(filtered_df["num_reviews"].mean())
                )

            with col3:
                st.metric(
                    "Manufacturers",
                    filtered_df["manufacturer"].nunique()
                )
            
            #PI Smart Insights
            st.subheader(" 🧠 Product Insights")

            if avg_rating >=4.0:
                st.success("High Customer Satisfaction detected.")
            
            elif avg_rating>=3.0:
                st.warning("Average Customer Satisfaction.")
            
            else:
                st.error("Poor Product ratings detected.")

            if avg_price>1000:
                st.info("Premium pricing category")

            else:
                st.info("Affordable pricing category.")



            if len(filtered_df)>0:


                st.dataframe(
                    filtered_df,
                    use_container_width=True
                )

                csv=filtered_df.to_csv(
                    index=False
                )

                st.download_button(
                    label=" 📥  Download Product Report",
                    data=csv,
                    file_name="product_report.csv",
                    mime="text/csv"
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

                st.subheader(
                    " 💰 Price Distribution"
                )

                price_fig = px.histogram(
                    filtered_df,
                    x="final_price",
                    nbins=20,
                    title="Medicine Price Distribution"
                )

                st.plotly_chart(
                    price_fig,
                    use_container_width=True
                )

        else:

            st.warning(
                "No medicine found. Please enter correct data"
            )

    st.divider()
    st.caption("Smart Pharmacy Prediction Analytics System | IEEE EMBS Internship 2026")        