import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app import ocr, business_logic, db, config

def main():
    st.title("JayaAbadi - Purchase Order Processor")
    
    # File uploader for PDF files
    uploaded_file = st.file_uploader("Upload PO PDF", type=["pdf"])
    
    if uploaded_file:
        st.write("File uploaded successfully!")
        # Optionally, save file to disk or S3 here.
        
        # Trigger OCR processing (dummy function for now)
        st.write("Processing file with OCR ...")
        # Here you would call your OCR function. For PoC, we simulate with dummy data.
        extracted_data = ocr.extract_text_from_pdf(uploaded_file)
        
        # Process data with business logic (dummy operation)
        processed_df = business_logic.process_extracted_data(extracted_data)
        
        # Show the extracted result as an editable pandas dataframe
        st.write("Editable DataFrame:")
        edited_df = st.experimental_data_editor(processed_df, num_rows="dynamic")
        
        # Optionally, you can save the edited dataframe or perform further actions
        st.write("Final DataFrame:", edited_df)
        
        # Example of a DB update (dummy call)
        db.record_transaction(edited_df)

if __name__ == "__main__":
    main()
