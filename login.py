import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("logins.json")
if not firebase_admin._apps:
    default_app = firebase_admin.initialize_app(cred,{'databaseURL':'https://login-42d5f-default-rtdb.firebaseio.com/'})
users_ref = db.reference('/')
st.header("Login")
mail_Id = st.text_input("Enter email_id")
password = st.text_input("Enter your Password")
if st.button("Submit"):
    user_data = users_ref.get()
    if user_data is None:
        st.error("Error: could not retrieve user data from database")
    else:
        for user_id, user in user_data.items():
            if user['mail_Id'] == 'python@gmail.com' and user["password"] == password:
                st.success("Login successful!")
                employee_data = {"Mail": mail_Id,"Password": password}
                users_ref.child(user_id).update(employee_data)
                break
        else:
            st.error("Invalid email or password")
else:
    st.warning("Enter your credentials and click 'Submit'")
