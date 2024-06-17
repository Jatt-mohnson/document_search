import os

ROOT = os.path.dirname(os.path.abspath(__file__))
prod_file_path = f'{ROOT}/src/data/*.txt'
prod_index_path = f'{ROOT}/src/indexes/'
dev_file_path = f'{ROOT}/tests/data/*.txt'
dev_index_path = f'{ROOT}/tests/indexes/'

env_paths = {
    'dev': {'index': dev_index_path, 'files': dev_file_path},
    'prod': {'index': prod_index_path, 'files': prod_file_path}
}
