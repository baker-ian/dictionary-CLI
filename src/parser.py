import sys

def parse_definitions(data):
    """
    Parses the definitions from the API data.
    
    Args:
        data (dict): The JSON data for the word.
        
    Returns:
        str: A formatted string of definitions, or None if not found.
    """
    try:
        # 'meanings' is a list of dictionaries (e.g., "noun", "verb")
        meanings = data.get('meanings', [])
        if not meanings:
            return "No definitions found."
            
        output = []
        word = data.get('word', '')
        
        # Loop through each meaning block (noun, verb, etc.)
        for meaning in meanings:
            part_of_speech = meaning.get('partOfSpeech', 'unknown')
            output.append(f"\n--- {word} ({part_of_speech}) ---")
            
            # Loop through each definition for that part of speech
            definitions = meaning.get('definitions', [])
            for i, definition_obj in enumerate(definitions, 1):
                definition_text = definition_obj.get('definition', 'No definition text.')
                output.append(f"  {i}. {definition_text}")
                
        return "\n".join(output)
        
    except Exception as e:
        print(f"Error parsing definitions: {e}", file=sys.stderr)
        return None

def parse_phonetic(data):
    """
    Parses the phonetic spelling and audio from the API data.
    
    Args:
        data (dict): The JSON data for the word.
        
    Returns:
        str: A formatted string of phonetic info, or None if not found.
    """
    try:
        # 'phonetics' is a list
        phonetics = data.get('phonetics', [])
        if not phonetics:
            return "No phonetic information found."
            
        # Find the first phonetic entry that has both text and audio
        for phonetic_info in phonetics:
            text = phonetic_info.get('text')
            audio = phonetic_info.get('audio')
            
            if text and audio:
                # The API audio URLs sometimes start with //
                if audio.startswith("//"):
                    audio = "https:" + audio
                return f"Phonetic: {text}\nAudio: {audio}"
                
        # If none have both, just return the first text one
        if phonetics[0].get('text'):
            return f"Phonetic: {phonetics[0]['text']}"
            
        return "No phonetic information found."
        
    except Exception as e:
        print(f"Error parsing phonetics: {e}", file=sys.stderr)
        return None

def parse_origin(data):
    """
    Parses the word origin (etymology) from the API data.
    
    Args:
        data (dict): The JSON data for the word.
        
    Returns:
        str: A formatted string of the origin, or None if not found.
    """
    try:
        origin = data.get('origin')
        
        if origin:
            return f"Origin: {origin}"
        else:
            return "No origin information found."
            
    except Exception as e:
        print(f"Error parsing origin: {e}", file=sys.stderr)
        return None