from src import graphs
import networkx as nx
import matplotlib.pyplot as plt

def main():
    following = None
    followers = None
    option = -1
    
    while following == None and followers == None:
        following, followers = graphs.getNecessaryData()

    graph = graphs.simpleGraph(following, followers)
    G = nx.DiGraph()
    G.add_edges_from(graph)
    G.remove_edges_from(nx.selfloop_edges(G))

    while option != 4:
        print('Option 1: Print Graph\nOption 2: Page Rank\nOption 3: Hits\nOption 4: Exit')
        option = int(input('Select an option'))
        match option:
            case 1:
                pos = nx.kamada_kawai_layout(G)
                # pos = nx.spring_layout(G)
                nx.draw(G, pos, with_labels=True, node_size=100, node_color='lightgreen', font_size=8, font_color='black',
                        font_weight='bold', width=1, edge_color='skyblue')
                plt.show()
            case 2:
                #retorna um dicionario com os ranks
                pagerank = nx.pagerank(G)
            case 3:
                #retorna uma dupla cm 2 dicionarios com ranks, um dos portais e outro das autoridades
                hits = nx.hits(G)
            case 4:
                break
            case _:
                print('erro')


if __name__ == '__main__':
    main()
