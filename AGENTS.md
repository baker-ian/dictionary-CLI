# Project: Dictionary CLI

## Overview
This project is a Python-based command-line interface (CLI) tool for the Midterm Project. It allows users to get definitions, phonetic information, and word origins from the command line. It is built with `argparse` for the CLI, `requests` for API interaction, and `pytest` for testing.

## API Integration
- **API:** Free Dictionary API
- **Docs URL:** https://dictionaryapi.dev/
- **Base URL:** `https://api.dictionaryapi.dev/api/v2/entries/en/<word>`
- **Auth:** No authentication or API key is required.
- **Data Format:** The API returns a JSON list. We will typically work with the first element of that list (index `[0]`).

## CLI Commands (3+ required)
The CLI will be structured using `argparse` subcommands:

1.  **`define <word>`**
    * **Action:** Fetches the definitions for the given `<word>`.
    * **Output:** Will display the part of speech followed by its definitions, looping through all available parts of speech (e.g., "noun", "verb").
    * **Example:** `python -m src.main define hello`

2.  **`phonetic <word>`**
    * **Action:** Fetches the primary phonetic spelling and audio link for the `<word>`.
    * **Output:** Will display the phonetic text (e.g., "həˈləʊ") and the URL for the audio file.
    * **Example:** `python -m src.main phonetic hello`

3.  **`origin <word>`**
    * **Action:** Fetches the word's origin (etymology).
    * **Output:** Will display the origin string, if one exists in the API response.
    * **Example:** `python -m src.main origin hello`

## Technical Stack
- **Language:** Python 3.10+
- **CLI:** `argparse` (from the standard library)
- **API Calls:** `requests` library
- **Testing:** `pytest` library, using `unittest.mock.patch` for mocking API calls.
- **CI/CD:** GitHub Actions

## Code Organization
The project will follow a `src` layout:

- **`src/main.py`**: The main entry point. Responsible for:
    - Setting up `argparse` (parser and subparsers).
    - Parsing user arguments.
    - Calling `api.py` to get data.
    - Calling `parser.py` to process the data.
    - Printing the final, formatted output to the console.

- **`src/api.py`**: Handles all network-related tasks.
    - Will contain a function `get_word_data(word)`.
    - This function uses `requests.get()` to call the API.
    - It will perform error handling (e.g., 404 "Word not found", 500 server errors, network errors) and return the JSON response.

- **`src/parser.py`**: Handles all data processing logic.
    - Will contain functions like `parse_definitions(json_data)`, `parse_phonetic(json_data)`, and `parse_origin(json_data)`.
    - These functions take the raw JSON from `api.py` and extract/format the specific information needed by `main.py`. This keeps the `main.py` file clean and simple.

- **`tests/`**: Contains all tests.
    - **`test_api.py`**: Tests the `api.py` module. Will use `pytest` and `unittest.mock` to patch `requests.get` and simulate API responses (both success and failure).
    - **`test_parser.py`**: Tests the `parser.py` module. Will use static, saved JSON examples to ensure the parsing functions correctly extract the data.

## Standards & Practices
- All code will follow PEP 8 style guidelines.
- All functions and classes will have docstrings.
- All API calls in tests *must* be mocked. No real network requests will be made during testing.
- The CLI will gracefully handle errors (e.g., if a word is not found, it will print "Word not found: '...'." instead of crashing).