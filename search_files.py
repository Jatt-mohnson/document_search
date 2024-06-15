import glob
from utility import ROOT, process_text, sorted_dictionary

def simple_string_match(phrase):
    occurences = {}
    count = 0
    for file_path in glob.glob(f'{ROOT}/data/*.txt'):
        with open(file_path, 'r') as file:
            processed_text = process_text(file.read()).split(' ')
            if phrase in processed_text:
                count = processed_text.count(phrase)

            occurences.update({file_path.split('/')[-1]: count})

    return occurences
def regex_match(phrase):
    import re
    occurences = {}
    for file_path in glob.glob(f'{ROOT}/data/*.txt'):
        with open(file_path, 'r') as file:
            #clean up the text
            processed_text = process_text(file.read())

            matches = re.findall(f'\\b{phrase}\\b', processed_text)
            count = len(matches)
            occurences.update({file_path.split('/')[-1]: count})

    return occurences

def search_index(phrase):
    import json
    with open(f'{ROOT}/indexes/word_index.json', 'r') as f:
        word_index = json.load(f)
    occurences = word_index.get(phrase, {'No Results': 0})
    return occurences

if __name__ == "__main__":
    import time
    search_function_dict = {
        '1': simple_string_match,
        '2': regex_match,
        '3': search_index
    }

    search_term = 'x x'
    while len(search_term.split(' ')) > 1:
        search_term = input('Enter the search term: ')
        if len(search_term.split(' ')) > 1:
            print('Please limit your search to a single word')
    search_term = process_text(search_term)

    search_method = ''
    while search_method not in ['1', '2', '3']:
        search_method = input('1) String Match 2) Regular Expression 3) Indexed\nChoose method: ')
        if search_method not in ['1', '2', '3']:
            print('invalid search method, please select from below choices\n')

    start_time = time.time()
    phrase_counts = search_function_dict.get(search_method, 'invalid choice')(search_term)

    print('Search Results: ')

    for file, count in sorted_dictionary(phrase_counts).items():
        print(f'\t{file} - {count} matches')

    print(f'Elapsed time: {(time.time() - start_time)*1000:.2f} ms')
