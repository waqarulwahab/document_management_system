import streamlit as st
import pandas as pd
from helper_functions.load_data import load_data

def inputs(file_name):
    # Use a form to group input fields and submit button
    with st.form("input_form"):

        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            address = st.text_input("Address")
        with col2:    
            email = st.text_input("Email")
        with col3:    
            phone = st.text_input("Phone #")
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            age = st.number_input("Age", min_value=0, step=1)
        with col2:
            emp_id = st.text_input("EMP ID")
        with col3:
            dod_id = st.text_input("DOD ID")
        

        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            gender = st.selectbox("Gender (M/F)", ["M", "F"])
        with col2:
            ssn = st.text_input("SSN")
        with col3:
            name = st.text_input("Name (UMR)")

        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            mos  = st.text_input("MOS")
        with col2:
            phase = st.text_input("Phase")
        with col3:
            rsid = st.text_input("RSID")
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            enlistment = st.date_input("Enlistment Date")
        with col2:
            ship  = st.date_input("Ship Date")
        with col3:
            return_date = st.date_input("Return Date")
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            uic = st.text_input("UIC")
        with col2:
            state = st.text_input("State of Residency")
        with col3:
            opat = st.text_input("OPAT")
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            opat_lv = st.text_input("OPAT Level")
        with col2:
            height = st.number_input("Height", step=0.1)
        with col3:
            max_wt = st.number_input("Max Weight", step=0.1)
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            finserve = st.text_input("FINSERVE")
        with col2:
            marital_status  = st.selectbox("Marital Status (M/S)", ["M", "S"])
        with col3:
            dep  = st.text_input("DEP")
        
        col1, col2 = st.columns([1,1])
        with col1:
            flu_shot = st.text_input("Flu Shot")
        with col2:
            rank = st.text_input("Rank")

        col1, col2 = st.columns([1,8])
        # Submit button
        with col1:
            submitted = st.form_submit_button("Add Record")
        with col2:
            display_record = st.form_submit_button("Display Record")

    if submitted:
        new_record = pd.DataFrame([{
            "ADDRESS": address, "EMAIL": email, "PHONE #": phone, "AGE": age, "EMP ID": emp_id, "DOD ID": dod_id,
            "M/F": gender, "SSN": ssn, "NAME (UMR)": name, "RANK": rank, "MOS": mos, "PHASE": phase,
            "RSID": rsid, "ENLISTMENT": str(enlistment), "SHIP": str(ship), "RETURN": str(return_date),
            "UIC": uic, "STATE": state, "OPAT": opat, "OPAT LV": opat_lv, "HEIGHT": height, "MAX WT": max_wt,
            "FINSERVE": finserve, "M/S": marital_status, "DEP": dep, "FLU SHOT": flu_shot
        }])

        # Load existing data, append the new record, and save back to file
        data = pd.concat([load_data(file_name), new_record], ignore_index=True)
        data.to_excel(file_name, index=False, engine="openpyxl")
        st.success("✅ Record added successfully!")

    if display_record:
        data = pd.read_excel(file_name)
        st.dataframe(data)
