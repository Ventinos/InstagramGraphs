InstagramGraphs,
AKA: Instagram data extraction + Visualization via Digraphs:
======

## Proposal:

We were tasked with mapping a problem to a graph solution for a Graph Theory course at university, we chose to integrate web scraping and extract data from Instagram users and map their connections to a directed graph. We begin with scraping the followers of a large account, whom we can assume will have things in common because they follow said account, and creating a set; afterwards we ((try to)) check each and every one of them to see if they follow anyone in the set, if they do we establish a connection between them in the graph.

With the scraping done, we convert it to a graph object and apply some algorithms to it in order to visualize the trends, biases and interactions within the set, all with an intuitive and usually comprehensible visual interface.

Here is the link to a presentation that we've made to explain how the program works:
[Link](https://docs.google.com/presentation/d/1K2dQcy0U66EgZyk2QPHw07vJrq5e17elqSTDnYIH500/edit?usp=sharing)

## Install the dependencies:

Make sure you have at least python 3.10 installed and pip.
```pip install -r requirements.txt```

## How it works:

We have two main applications in this repo, main.py and main2.py ((very creative, we know)), the former is responsible for the web scrapping menu and functionalities, while the latter is responsible for the building of the graph structure, visualization via matplotlib + networkx, and the application of the algorithms on the generated graph.

We have a few sets and follwings binaries for test purpose at the repo, free feel to use them to see how the main2.py works. 
* PetSet + PetFollowing build the graph of the Tutorial Education Program (PET) of the IT department of our university.
* CompSet + CompFollowing build the graph of the Samba Drum of IT department of our university + PET + IT department athletics team.

 
