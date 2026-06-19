#login system

import streamlit as st

#st.image(
#    "https://img.icons8.com/color/240/pill.png",
#    width=150
#)

def login():
    #st.title(" 🔐 Smart Pharmacy Login")

    st.markdown("""
    <h1 style ='text-align:center;'>
     💊 Smart Pharmacy Predictive Analytics
    </h1>
    """,
    unsafe_allow_html=True)

    st.markdown("""
    <h3 style='text-align:center; color:gray;'>
    Secure Healthcare Inventory Platform
    </h3>
    """,
    unsafe_allow_html=True)

    st.divider()

    #username =st.text_input("Username")
    #password = st.text_input(
    #    "Password",
    #    type="password"
    #)
 
    col1, col2, col3 = st.columns([1,2,1])
    with col2:

        st.subheader(" 🔐 User Login")
        username = st.text_input("Username")
        password=st.text_input("Password",
                               type="password"
        )

        users={
            "admin":{
                "password":"admin123",
                "role":"Admin"
            },
            "manager":{
                "password":"manager123",
                "role":"Manager"
            },
            "pharmacist":{
                "password":"pharma123",
                "role":"Pharmacist"
            }
        }

        if st.button(
            "Login",
            use_container_width=True):

            #if(username == "admin" and password == "admin123"):
            #    st.session_state["logged_in"]=True
            #    st.rerun()


            if username in users: 
                if password == users[username]["password"]:
                    st.session_state["logged_in"]=True
                    st.session_state["role"]=(users[username]["role"])

                    st.rerun()
                else:
                    st.error("Invalid Password")
        
            else:
                st.error("Invalid Username")

    st.divider()

    st.caption("IEEE EMBS Internship Project 2026")


