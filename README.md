# InstagramGraphs, aka: Instagram data extraction + Visualization via Digraphs:

## The main idea 💡:

We made this for a Graph Theory class, and the main idea was to get the followers of big accounts and build a community. We're going to call it 'bubble' (the bubble It's the union of the followers of our start accounts),   and after that, we connect the accounts of the bubble, we do this by looking at who each person of the bubble follows that it's also in the bubble. After that we manage the data to build a graph, visualize it and apply some algorithms on it, to see how the people interact in our bubble.

Here it's the link to a presentation that we've made to explain how the program works:
//link

## Install the dependencies:

Make sure you do have at least python 3.10 installed and pip.
```pip install -r requirements.txt```

## How it works:

We have two main applications in this repo, the main.py and the main2.py, the main.py it's responsible for the web scrapping menu and functionalities, while the main2.py it's responsible for 
the building of the graph structure, visualization via matplotlib + networkx, and the algorithms application on the generated graph.

We have a few sets and follwings binaries for test purpose at the repo, free feel to use them to see how the main2.py works. 
* PetSet + PetFollowing build the graph of the Tutorial Education Program (PET) of the IT department of our university.
* CompSet + CompFollowing build the graph of the Samba Drum of IT department of our university + PET + IT department athletics team.

 
