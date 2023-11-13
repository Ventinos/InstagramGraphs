from src import serializer
import os

def getNecessaryData():
    set = input('What set do you want to use to draw the graph? ')
    followings = input('What followings file do you want to use to draw the graph? ') or 'TempFollowings'
    
    set = os.path.join('bins',set)
    followings = os.path.join('bins',followings)
    
    try:
        following = serializer.deserializeStructurePath(followings)
        followers = serializer.deserializeStructurePath(set)
        followers = list(followers)
    except:
        return None, None
    return following,followers

def simpleGraph(following,followers):
    graph = []
    
    for i in range(len(following)):
        following[i]=list(following[i])

    for i in range(len(following)):
        for j in range(len(following[i])):
            graph.append((followers[i],following[i][j]))
    
    return graph
