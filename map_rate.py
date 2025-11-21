import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json

with open("data_/MusicMaps.json") as file:
    f = json.load(file)
    table = dict()
    for map in f:
        table[map["title"]] = map["visits_total"]
    sorted_table_by_visits = sorted(table.items(), key=lambda x: x[1])
    #sorted_table_by_visits = sorted(table.items(), key=lambda x: x[1], reverse = True)
    sorted_table = dict(sorted_table_by_visits)
    fig, ax = plt.subplots()
    ax.set_title("Самые посещаемые карты")
    titles = sorted_table.keys()
    values = sorted_table.values()
    ax.barh(titles, values)
    plt.show()