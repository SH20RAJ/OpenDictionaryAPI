import os
import requests
import time
import json
from tqdm import tqdm

# Paths
wordlist_file = 'assets/wordlist/english.txt'
output_folder = 'data/english'
error_log = 'error_log.txt'

# Ensure output directory exists
os.makedirs(output_folder, exist_ok=True)

def fetch_word_data(word):
    """Fetch data from the dictionary API for a given word."""
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None  # No data for this word
        else:
            print(f"Failed to fetch '{word}': {response.status_code}")
            return {}
    except requests.RequestException as e:
        print(f"Error fetching '{word}': {e}")
        return {}

def save_json(word, data):
    """Save the JSON data to a file."""
    filepath = os.path.join(output_folder, f"{word}.json")
    with open(filepath, 'w') as f:
        f.write(json.dumps(data, indent=4))

def is_valid_word(word):
    """Check if the word is valid (no special characters or spaces)."""
    return word.isalpha()

def log_error(word):
    """Log failed words to an error file."""
    with open(error_log, 'a') as f:
        f.write(f"{word}\n")

def main():
    # Read words from the wordlist file
    with open(wordlist_file, 'r') as f:
        words = [line.strip() for line in f if line.strip()]
    
    # Progress tracking
    print(f"Total words to process: {len(words)}")
    for word in tqdm(words, desc="Processing words"):
        json_path = os.path.join(output_folder, f"{word}.json")
        if os.path.exists(json_path):
            continue  # Skip already downloaded words
        
        if not is_valid_word(word):
            print(f"Skipping invalid word: {word}")
            log_error(word)
            continue
        
        data = fetch_word_data(word)
        if data is None:
            log_error(word)  # Log words with no data
            continue
        elif data == {}:
            log_error(word)  # Log failed fetch attempts
            continue
        
        save_json(word, data)
        time.sleep(1)  # Delay between requests to avoid hitting rate limits

    print("\nProcess completed.")

if __name__ == '__main__':
    main()
