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
    while option != 5:
        print('Option 1: Print Graph\nOption 2: Page Rank\nOption 3: Hits\nOption 4: Six Degrees of Separation\nOption 5: Exit\n')
        option = int(input('Select an option: '))
        match option:
            case 1:
                pos = nx.kamada_kawai_layout(G)
                # pos = nx.spring_layout(G)
                nx.draw(G, pos, with_labels=True, node_size=100, node_color='lightgreen', font_size=8, font_color='black',
                        font_weight='bold', width=1, edge_color='skyblue')
                plt.show()
            case 2:
                #retorna um dicionario com os ranks
                pos = nx.kamada_kawai_layout(G)
                pagerank = nx.pagerank(G)

                #gera um array chamado "cores" que possui os itens de cada chave do dicionario "pagerank", na ordem em que aparece os nos no G.nodes()
                colors = [pagerank.get(no) for no in G.nodes()]
                
                #pinta cada no com sua cor correspondente (correspondencia via equivalencia de posicao entre os arrays "cores" e G.nodes()
                nx.draw(G, pos, with_labels=True, node_size=100, node_color = colors, font_size=8, font_color='black',
                        font_weight='bold', width=1, edge_color='skyblue', cmap=plt.cm.plasma)
                plt.show()
            case 3:
                pos = nx.kamada_kawai_layout(G)
                #retorna uma dupla cm 2 dicionarios com ranks, um dos portais e outro das autoridades
                colorsHits = []
                (hub,autho) = nx.hits(G)
                for name in G.nodes():
                    indHub = hub.get(name)
                    indAutho = autho.get(name)
                    if indAutho-indHub<0.00 : #caso seja portal
                        colorsHits.append('pink')
                    else : #caso seja autoridade
                        colorsHits.append('yellow')

                nx.draw(G, pos, with_labels=True, node_size=100, node_color = colorsHits, font_size=8, font_color='black',
                        font_weight='bold', width=1, edge_color='skyblue')
                plt.show()
            case 4:
                totalPaths = 0
                nPaths = 0
                for i in G.nodes():
                    for j in G.nodes():
                        if i!=j :
                            try:
                                path = nx.shortest_path(G,i,j)
                                nPaths+=1
                                totalPaths += len(path)
                            except nx.NetworkXNoPath:
                                continue

                print('Average value = ' + str(float(totalPaths/nPaths)) + '\n')
            case 5:
                break
            case _:
                print('error')


if __name__ == '__main__':
    main()
