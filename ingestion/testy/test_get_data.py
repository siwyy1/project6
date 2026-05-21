from ingestion.get_data import *
def test_fetch():
    data = fetch()
    assert isinstance(data, list)

