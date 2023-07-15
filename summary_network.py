import networkx as nx
from summary_functions import *

G = load_flixbus_network()
print(G)


#------------------------------------------------------------
components = list(nx.connected_components(G))
print(components)
#0 - big turkish component
#1 - big european component

T = G.subgraph(nodes = components[0])
E = G.subgraph(nodes = components[1])

C = T

if C==T:
    print("RAPORT about the turkish component")
else:
    print("RAPORT about the european component")
#----------
print("Number of nodes = ", len(C.nodes()))
print("Number of edges = ", len(C.edges()))
print("Diameter = ", nx.diameter(C))
print("Average degree = ", round(average_degree(C), 3))
print("Clustering coefficient = ", round(nx.average_clustering(C), 3))
print("Average shortest path = ", nx.average_shortest_path_length(C))
print("Priphery nodes = ", nx.periphery(C))
print("Hubs [node's address, degree]: ")


hubs_list = hubs(C,10)
for i in range(len(hubs_list)):
    print(hubs_list[i])


#countries = list(nx.get_node_attributes(G, "country"))
#print(countries)
#countries = [y['country'] for x,y in C.nodes(data=True)]
#print(len(list(dict.fromkeys(countries)))) #without repetition

#print(len(countries))





