from bs4 import BeautifulSoup
import requests
import networkx as nx
import matplotlib.pyplot as plt
from scrapping_fun import *
from create_files import *

G = nx.read_edgelist('edges', create_using=nx.MultiGraph)
print(G.degree(['1365']))

