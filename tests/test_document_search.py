import sys, random
sys.path.append('../')
from src.search_files import search_index, simple_string_match, regex_match, process_text
def test_search_index():
    phrase = "the"
    expected_result = {'french_armed_forces.txt': 64, 'hitchhikers.txt': 29, 'warp_drive.txt': 6}
    assert search_index(phrase) == expected_result

def test_simple_string_match():
    phrase = "the"
    expected_result = {'french_armed_forces.txt': 64, 'hitchhikers.txt': 29, 'warp_drive.txt': 6}
    assert simple_string_match(phrase) == expected_result

def test_regex_match():
    phrase = "the"
    expected_result = {'french_armed_forces.txt': 64, 'hitchhikers.txt': 29, 'warp_drive.txt': 6}
    assert regex_match(phrase) == expected_result

def test_search_index_uppercase():
    phrase = process_text("THE")
    expected_result = {'french_armed_forces.txt': 64, 'hitchhikers.txt': 29, 'warp_drive.txt': 6}
    assert search_index(phrase) == expected_result

def test_simple_string_match_uppercase():
    phrase = process_text("THE")
    expected_result = {'french_armed_forces.txt': 64, 'hitchhikers.txt': 29, 'warp_drive.txt': 6}
    assert simple_string_match(phrase) == expected_result

def test_regex_match_uppercase():
    phrase = process_text("THE")
    expected_result = {'french_armed_forces.txt': 64, 'hitchhikers.txt': 29, 'warp_drive.txt': 6}
    assert regex_match(phrase) == expected_result
def test_search_index_timing():
    phrase = "the"
    import time
    start_time = time.time()
    search_index(phrase)
    assert time.time() - start_time < 1

def test_simple_string_match_timing():
    phrase = "the"
    import time
    start_time = time.time()
    simple_string_match(phrase)
    assert time.time() - start_time < 1

def test_regex_match_timing():
    phrase = "the"
    import time
    start_time = time.time()
    regex_match(phrase)
    assert time.time() - start_time < 1
def test_all_searches_match():
    word_list = ['having', 'the', 'two', 'also', 'sixth', 'formats', 'fiction', 'these', 'refer']
    phrase = random.choice(word_list)
    assert regex_match(phrase) == simple_string_match(phrase) == search_index(phrase)


