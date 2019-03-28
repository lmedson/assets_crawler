import json
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def set_tuples(data):
    repetition = []
    relations = []

    for i in range(len(data)):
        new_relations = []
        new_repetitions = []

        new_repetitions.extend([data[i]["page"]
                                for j in range(len(data[i]["related_links"]))])
        new_relations.extend(data[i]["related_links"])

        self_repetion = tuple(new_repetitions)
        self_relations = tuple(new_relations)

        repetition.append(self_repetion)
        relations.append(self_relations)
    return tuple(repetition), tuple(relations)


def save_json(data, filename):
    data_json = json.dumps(data)

    with open(filename, 'w+') as json_file:
        json_file.write(data_json)
        return filename


def plot_map(file):
    with open(file) as data:
        get_data = json.loads(data.read())

    rep, rel = set_tuples(get_data)

    d = pd.DataFrame()
    df = []

    for j in range(len(rel)):
        df = pd.DataFrame({'from': [rep[j][i]
                                    for i in range(len(rep[j]))], 'to': [rel[j][i]
                                                                         for i in range(len(rel[j]))]})
        d.append(df)
        G = nx.from_pandas_edgelist(df, 'from', 'to')

        nx.draw(G, with_labels=True, width=2, edge_color="skyblue",
                style="solid")
        name_image = str(j)+'.png'
        plt.show(name_image)
