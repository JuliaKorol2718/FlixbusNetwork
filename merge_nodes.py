import pandas as pd
from create_files import *

stops = pd.DataFrame(columns=["adress", "city", "country", "nr_list", "lat", "long"])
adress_list = list()
stops = stops.astype('object')

with open('nodes_coord', "r", encoding="utf-8") as f:
    lines = f.readlines()
    i=0
    for line in lines:
        nr, name, city, country, lat, long = line[:-2].split(', ')
        adress = city + str(', ') + country

        if adress not in adress_list:
            adress_list.append(adress)
            new = pd.DataFrame({
                'adress': adress,
                'city': city,
                'country': country,
                'nr_list': [[nr]],
                'lat': lat,
                'long': long}, dtype='object')

            stops = pd.concat([stops, new], join='outer', ignore_index=True)

        else:
            row = stops.index[stops['adress']==adress].tolist()[0]
            stops.at[row,'nr_list'].append(nr)
        i+=1

write_merged_from_df(stops, "nodes_merged")
