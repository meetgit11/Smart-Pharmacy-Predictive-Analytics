#dashboard interface


import streamlit as st
import pandas as pd

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

    st.write("✅ Demand Forecasting")
    st.write("✅ Inventory Monitoring")
    st.write("✅ Product Intelligence")

#Demand Forecasting
elif page == "Demand Forecasting":

    st.header("Demand Forecasting Module")

    st.info(
        "Demand forecasting model integration coming next."
    )

#Inventory Monitoring
elif page == "Inventory Monitoring":

    st.header("Inventory Monitoring Module")

    inventory_df = pd.read_csv(
        "outputs/inventory_alerts.csv"
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

    medicine_name = st.text_input("Search Medicine")
    