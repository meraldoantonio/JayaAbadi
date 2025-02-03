def test_process_extracted_data():
    # Dummy test for process_extracted_data function.
    from app import business_logic
    import pandas as pd

    df = pd.DataFrame({"A": [1,2,3]})
    processed_df = business_logic.process_extracted_data(df)
    assert "Processed" in processed_df.columns
