import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def distance(ville1, ville2):
    x1, y1 = ville1.x, ville1.y
    x2, y2 = ville2.x, ville2.y

    d = np.sqrt((x1-x2)**2 + (y1-y2)**2)

    return d


def plot_cities(villes, routes):

    fig, ax = plt.subplots()

    for ville in villes:
        x, y = ville.x, ville.y
        if ville.num == 0:
            ax.plot(x, y , 'bo', label="nid")
        else:
            ax.plot(x, y, '*', label=ville.num)
        ax.legend()

    for route in routes:
        start = route.ville_depart
        stop = route.ville_arrivee
        ax.plot([start.x, stop.x], [start.y, stop.y], '-', alpha=0.5)
    plt.show()


def plot_pheromone(routes):
    sns.catplot([route.pheromone for route in routes], kind="bar")
    plt.show()
