import streamlit as st
import pandas as pd
from helper_functions.filter import filter_record
from helper_functions.input_fields import inputs
from tabs.tab2 import tab_2

st.set_page_config(layout="wide", page_title="Document Management App", page_icon="📄")

# Add a header with some styling
st.markdown(
    """
    <style>
    .main-header {
        font-size: 32px;
        font-weight: bold;
        color: #4A90E2;
        text-align: center;
        margin-bottom: 20px;
    }
    .sub-header {
        font-size: 20px;
        font-weight: bold;
        color: #333333;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown('<div class="main-header">Document Management Application 📄</div>', unsafe_allow_html=True)

# Load the Excel file
file_name = "records.xlsx"  # Replace with your actual file name
df = pd.read_excel(file_name)

# Tabs
tab1, tab2 = st.tabs(["📋 Display Data", "📤 Export Documents"])

# Tab 1: Display Data
with tab1:
    st.markdown('<div class="sub-header">Input New Records</div>', unsafe_allow_html=True)
    st.write("Add new records to the dataset below. Fill in the required details and submit.")
    
    # Create two columns for input fields
    col1, col2 = st.columns(2)
    with col1:
        st.info("📝 Fill in the required details in the input fields.")
    with col2:
        st.success("📌 Ensure data integrity when adding records.")
    
    # Input fields function
    inputs(file_name)

# Tab 2: Export Documents
with tab2:
    st.markdown('<div class="sub-header">Filter Records and Export Documents</div>', unsafe_allow_html=True)
    st.write("Use the filtering options to select records and export them as documents.")

    # Filter records with a styled message
    st.info("🔍 Filter records by specific criteria.")
    filtered_record, selected_value = filter_record(df)
    
    if not filtered_record.empty:
        st.success(f"✅ Filtered records based on your selection: **{selected_value}**")
        st.dataframe(filtered_record)
        
        # Allow exporting the filtered row
        csv_filtered_row = filtered_record.to_csv(index=False)
        
        # Call tab_2 for additional options
        tab_2(filtered_record)
    else:
        st.warning("⚠️ No records found based on your filter criteria. Please try again.")
