import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pylab as pl


def distance(ville1, ville2):
    x1, y1 = ville1.x, ville1.y
    x2, y2 = ville2.x, ville2.y

    d = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return d


def plot_cities(villes, routes):
    fig, ax = plt.subplots()

    for ville in villes:
        x, y = ville.x, ville.y
        if ville.num == 0:
            ax.plot(x, y, 'bo', label="nid")
            pl.text(x, y, str(ville.num))
        else:
            ax.plot(x, y, '*', label=ville.num)
            pl.text(x, y, str(ville.num))
        ax.legend()

    for route in routes:
        start = route.ville_depart
        stop = route.ville_arrivee
        ax.plot([start.x, stop.x], [start.y, stop.y], '-', alpha=0.5)
    plt.show()


def plot_pheromone(routes):
    sns.catplot([route.pheromone for route in routes], kind="bar")
    plt.show()


def show_pheromones(routes):
    for route in routes:
        print("niveau de pheromone route ", route, ':', route.get_pheromone())


def show_fourmis(fourmis):
    for fourmi in fourmis:
        print("ville_actuelle ", fourmi.ville_actuelle)
        print("chemin parcouru", [str(chemin) for chemin in fourmi.chemin_parcouru])
        print("distance parcourue depuis le nid", fourmi.distance_parcourue_depuis_nid)