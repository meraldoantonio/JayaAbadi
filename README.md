# JayaAbadi

JayaAbadi is a proof-of-concept (PoC) application designed to process purchase order (PO) PDF files. The app leverages AWS Textract for OCR to extract data from uploaded PDFs and uses Amazon DynamoDB to store and update product transaction records and stock levels. A Python-based Streamlit front end provides a user-friendly interface, including the ability to display the OCR-extracted results as an editable pandas DataFrame.

## Features

- **PO PDF Upload:** Easily upload purchase order PDF files.
- **OCR Processing:** Uses AWS Textract to extract tables and figures from PDFs.
- **Business Logic:** Translates external product codes to internal ones, records transactions, updates stock levels, and tracks product IDs.
- **Editable Data Display:** Displays OCR-extracted data as an editable pandas DataFrame for easy review and correction.
- **Serverless & Cost-Effective:** Leverages AWS managed services like S3, Textract, and DynamoDB to minimize operational overhead and cost.
- **Organized Codebase:** Utilizes a modular folder structure and Poetry for dependency management.

## Technology Stack

- **Front End:** [Streamlit](https://streamlit.io/)
- **Backend Processing:** Python, AWS Textract (OCR)
- **Database:** [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- **File Storage:** [Amazon S3](https://aws.amazon.com/s3/)
- **Dependency Management:** [Poetry](https://python-poetry.org/)

## Folder Structure

```plaintext
JayaAbadi/
├── app/
│   ├── __init__.py
│   ├── main.py              # Streamlit entry point
│   ├── config.py            # Configuration settings (AWS credentials, table names, etc.)
│   ├── ocr.py               # Functions for AWS Textract integration
│   ├── business_logic.py    # Functions for processing OCR data and business logic
│   ├── db.py                # DynamoDB interactions (CRUD operations)
│   └── utils.py             # Helper functions and utilities
├── static/
│   ├── images/              # Folder for storing sample images
│   │   └── sample.png       # Example image file
│   └── logo.png             # Additional static assets
├── tests/
│   ├── __init__.py
│   ├── test_business_logic.py
│   ├── test_db.py
│   └── test_ocr.py
├── pyproject.toml           # Poetry project configuration
├── README.md                # Project overview and documentation
└── .gitignore               # Git ignore file
