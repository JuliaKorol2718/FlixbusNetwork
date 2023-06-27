import networkx as nx
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium

G = nx.read_edgelist('edges', create_using=nx.MultiGraph)
nodes = {"nr":[], "name":[], "city":[], "country":[], "lat":[], "long":[]}
locator = Nominatim(user_agent="example app")
geocode = RateLimiter(locator.geocode, min_delay_seconds=0.1)

#test_list = list()

with open("nodes_coord", 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:

        nr, name, city, country, lat, long = line[:-3].split(', ')
        stop = {
            "name": name,
            "city": city,
            "country": country,
            "lat": lat,
            "long": long
        }
        nodes[nr]=stop

nx.set_node_attributes(G, nodes)


map1 = folium.Map(
    location=[51.0, 10.0],
    tiles='cartodbpositron',
    zoom_start=4,
)

for nr in G.nodes():
    if G.nodes[nr]["lat"] != '?':
        folium.Marker(
            location=[G.nodes[nr]["lat"], G.nodes[nr]["long"]],
            popup = str(nr)+str(', ')+
                    G.nodes[nr]["name"]+str(', ')+
                    G.nodes[nr]["city"]+str(', ')+
                    G.nodes[nr]["country"]
        ).add_to(map1)
'''
linelist = list()
for nr1, nr2, line in G.edges(data=True):
    if G.nodes[nr1]["lat"] != '?' and G.nodes[nr2]["lat"] != '?':
        linelist.append(list([tuple([G.nodes[nr1]["lat"], G.nodes[nr1]["long"]]),
        tuple([G.nodes[nr2]["lat"], G.nodes[nr2]["long"]])]))

folium.PolyLine(linelist)
'''
map1.show_in_browser()



