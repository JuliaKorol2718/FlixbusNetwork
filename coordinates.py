import networkx as nx
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium
from create_files import *


G = nx.read_edgelist('edges', create_using=nx.MultiGraph)
nodes = {"nr":[], "name":[], "city":[], "country":[]}
locator = Nominatim(user_agent="example app")
geocode = RateLimiter(locator.geocode, min_delay_seconds=0.1)


with open("nodes_coord", 'r', encoding="utf-8") as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        nr, name, city, country, lat, long = line[:-2].split(', ')
        adress = city + ", " + country

        if lat == '?':
            location = geocode(adress)
            try:
                lat, long, alt = tuple(location.point)
            except:
                lat = '?'
                long = '?'

        stop = {
            "name": name,
            "city": city,
            "country": country,
            "adress": adress,
            #"location": location,
            "lat": lat,
            "long": long
        }
        nodes[nr]=stop

nx.set_node_attributes(G, nodes)
#write_nodelist_coordinates(G, 'nodes_coord1')


