import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json

with open("data_/users.json") as file:
    f = json.load(file)
    user = f[0]
    if (len(user["recent_accuracy"]) != 0):
        fig, ax = plt.subplots(figsize = (6, 4))
        ax.set_xlabel("последние игры")
        ax.set_ylabel("точность")
        ax.set_title("История за последние 5 игр")
        ax.grid(True)
        x = np.arange(1, 6)
        ax.plot(x, user["recent_accuracy"])
        ax.legend()
        plt.show()