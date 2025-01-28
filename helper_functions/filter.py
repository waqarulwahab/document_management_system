import streamlit as st

def filter_record(df):

    col1, col2, col3, col4 = st.columns([1,1,1,1])

    with col1:
        identifier_column = st.selectbox(
            "Select a column to use as the identifier:",
            options=df.columns,
            help="Choose the column to filter rows dynamically."
        )
    with col2:
        unique_values = df[identifier_column].unique()
        
        selected_value = st.selectbox(
            "Select a value:",
            options=unique_values,
            help=f"Choose a specific value from the '{identifier_column}' column to filter rows."
        )
    with col3:
        pass
    with col4:
        pass
    filtered_row = df[df[identifier_column] == selected_value]
    return filtered_row, selected_value

