import sys, glob
# adding the directory to the path
sys.path.append('../')
from src.utility import process_text, sorted_dictionary
from config import env_paths


def simple_string_match(phrase, env='dev'):
    file_count = {}

    for file_path in glob.glob(env_paths[env]['files']):
        with open(file_path, 'r') as file:
            processed_text = process_text(file.read()).split(' ')
            if phrase in processed_text:
                count = processed_text.count(phrase)
            else:
                count = 0
            file_count.update({file_path.split('/')[-1]: count})

    return file_count

def regex_match(phrase, env='dev'):
    import re
    file_count = {}
    for file_path in glob.glob(env_paths[env]['files']):
        with open(file_path, 'r') as file:
            #clean up the text
            processed_text = process_text(file.read())

            matches = re.findall(f'\\b{phrase}\\b', processed_text)
            count = len(matches)
            file_count.update({file_path.split('/')[-1]: count})

    return file_count

def search_index(phrase, env='dev'):
    import json
    with open(env_paths[env]['index']+'/word_index.json', 'r') as f:
        word_index = json.load(f)
    file_count = word_index.get(phrase, {})

    file_list = glob.glob(env_paths[env]['files'])
    # add in files with 0 references
    # This is faster than bogging down the actual index with files with 0 counts
    [file_count.update({f.split('/')[-1]: 0}) for f in file_list if f.split('/')[-1] not in list(file_count.keys())]

    return file_count

if __name__ == "__main__":
    import time
    search_function_dict = {
        '1': simple_string_match,
        '2': regex_match,
        '3': search_index
    }

    search_term = 'x x'
    while len(search_term.split(' ')) > 1:
        search_term = input('Enter the search term: ').strip(' ')
        if len(search_term.split(' ')) > 1:
            print('Please limit your search to a single word')
    search_term = process_text(search_term)

    search_method = ''
    while search_method not in ['1', '2', '3']:
        search_method = input('1) String Match 2) Regular Expression 3) Indexed\nChoose method: ').strip(' ')
        if search_method not in ['1', '2', '3']:
            print('invalid search method, please select from below choices\n')

    start_time = time.time()
    phrase_counts = search_function_dict.get(search_method, 'invalid choice')(search_term, env='prod')

    print('Search Results: ')
    for file, count in sorted_dictionary(phrase_counts).items():
        print(f'\t{file} - {count} matches')

    print(f'Elapsed time: {(time.time() - start_time)*1000:.2f} ms')
