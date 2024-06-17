# Document Search Case Study
The goal of this exercise is to create a working program to search a set of documents for the given search term or phrase (single token), and return results in order of relevance.
Relevancy is defined as number of times the exact term or phrase appears in the document.

Create three methods for searching the documents:
- Simple string matching
- Text search using regular expressions
- Preprocess the content and then search the index

Prompt the user to enter a search term and search method, execute the search, and return results.

## usage
#### main program
1. Ensure you have python 3 installed.
2. In terminal, navigate to the document_search/src/ directory.
3. Run command below and follow the prompts:
```
python search_files.py
```
#### Benchmarking Script
1. Ensure you have python 3 installed.
2. In terminal, navigate to the document_search/src/ directory.
3. Run command below:
```
python benchmarking.py
```
#### Testing
1. pip install pytest if it is not already installed
2. In terminal, navigate to the document_search/tests/ directory.
3. Run command below:
```
pytest
```

## Performance Test Results
- simple_string_match:
  - total time - 346.63 s
  - avg time - 0.17 ms

- regex_match:
  - total time - 403.79 s
  - avg time - 0.20 ms
  
- search_index:
  - total time - 264.92 s
  - avg time - 0.13 ms

The index search method is fastest, because all the text processing has already been done prior to the user entering a 
search term. This indexing benefit will continue to grow as more documents are added into the catalog. 

## How can we continue to scale?
The first step to scaling this program is to move it from a local machine and into the cloud which opens up a wide
variety of both software and hardware scaling options. Once in the cloud, we can leverage autoscaling and load balancers
to ensure our app is always able to handle spikes in request volume or storage needs. Beyond relying on hardware scaling 
we can also use more modern software like elasticsearch which uses distributed computing and partitioned indexes to faster
search our index.