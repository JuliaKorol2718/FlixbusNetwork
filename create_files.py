def write_nodelist(G, file_):
    with open(file_, 'w', encoding="utf-8") as f:
        for stop in list(G.nodes(data=True)):
            f.write(str(stop[0])+str(", "))
            f.write(str(stop[1]['name'])+str(", "))
            f.write(str(stop[1]['city'])+str(", "))
            f.write(str(stop[1]['country']))
            f.write('\n')

def write_nodelist_coordinates(G, file_):
    with open(file_, 'w', encoding="utf-8") as f:
        for stop in list(G.nodes(data=True)):
            f.write(str(stop[0])+str(", "))
            f.write(str(stop[1]['name'])+str(", "))
            f.write(str(stop[1]['city'])+str(", "))
            f.write(str(stop[1]['country'])+str(", "))
            f.write(str(stop[1]['lat'])+str(", "))
            f.write(str(stop[1]['long']))
            f.write('\n')

def write_merged_from_df(df, file_):
    with open(file_, 'w', encoding="utf-8") as f:
        for index, stop in df.iterrows():
            f.write(str(stop['adress'])+str("; "))
            f.write(str(stop['nr_list'])+str("; "))
            f.write(str(stop['lat'])+str("; "))
            f.write(str(stop['long']))
            f.write('\n')