# This is a sample JSON response for the word "hello"
# We use this as a "fixture" to test our parser functions
# without making real API calls.

HELLO_DATA = {
    "word": "hello",
    "phonetic": "həˈləʊ",
    "phonetics": [
        {
            "text": "həˈləʊ",
            "audio": "//ssl.gstatic.com/dictionary/static/sounds/20200429/hello--_gb_1.mp3"
        },
        {
            "text": "hɛˈləʊ"
        }
    ],
    "origin": "early 19th century: variant of earlier hollo ; related to holla.",
    "meanings": [
        {
            "partOfSpeech": "exclamation",
            "definitions": [
                {
                    "definition": "used as a greeting or to begin a phone conversation.",
                    "example": "hello there, Katie!",
                    "synonyms": [],
                    "antonyms": []
                }
            ]
        },
        {
            "partOfSpeech": "noun",
            "definitions": [
                {
                    "definition": "an utterance of 'hello'; a greeting.",
                    "example": "she was getting polite nods and hellos from people",
                    "synonyms": [],
                    "antonyms": []
                }
            ]
        },
        {
            "partOfSpeech": "verb",
            "definitions": [
                {
                    "definition": "say or shout 'hello'.",
                    "example": "I pressed the phone button and helloed",
                    "synonyms": [],
                    "antonyms": []
                }
            ]
        }
    ]
}

# Sample data for a word where some fields are missing
NO_ORIGIN_DATA = {
    "word": "test",
    "phonetic": "tɛst",
    "phonetics": [
        {
            "text": "tɛst",
            "audio": "" # Missing audio
        }
    ],
    "meanings": [
        {
            "partOfSpeech": "noun",
            "definitions": [
                {
                    "definition": "a procedure intended to establish the quality."
                }
            ]
        }
    ]
    # 'origin' key is missing
}