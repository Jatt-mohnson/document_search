import glob
from config import env_paths

def process_text(text):
    import re

    processed_text = text.lower()
    # cleaning up line breaks and tabs
    processed_text = re.compile('[\n\t]').sub(' ', processed_text)
    # removing all the symbols
    processed_text = re.compile('[^0-9a-z ]').sub('', processed_text)

    return processed_text

def create_word_index(env='dev'):
    import json
    word_index = {}

    for file_path in glob.glob(env_paths[env]['files']):
        with open(file_path, 'r') as file:

            processed_text = process_text(file.read()).split(' ')
            for token in processed_text:
                occurrences = processed_text.count(token)
                if token in word_index:
                    word_index[token].update({file_path.split('/')[-1]: occurrences})
                else:
                    word_index[token] = {file_path.split('/')[-1]: occurrences}
    with open(env_paths[env]['index']+'/word_index.json', 'w') as f:
        json.dump(word_index, f)

    return word_index

def sorted_dictionary(dictionary):
    sort_results = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

    return sort_results
