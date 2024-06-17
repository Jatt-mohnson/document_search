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
The first step to scaling this program is to move it from a local machine and into the cloud. Once our app and data is hosted
in one of the major cloud providers we can take advantage of a wide variety of both software and hardware scaling options. 
From the hardware perspective, we could leverage autoscaling to increase our compute and storage either vertically or horizontally
to ensure our app is always able to handle spikes in request volume or storage needs. If we decide to scale vertically, 
then we will need to make sure our program's code is asynchronous so that it can handle multiple requests at once. 
If we decide to scale horizontally then we will want to implement a load balancer to make sure requests are spread evenly
across our machines. However, rather than manually building and managing all of this new hardware it is likely smarter to
use a software already built to perform document search tasks at scale. One popular option would be Elasticsearch. 
Elasticsearch takes a similar approach that I wrote for the index search method but uses scalable distributed computing and 
partitioned indexes to faster return results.