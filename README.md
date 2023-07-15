# FlixbusNetworkProject

The project scrappes data from a website https://www.muenchen-zob.de/en/carriers/1 and using networkx creates a graph of flixbus connections in Europe. 
Because of the quality of the data, files "nodes1" and "nodes_coord" where corrected by hand. The nodes are flixbus stations, and between two nodes there exist
an edge with the line name, if this line connects directly those two stations.

In the project is done:
-> scrapping the data into a Multigraph, storing Flixbus stations and it's adresses
-> merging multiedges into simple ones
-> merging stations from one city into one node
-> scrapping coordinates of the stations and creates a folium map of the network
-> calculates some popular graph measures and quantities and summarises it

Warning: during the work on the project, the data on the website changed, so the data is unfortunatelly not actual.
