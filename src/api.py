import requests

BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def get_word_data(word):
    """
    Fetches data for a given word from the Dictionary API.
    
    Args:
        word (str): The word to look up.
        
    Returns:
        dict: The JSON data for the word if found.
        
    Raises:
        requests.exceptions.RequestException: For network-related errors.
        Exception: For 404 (word not found) or other HTTP errors.
    """
    url = f"{BASE_URL}{word}"
    
    try:
        response = requests.get(url)
        
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        
        # The API returns a list, we typically want the first item.
        return response.json()[0]
        
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            # Re-raise as a more specific, clear exception
            raise Exception(f"Word not found: '{word}'")
        else:
            raise Exception(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        # For other errors like no network connection
        raise Exception(f"A network error occurred: {req_err}")