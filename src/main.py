import argparse
import sys
from src import api, parser

def main():
    """
    Main entry point for the CLI application.
    """
    # Main parser setup
    cli_parser = argparse.ArgumentParser(
        description="A command-line dictionary tool."
    )
    
    # We use subparsers to handle the different commands (define, phonetic, origin)
    subparsers = cli_parser.add_subparsers(dest='command', required=True,
                                           help="The command to execute.")
    
    # --- 'define' command ---
    define_parser = subparsers.add_parser(
        'define', help="Get the definition(s) of a word."
    )
    define_parser.add_argument('word', type=str, help="The word to define.")
    
    # --- 'phonetic' command ---
    phonetic_parser = subparsers.add_parser(
        'phonetic', help="Get the phonetic spelling and audio for a word."
    )
    phonetic_parser.add_argument('word', type=str, help="The word to look up.")

    # --- 'origin' command ---
    origin_parser = subparsers.add_parser(
        'origin', help="Get the origin (etymology) of a word."
    )
    origin_parser.add_argument('word', type=str, help="The word to look up.")
    
    
    # Parse the arguments from the command line
    args = cli_parser.parse_args()
    
    try:
        # 1. Call the API to get data
        word_data = api.get_word_data(args.word)
        
        output = None
        # 2. Call the correct parser based on the command
        if args.command == 'define':
            output = parser.parse_definitions(word_data)
        elif args.command == 'phonetic':
            output = parser.parse_phonetic(word_data)
        elif args.command == 'origin':
            output = parser.parse_origin(word_data)
            
        # 3. Print the formatted output
        if output:
            print(output)
        else:
            # This handles cases where the parser itself failed
            print(f"Could not retrieve '{args.command}' for '{args.word}'.", file=sys.stderr)

    except Exception as e:
        # Handle errors gracefully (e.g., word not found from api.py)
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()