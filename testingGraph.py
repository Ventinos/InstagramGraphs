import serializer
import networkx as nx
import matplotlib.pyplot as plt

following = serializer.deserializeStructure2('TempFollowings')
followers = serializer.deserializeStructure2('comp')
followers = list(followers)

graph = []
for i in range(len(following)):
    following[i]=list(following[i])

for i in range(len(following)):
    for j in range(len(following[i])):
        graph.append((followers[i],following[i][j]))
#print(graph)

G = nx.Graph()
G.add_edges_from(graph)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=200, node_color='lightgreen', font_size=10, font_color='black', font_weight='bold', width=2, edge_color='skyblue')
plt.show()
