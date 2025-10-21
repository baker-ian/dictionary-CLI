import pytest
from src import parser
from tests.sample_data import HELLO_DATA, NO_ORIGIN_DATA

def test_parse_definitions():
    """
    Tests that the definition parser correctly formats the output.
    """
    output = parser.parse_definitions(HELLO_DATA)
    
    # Check for key elements
    assert "--- hello (exclamation) ---" in output
    assert "1. used as a greeting or to begin a phone conversation." in output
    assert "--- hello (noun) ---" in output
    assert "1. an utterance of 'hello'; a greeting." in output
    assert "--- hello (verb) ---" in output
    assert "1. say or shout 'hello'." in output

def test_parse_phonetic():
    """
    Tests that the phonetic parser finds the text and audio.
    """
    output = parser.parse_phonetic(HELLO_DATA)
    
    assert "Phonetic: həˈləʊ" in output
    assert "Audio: https://ssl.gstatic.com/dictionary/static/sounds/20200429/hello--_gb_1.mp3" in output

def test_parse_origin():
    """
    Tests that the origin parser finds the origin string.
    """
    output = parser.parse_origin(HELLO_DATA)
    
    assert "Origin: early 19th century:" in output

def test_parse_origin_not_found():
    """
    Tests that the origin parser handles missing data gracefully.
    """
    output = parser.parse_origin(NO_ORIGIN_DATA)
    
    assert output == "No origin information found."

def test_parse_phonetic_missing_audio():
    """
    Tests that the phonetic parser can handle a missing audio URL.
    """
    output = parser.parse_phonetic(NO_ORIGIN_DATA)
    
    # It should fall back to just providing the text
    assert output == "Phonetic: tɛst"