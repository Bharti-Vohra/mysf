import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase app
cred = credentials.Certificate("sfire.json")
if not firebase_admin._apps:
    default_app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://sfire-66399-default-rtdb.firebaseio.com/'})

# Get database reference
ref = db.reference('/employees')  

# Add Employee form
st.header("Add Employee")
emp_id = st.text_input("Employee_Id")
name = st.text_input("Name")
age = st.number_input("Age", min_value=0, max_value=120)
salary = st.number_input("Salary", min_value=0)

# Submit button
if st.button("Submit"):
    employee_data = {
        "name": name,
        "age": age,
        "salary": salary
    }
    ref.child(emp_id).set(employee_data)
    st.success("Employee data added to Firebase!")
