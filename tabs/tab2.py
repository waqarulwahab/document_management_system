import streamlit as st
from report.Access_RC_Pay import Access_RC_Pay


def tab_2(filtered_record):
    
    col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
    with col1:
        Access_RC_Pay_Report = st.checkbox("Access_RC_Pay")
    with col2:
        Blank_Bah_Addendum_PDF = st.checkbox("BLANK_BAH_ADDENDUM.pdf", disabled=True)
    with col3:
        n_426_PDF = st.checkbox("N-426", disabled=True)
    with col4:
        Male_5500_PDF = st.checkbox("5500_MALE", disabled=True)
    with col5:
        Female_5501_PDF = st.checkbox("5501_FEMALE", disabled=True)


    Access_RC_Pay_output = None  # Initialize the variable for storing the PDF output

    # Handle the selected checkboxes
    if Access_RC_Pay_Report:
        Access_RC_Pay_output = Access_RC_Pay(filtered_record)
    if Blank_Bah_Addendum_PDF:
        pass  # Add logic here for handling Blank_Bah_Addendum_PDF if needed
    if n_426_PDF:
        pass
    if Male_5500_PDF:
        pass
    if Female_5501_PDF:
        pass

    # Only show the export section if any checkbox is selected
    if Access_RC_Pay_Report or Blank_Bah_Addendum_PDF or n_426_PDF or Male_5500_PDF or Female_5501_PDF:
        if st.button("Export PDF"):
            if Access_RC_Pay_output:
                # Provide the user with a download link for the populated PDF
                st.download_button(
                    label="Download Populated PDF",
                    data=Access_RC_Pay_output.getvalue(),
                    file_name="Access_RC_Pay_Populated.pdf",
                    mime="application/pdf"
                )
