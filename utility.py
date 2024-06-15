import os
import glob

ROOT = os.path.dirname(os.path.abspath(__file__))
def process_text(text):
    import re

    processed_text = text.lower()
    # cleaning up line breaks and tabs
    processed_text = re.compile('[\n\t]').sub(' ', processed_text)
    # removing all the symbols
    processed_text = re.compile('[^0-9a-z ]').sub('', processed_text)

    return processed_text

def create_word_index():
    import json
    word_index = {}

    for file_path in glob.glob(f'{ROOT}/data/*.txt'):
        with open(file_path, 'r') as file:
            # clean up the text
            processed_text = process_text(file.read()).split(' ')
            print(processed_text)
            for token in processed_text:
                occurrences = processed_text.count(token)
                if token in word_index:
                    word_index[token].update({file_path.split('/')[-1]: occurrences})
                else:
                    word_index[token] = {file_path.split('/')[-1]: occurrences}
    with open(f'{ROOT}/indexes/word_index.json', 'w') as f:
        json.dump(word_index, f)

    return word_index

def sorted_dictionary(dictionary):
    sort_results = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

    return sort_results
