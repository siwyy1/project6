from ingestion.get_data import *
from unittest.mock import patch, Mock
import json

@patch("ingestion.get_data.requests.get")
def test_fetch(mock_get):

    fake_data = [
        {"name": "repo1"},
        {"name": "repo2"}
    ]

    mock_response = Mock()
    mock_response.json.return_value = fake_data

    mock_get.return_value = mock_response

    data = fetch()

    assert isinstance(data, list)
    assert data == fake_data