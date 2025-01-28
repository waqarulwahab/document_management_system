import streamlit as st
import pdfrw
import re
from io import BytesIO


template_pdf = "report/Access_RC_Pay.pdf"

def sanitize_field_name(field_name):
    """Sanitize field names by removing unwanted characters and spaces"""
    # Remove any special characters (e.g. parentheses) and spaces, and normalize the case
    field_name = re.sub(r'\(.*\)', '', field_name)  # Remove text inside parentheses
    field_name = field_name.strip().replace(' ', '').lower()  # Remove spaces and normalize to lowercase
    return field_name

def populate_pdf_with_data(input_pdf, data):
    # Read the input PDF
    template_pdf = pdfrw.PdfReader(input_pdf)
    
    # Fill form fields with data
    for page in template_pdf.pages:
        annotations = page['/Annots']
        if annotations:
            for annotation in annotations:
                # Get the field name
                field_name = annotation['/T'][1:-1]  # Get field name (remove quotes)
                
                # Debugging: Print the original, unprocessed field names
                print(f"Original field name: {field_name}")  # Show the exact field name
                
                # Sanitize the field name
                sanitized_field_name = sanitize_field_name(field_name)
                
                # Loop through the dictionary and check for partial matches
                for key, value in data.items():
                    sanitized_key = sanitize_field_name(key)
                    
                    # Check if sanitized key is part of the sanitized field name
                    if sanitized_key in sanitized_field_name:
                        print(f"Match found: {sanitized_field_name} -> {sanitized_key}")  # Debug match
                        annotation.update(pdfrw.PdfDict(V=f'{value}'))  # Update field with data
                        break

    # Create an in-memory output PDF
    output_pdf = BytesIO()
    pdfrw.PdfWriter().write(output_pdf, template_pdf)
    
    return output_pdf



def Access_RC_Pay(filtered_record):
    name   = filtered_record['NAME (UMR)'].iloc[0]  # Extract just the value
    gender = filtered_record['M/F'].iloc[0]
    uic    = filtered_record['UIC'].iloc[0]
    ssn    = filtered_record['SSN'].iloc[0]

    add_data = {
        "Name": name,
        "SSN": ssn,
        # "DOB": "01/01/1990",
        "UIC": uic,
        # "State of Residency": "NY",
        # "Pay Entry Base Date": "01/01/2020",
        # "Pay Grade": "E5",
        # "Date of entry to NYARNG": "01/01/2015",
        "Gender":  gender,
        # "Dependency Status and Type": "Single",
        # "SGLI Option": "Option A",
        # "Federal Income Tax Withholding(FITW)": "Yes",
        # "Marital Status": "Single",
        # "# of FITW Exemptions": "0",
        # "ETF": "No",
        # "Checking Account Number": "987654321",
        # "Routing Number": "123456789",
        # "SM Signatur": "John Doe Signature"
    }

    Access_RC_Pay = populate_pdf_with_data(template_pdf, add_data)
    return Access_RC_Pay

