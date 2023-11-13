from src import graphs
import networkx as nx
import matplotlib.pyplot as plt

def main():
    following = None
    followers = None
    
    while following == None and followers == None:
        following, followers = graphs.getNecessaryData()

    graph = graphs.simpleGraph(following, followers)
    G = nx.Graph()
    G.add_edges_from(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=200, node_color='lightgreen', font_size=10, font_color='black', font_weight='bold', width=2, edge_color='skyblue')
    plt.show()

if __name__ == '__main__':
    main()
