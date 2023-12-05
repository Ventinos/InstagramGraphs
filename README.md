
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

We have two main applications in this repo, ```main.py```  and ```main2.py```  ((very original, we know)), the former is responsible for the web scrapping menu and functionalities, while the latter is responsible for the building of the graph structure, visualization via matplotlib + networkx, and the application of the algorithms on the generated graph.

We have a few sets and followings binaries for test purposes at the repo, free feel to use them to see how the ```main2.py``` works. 
* PetSet + PetFollowing are used to build the graph of the Tutorial Education Program (PET) of the IT department of our university.
* CompSet + CompFollowing are used to build the graph of the musical team (referred to here in Brazil as a "Bateria") of the IT department of our university + PET + IT department athletics team.

## Scraping:

In very simple terms, we utilize selenium and beautifulsoup to automate the process of data scraping, which can be summarized as follows:
* Log onto Instagram from a burner account ((we get banned a lot, would strongly advise against using your personal account));
* Choose whether we want to generate a new set by scraping the followers of a given account(s) or scrape the followings of the accounts already within a set:
	* For the former, the user will input the desired accounts and the program will access them and collect the data, afterward the set is saved as a binary file which the user is prompted to name.
	* For the latter, the program will automatically try to access all of them and collect the data, however we have to make a few adjustments and establish a few contingencies:
		* After accessing a few of the accounts in the set, our own account will start to have it's actions restricted by Instagram ((not a ban yet)) and when it happens, for an unspecified amount of time and for every browser or application we use, our account will not be able to access the followings tab of other accounts. Therefore we found a way to check if "null data" is being scraped and when that happens the program will save the progress and close itself.
		* There are many other instances where saving our progress would be valuable, in case the computer spontaneously combusts or someone steps on the router cable. Therefore we chose to establish a checkpoint every 5 iterations of the scraping loop, so we never stand to loose too much work.
		* If the program comes across a private account it will not be able to access the followings tab and will halt. Therefore we utilized beautifulsoup to check the HTML contents of the page and see if it has the text containers related to private accounts, if it does the program will simply go to the next account and the current one will remain as following no one. This method can also be applied to checking if an account no longer exists, which can happen if it is deleted in between the generation of the set and it's turn to be scraped.
* After the followers scrape, we save our set in a binary using pickle lib, because we're going to need it to build the graph later.
* As we scrape who each account follows in the set, we make our checkpoints at TempFollowing binary and in a .txt file, so if you want to stop scrapping a set and go to another one, rename TempFollowings and the .txt .
* With this two binaries, the set and the followings, you can run main2.py and use the graph functionalities.
* There's a lot going on at the codebase, so if you want more details, fell free to have a look at it.

## Algorithms and visualization:

All you need to know about the graphs and the way it works it's at this file and at the graph package, it's pretty simple, so any doubt you can just take the code and read it. We're mainly using the algorithms implementations of the networkx lib, so any doubt about the code take a look at the lib documentation.

## Obs:
This is a college project made in basically a month so, there is a lot of things that can be improved and better organized, feel free to make a push request or a fork and help us to improve this project!
