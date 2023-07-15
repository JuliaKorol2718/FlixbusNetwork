import networkx as nx
from summary_functions import *
import pandas as pd
from pathlib import Path


G = load_flixbus_network()
components = list(nx.connected_components(G))
C = G.subgraph(nodes = components[1])
df = pd.DataFrame.from_dict(dict(C.nodes(data=True)), orient='index')

countries_data = {}
for country_ in list(df.country.unique()):

    df_country = df[df.country==country_]
    subgraph = C.subgraph(nodes=list(df_country.adress))
    nr_nodes = len(subgraph.nodes())
    nr_edges = len(subgraph.edges())

    countries_data[country_] = {
        '#nodes': nr_nodes,
        '#edges': nr_edges,
        'clustering': round(nx.average_clustering(subgraph), 3),
        'connectedness': round(2*nr_edges/(nr_nodes*(nr_nodes-1)), 4) if nr_nodes>1 else 0
      }

df_countries = pd.DataFrame.from_dict(countries_data, orient='index')

print(df_countries.sort_values(by=['#nodes'], ascending=False))

'''
filepath = Path('results/df.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)
print(df)
'''