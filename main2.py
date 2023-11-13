from src import graphs
import networkx as nx
import matplotlib.pyplot as plt

def main():
    following = None
    followers = None
    
    while following == None and followers == None:
        following, followers = graphs.getNecessaryData()

    graph = graphs.simpleGraph(following, followers)
    G = nx.DiGraph()
    G.add_edges_from(graph)
    G.remove_edges_from(nx.selfloop_edges(G))
    pos = nx.kamada_kawai_layout(G)
    #pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=100, node_color='lightgreen', font_size=8, font_color='black', font_weight='bold', width=1, edge_color='skyblue')
    plt.show()

if __name__ == '__main__':
    main()
