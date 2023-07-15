import networkx as nx
from geopy.geocoders import Nominatim
from summary_functions import *
import folium

G = load_flixbus_network()
locator = Nominatim(user_agent="example app")

components = list(nx.connected_components(G))
E = G.subgraph(nodes = components[0])
T = G.subgraph(nodes = components[1])

def extract(lst):
    return [item[0] for item in lst]

hubs_E = extract(hubs(E, 10))
hubs_T = extract(hubs(T, 10))
hubs = hubs_E + hubs_T

map1 = folium.Map(
    location=[51.0, 10.0],
    tiles='cartodbpositron',
    zoom_start=4,
)
periphery = ['Erfelek, Turkey','Artvin, Turkey',
             'Kalmar, Sweden', 'Botosani, Romania']
periphery_path_E = nx.shortest_path(G, 'Kalmar, Sweden', 'Botosani, Romania')
periphery_path_T = nx.shortest_path(G,'Erfelek, Turkey','Artvin, Turkey')

'''
for v in G.nodes():
    if v in periphery_path_E or v in periphery_path_T:
        folium.Marker(
            location=[G.nodes[v]["lat"], G.nodes[v]["long"]],
            popup = G.nodes[v]["adress"]+str(', ')+
                    G.nodes[v]["stops"],
            icon=folium.Icon(color =
                            'green' if v in periphery else 'blue',
                             icon = 'circle')

        ).add_to(map1)

'''
'''
for v in G.nodes():

    folium.Marker(
        location=[G.nodes[v]["lat"], G.nodes[v]["long"]],
        popup = G.nodes[v]["adress"]+str(', ')+
                G.nodes[v]["stops"],
        icon=folium.Icon(color =
                         'red' if v in hubs else 'green' if v in periphery else 'blue',
                         icon = 'circle')

    ).add_to(map1)
'''

for v in G.nodes():
    if v in hubs:
        folium.Marker(
            location=[G.nodes[v]["lat"], G.nodes[v]["long"]],
            popup = G.nodes[v]["adress"]+str(', ')+
                    G.nodes[v]["stops"],
            icon=folium.Icon(color = 'red',
                             icon = 'circle')

        ).add_to(map1)




linelist = list()
i = 0
for u, v, line in G.edges(data=True):

    coord = [
        tuple([G.nodes[u]["lat"], G.nodes[u]["long"]]),
        tuple([G.nodes[v]["lat"], G.nodes[v]["long"]])
    ]
    linelist.append(coord)

folium.PolyLine(linelist, weight=2, color="black").add_to(map1)

map1.show_in_browser()



