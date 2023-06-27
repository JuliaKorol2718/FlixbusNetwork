import networkx as nx

def connected(u, v, G):
    return u in G.neighbors(v)

G = nx.parse_edgelist('edges', create_using=nx.MultiGraph)
print(G.edges())
nodes = {}


with open("nodes_coord", 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        nr, name, city, country, lat, long = line[:-3].split(', ')
        nodes[nr]= city + str(', ') + country

G_merged = nx.MultiGraph()
G_merged.add_nodes_from(set(nodes.values()))

for u,v,data in G.edges(data=True):
    m1 = nodes[u]
    m2 = nodes[v]
    G.edges(u,v)
    if m1!=m2:
        if not connected(m1,m2,G_merged):
            G_merged.add_edge(m1,m2, lines = data['line'])
            print(G_merged.edges(m1,m2))
        else:
            G_merged.edges[m1,m2,'lines'].append(data['line'])

nx.write_edgelist(G, 'merged_edges')

