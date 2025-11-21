import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json

with open("data_/users.json") as file:
    f = json.load(file)
    table = dict()
    print(f)
    for user in f:
        table[user["username"]] = user["stats"]["total_maps_completed"]
    sorted_table_by_amount = sorted(table.items(), key=lambda x: x[1], reverse = True)
    sorted_table = dict(sorted_table_by_amount)
    keys = list(sorted_table.keys())[:5]
    top_table = {key: sorted_table[key] for key in keys}
    fig, ax = plt.subplots()
    ax.set_title("Топ игроков по количеству пройденных карт")
    titles = top_table.keys()
    values = top_table.values()
    ax.scatter(titles, values)
    plt.show()


#Топ активности пользователей за последнюю неделю

