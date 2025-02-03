import io
import pandas as pd
# In a real implementation, you would import boto3 and use AWS Textract

def extract_text_from_pdf(file_obj):
    """
    Dummy function to simulate OCR extraction.
    Replace this with actual calls to AWS Textract.
    """
    # For demonstration, we create a dummy pandas DataFrame.
    data = {
        "Column1": ["Value1", "Value2", "Value3"],
        "Column2": [10, 20, 30]
    }
    df = pd.DataFrame(data)
    return df
