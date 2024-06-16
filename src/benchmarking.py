import timeit
import random
run_iterations = 2_000_000
words = ['travel', '1981', 'filmed', 'having', 'the', 'two', 'also', 'sixth', 'formats', 'fiction', 'these', 'refer', 'fourth', 'incarnations', 'prominently', 'panic', 'stage', '2004', 'used', '5', 'fan', 'science', 'any', 'douglas', 'eoin', 'radio', 'april', 'h2g2', 'title', 'featured', 'galaxy', 'adamsthe', 'international', 'official', 'an', 'be', 'hollywoodfunded', 'comics', 'various', 'most', 'more', 'novel12', 'drafts', 'neil', '2009', 'widely', '30', 'series', 'considered', 'new', 'chapter', 'name', 'abbreviated', '1984', 'penned', 'galaxy3', 'a', 'game', 'version', 'websites', 'comedy', 'in', 'text', 'from', 'translated', 'adaptations', 'hollywood', 'online', 'which', 'or', 'beerdavies', 'first', 'colfer', 'uk', 'to', 'is', 'dc', 'than', 'many', 'computer', 'published', 'including', 'was', 'towels', 'fictional', '2005', 'earliest', 'created', 'referred', 'did', 'other', 'produced', '4', 'film', 'comic', 'fifth', 'of', 'hhgttg', 'included', 'are', 'some', '1993', 'later', 'can', 'five', 'as', 'originally', 'broadcast', 'fans', 'hitchhikers', 'and', 'electronic', 'gradually', 'shows', 'gaiman', 'books', 'have', 'novel', 'that', 'story', 'often', 'guide', '1992', 'written', 'distributed', 'phenomenon', 'there', 'between', 'material', 'simply', 'bbc', 'this', 'seriesthe', 'languages', 'screenplay', 'been', 'adapted', 'were', 'include', 'book', 'became', 'into', 'eccentric', 'over', 'threepart', 'third', 'three', 'released', '1996', 'hg2g', '1979', 'trilogy', 'introduced', '1978', 'dont', 'multimedia', 'by', 'they', 'years', 'tv', 'on', 'several', 'films', 'it', 'novels', 'adams', 'banana', 'hamburger', 'hotdog']

# loop through the 3 search methods
for function in ['simple_string_match', 'regex_match', 'search_index']:
    code = f"""
from search_files import {function}
    
{function}('{random.choice(words)}')
    """

    execution_time = timeit.timeit(code, number=run_iterations)
    print(f'{function}: \n\ttotal time - {execution_time:.2f}\n\tavg time - {(execution_time / run_iterations)*1000:.2f} ms')
