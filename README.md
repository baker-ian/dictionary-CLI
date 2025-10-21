# Dictionary CLI

A Python-based command-line tool that fetches word definitions, phonetics, and origins using the [Free Dictionary API](https://dictionaryapi.dev/).

This project was built for a university midterm, demonstrating AI-assisted development, testing, and CI/CD practices.

![Tests](https://github.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>/workflows/Tests/badge.svg)
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