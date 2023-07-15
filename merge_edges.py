import networkx as nx

def connected(u, v, G):
    return u in G.neighbors(v)

with open("edges", 'r', encoding="utf-8") as f:
    G = nx.parse_edgelist(f.readlines(), create_using=nx.MultiGraph)

nodes = {}
with open("nodes_coord", 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        nr, name, city, country, lat, long = line[:-3].split(', ')
        nodes[nr]= city + str(', ') + country

G_merged = nx.Graph()
G_merged.add_nodes_from(set(nodes.values()))

for u,v,data in G.edges(data=True):
    ad1 = nodes[u]
    ad2 = nodes[v]

    if ad1!=ad2:
        if not connected(ad1,ad2,G_merged):
            G_merged.add_edge(ad1,ad2, lines = [data['line']])

        else:
            G_merged.edges[ad1,ad2]["lines"].append(data['line'])

nx.write_edgelist(G_merged, 'merged_edges', delimiter = '; ')

