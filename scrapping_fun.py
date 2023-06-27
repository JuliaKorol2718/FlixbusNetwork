from typing import List, Dict, Any

from bs4 import BeautifulSoup
import requests
import networkx as nx

def stopsList(route):

    #route html -> stops html
    url = route['href']
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    stops_html = soup.find(class_="stops-list _margin--top--3").find_all('a') #list of stops html's

    #stops html -> list of dictionaries with stops data
    stops_list = list()
    base_url_len = len("https://www.muenchen-zob.de/en/stops/")

    for stop in stops_html:
        url = stop['href']

        # stop_nr
        stop_nr = str(url)[base_url_len:]

        # stop_name, stop_city, soup_country
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")
        stop_name = soup.find(class_="_h1").text.encode("windows-1252", errors="replace").decode("utf-8", errors="replace") #
        stop_city_country = soup.find(class_ = "_h5 _margin--top").text.encode("windows-1252", errors="replace").decode("utf-8", errors="replace")
        try:
            stop_city, stop_country = stop_city_country.split(", ")
        except BaseException:
            print(stop_name)
            stop_city = '?'
            stop_country = '?'

        stops_list.append({
            'nr' : stop_nr,
            'name' : stop_name,
            'city' : stop_city,
            'country' : stop_country
        })

    return stops_list


def addNode(G, stop): #stop is a dict with keys 'stop_nr' and 'stop_name'
    G.add_node(stop['nr'], name=stop['name'], city=stop['city'], country=stop['country'])
    return G


def addRoute(G, route):
    # html code -> dictionary of stops data: {'nr', 'name', 'city', 'country}
    stops = stopsList(route)

    url = route['href']
    base_url_len = len("https://www.muenchen-zob.de/en/carriers/1/connections/")
    line = str(url)[base_url_len:]

    if not stops[0]['nr'] in G:
        G = addNode(G, stops[0])

    i = 0

    while i < len(stops)-1:

        stop_from = stops[i]
        stop_to = stops[i+1]

        if not stop_to['nr'] in G:
            G = addNode(G, stop_to)

        G.add_edge(stop_from['nr'], stop_to['nr'], line = line)
        i+=1

    return G


