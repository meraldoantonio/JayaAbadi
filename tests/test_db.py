def test_record_transaction(capfd):
    # Dummy test for record_transaction function.
    from app import db
    data = {"sample": "data"}
    db.record_transaction(data)
    # Here you could capture stdout and check that the print occurred.
