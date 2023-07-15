from bs4 import BeautifulSoup
import requests
import networkx as nx
import matplotlib.pyplot as plt
from scrapping_fun import *
from create_files import *


# the programm scrapps the connections available the website.
# just like on the website, it goes over each bus line ("route")
# from there gets the information about each station on a way
# a result is a MultiGraph object with

# nodes = bus stations, attributes = station number, name, city+country (seperate tbd)
# edge = direct connections, label = line number


G = nx.MultiGraph()
url = "https://www.muenchen-zob.de/en/carriers/1"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
all_routes = soup.find_all(class_ ="route-title _fc _pj", href=True, limit=526)

i=0
for route in all_routes:
    #print(str(i)+" Route: ", route.text, "\n")
    i+=1
    G = addRoute(G, route)

nx.write_edgelist(G, 'edges1')
write_nodelist(G, 'nodes1')



