import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_edge(1,2)
fig = plt.figure(figsize=(15,15))
pos = nx.spring_layout(G,  k=0.65, iterations=300)
labels = nx.get_node_attributes(G, 'city')
nx.draw(G, pos, node_size=100, node_color='lightblue', font_size=8, font_weight='bold')
nx.draw_networkx_labels(G,pos, labels= labels)
plt.show()


#nx.write_edgelist(G, 'edges', data=True)
#plt.savefig("Graph.png", format="PNG")