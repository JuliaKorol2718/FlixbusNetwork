import networkx as nx
G = nx.read_edgelist('edges', create_using=nx.MultiGraph)
import matplotlib.pyplot as plt

nodes = {"nr":[], "name":[], "city":[], "country":[]}


with open("nodes1", 'r', encoding="utf-8") as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        nr, name, city, country = line[:-1].split(', ')

        stop = {
            "name": name,
            "city": city,
            "country": country
        }
        nodes[nr]=stop

nx.set_node_attributes(G, nodes)

def hubs(C, nr):
    degr = sorted(dict(C.degree()).items(), key = lambda x: x[1], reverse = True)
    return degr[0:nr]


components = list(nx.connected_components(G))

#0 - big european component
#5 - turkish component

E = G.subgraph(nodes = components[0])
T = G.subgraph(nodes = components[5])

print(T.nodes(data=True))


C = E
hb = hubs(C, 10) #(node, deg)
'''
for node, deg in hb:
    li = list([node, deg, G.nodes[node]["name"], G.nodes[node]["city"], G.nodes[node]["country"]])
    print(li)
'''

countries = [y['country'] for x,y in C.nodes(data=True)]
#print(list(dict.fromkeys(countries))) #without repetition

#print(nx.diameter(E))
def Average(G):
    return sum(dict(G.degree()).values()) / G.number_of_nodes()

#print(Average(G))
#print(Average(E))
#print(Average(T))
'''
hb = hubs(E, 10)

for node, deg in hb:
    li = list([node, deg, G.nodes[node]["name"], G.nodes[node]["city"], G.nodes[node]["country"]])
    print(li)
'''

print(nx.average_shortest_path_length(T))
print(nx.average_shortest_path_length(E))


