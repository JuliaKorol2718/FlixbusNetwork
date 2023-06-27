from bs4 import BeautifulSoup
import requests
import networkx as nx
import matplotlib.pyplot as plt
from scrapping_fun import *
from create_files import *

#node attributes = station number, name, city+country (seperate tbd)
#edge label = line number


G = nx.MultiGraph()
url = "https://www.muenchen-zob.de/en/carriers/1"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
#print(doc.prettify())
all_routes = soup.find_all(class_ ="route-title _fc _pj", href=True, limit=526)

i=0

for route in all_routes:
    #print(str(i)+" Route: ", route.text, "\n")
    i+=1
    G = addRoute(G, route)

#nx.write_edgelist(G, 'edges1')
write_nodelist(G, 'nodes1')



