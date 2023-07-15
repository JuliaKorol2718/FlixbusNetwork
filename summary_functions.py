import networkx as nx
from geopy.distance import geodesic as GD

#create a graph
def load_flixbus_network():
    with open("merged_edges", 'r', encoding="utf-8") as f:
        G = nx.parse_edgelist(f.readlines(), create_using=nx.Graph, delimiter="; ")

    nodes = {"nr":[], "name":[], "city":[], "country":[], "lat":[], "long":[]}

    with open("nodes_merged", 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            adress, city, country, stops, lat, long = line[:-3].split('; ')
            stop = {
                "adress": adress,
                "city": city,
                "country": country,
                "stops": stops,
                "lat": float(lat),
                "long": float(long)
            }
            nodes[adress]=stop

    nx.set_node_attributes(G, nodes)

    edges_to_remove = list()
    for u,v,line in G.edges(data=True):
        coord = [
            tuple([G.nodes[u]["lat"], G.nodes[u]["long"]]),
            tuple([G.nodes[v]["lat"], G.nodes[v]["long"]])
        ]
        # remove improbable edges - very long distance between countries
        if GD(coord[0], coord[1]).km>600 and G.nodes[u]["country"] != G.nodes[v]["country"]:
            edges_to_remove.append([u,v])

    G.remove_edges_from(edges_to_remove)
    G.remove_nodes_from([node for node in G.nodes() if G.nodes[node]["country"]=='USA'])

    return G

#measures
def hubs(C, nr):
    degr = sorted(dict(C.degree()).items(), key = lambda x: x[1], reverse = True)
    res = [[touple[0]] + [touple[1]] for touple in degr[:nr]]
    return res

def average_degree(G):
    return sum(dict(G.degree()).values()) / G.number_of_nodes()
