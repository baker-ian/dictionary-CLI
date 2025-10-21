import pytest
import requests
from unittest.mock import patch, MagicMock
from src import api
from tests.sample_data import HELLO_DATA

# This is the "path" to the 'requests' library *as it is used inside the api.py file*.
# This is a common point of confusion. We patch it where it's *used*, not where it's defined.
PATCH_PATH = "src.api.requests.get"

@patch(PATCH_PATH)
def test_get_word_data_success(mock_get):
    """
    Tests a successful API call.
    """
    # Create a mock response object
    mock_response = MagicMock()
    mock_response.status_code = 200
    # The API returns a list, so we return our data inside a list
    mock_response.json.return_value = [HELLO_DATA]
    
    # Configure the mock 'requests.get' to return our mock response
    mock_get.return_value = mock_response
    
    # Call the function
    data = api.get_word_data("hello")
    
    # Check that requests.get was called correctly
    mock_get.assert_called_with("https://api.dictionaryapi.dev/api/v2/entries/en/hello")
    # Check that our function returned the first item from the list
    assert data == HELLO_DATA

@patch(PATCH_PATH)
def test_get_word_data_not_found(mock_get):
    """
    Tests a 404 Not Found error.
    """
    # Create a mock response object that will simulate a 404
    mock_response = MagicMock()
    mock_response.status_code = 404
    # Configure the mock to raise an HTTPError when .raise_for_status() is called
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "404 Client Error: Not Found"
    )
    
    mock_get.return_value = mock_response
    
    # Use pytest.raises to check that our function correctly raises an Exception
    with pytest.raises(Exception, match="Word not found: 'asdf'"):
        api.get_word_data("asdf")
        
    # Check that requests.get was still called
    mock_get.assert_called_with("https://api.dictionaryapi.dev/api/v2/entries/en/asdf")

@patch(PATCH_PATH)
def test_get_word_data_server_error(mock_get):
    """
    Tests a 500 Internal Server Error.
    """
    # Create a mock response object that will simulate a 500
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "500 Server Error: Internal Server Error"
    )
    
    mock_get.return_value = mock_response
    
    # Check that our function raises a generic HTTP error
    with pytest.raises(Exception, match="HTTP error occurred"):
        api.get_word_data("serverfail")

@patch(PATCH_PATH)
def test_get_word_data_network_error(mock_get):
    """
    Tests a network-level error (e.g., no internet connection).
    """
    # Configure the mock to raise a RequestException (base class for network errors)
    mock_get.side_effect = requests.exceptions.RequestException("Connection timed out")
    
    with pytest.raises(Exception, match="A network error occurred"):
        api.get_word_data("networkfail")