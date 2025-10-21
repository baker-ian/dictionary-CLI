# Dictionary CLI

A Python-based command-line tool that fetches word definitions, phonetics, and origins using the [Free Dictionary API](https://dictionaryapi.dev/).

This project was built for a university midterm, demonstrating AI-assisted development, testing, and CI/CD practices.

![Tests](https://github.com/baker-ian/dictionary-CLI/workflows/Tests/badge.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 🌟 Features
* **Definitions:** Get a full list of definitions, grouped by part of speech.
* **Phonetics:** Find the phonetic spelling and a URL for audio pronunciation.
* **Etymology:** Look up a word's origin.
* **Error Handling:** Gracefully handles words that aren't found and network errors.

## ⚙️ Installation

To run this tool locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)baker-ian/dictionary-CLI.git
    cd <YOUR_REPO_NAME>
    ```

2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    
    # On Windows
    py -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

All commands are run from the project's root directory using the `python -m src.main` command.

### Get a Definition
```bash
python -m src.main define <word>
```
**Example**:
```bash
$ python -m src.main define hello

--- hello (exclamation) ---
  1. used as a greeting or to begin a phone conversation.

--- hello (noun) ---
  1. an utterance of 'hello'; a greeting.

--- hello (verb) ---
  1. say or shout 'hello'.
```

### Get Phonetics
```bash
python -m src.main phonetic <word>
```
**Example**
```bash
$ python -m src.main phonetic hello
Phonetic: həˈləʊ
Audio: [https://ssl.gstatic.com/dictionary/static/sounds/20200429/hello--_gb_1.mp3](https://ssl.gstatic.com/dictionary/static/sounds/20200429/hello--_gb_1.mp3)
```

### Get Word Origin
```bash
python -m src.main origin <word>
```
**Example**
```bash
$ python -m src.main origin hello
Origin: early 19th century: variant of earlier hollo ; related to holla.
```

### Error: Word Not Found
```bash
$ python -m src.main define asdfasdf
Error: Word not found: 'asdfasdf'
```

## 🧪 Testing
This project uses pytest and unittest.mock to ensure reliability. The test suite includes full mocking for all API calls, meaning it runs without needing an internet connection.

To run the tests locally:

1. Make sure you've installed dependencies (pip install -r requirements.txt).

2. Run pytest from the root directory:
```bash
pytest
```

## 🛠️ Technologies & API

* Python 3.10+
* argparse: For building the command-line interface.
* requests: For making API calls.
* pytest: For unit testing.
* unittest.mock: For mocking API responses during tests.
* GitHub Actions: For Continuous Integration (CI/CD).

### API
This tool is powered by the Free Dictionary API and does not require an API key.