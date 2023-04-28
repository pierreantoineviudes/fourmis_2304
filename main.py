"""
    Définition des classes de notre modèle
"""

from calculs.distance import distance, plot_cities, plot_pheromone, show_pheromones, show_fourmis
import numpy as np
import random as rd
from tqdm import tqdm

from interface_graphique.interface import FenPrincipale


class Fourmi:

    def __init__(self, nid):
        self.ville_actuelle = nid
        self.chemin_parcouru = []
        self.distance_parcourue_depuis_nid = 0


class Route:

    def __init__(self, ville_depart, ville_arrivee):
        self.ville_depart = ville_depart
        self.ville_arrivee = ville_arrivee
        self.longueur = distance(ville_depart, ville_arrivee)
        self.pheromone = 1

    def deposer_pheromone(self):
        self.pheromone += 1

    def get_pheromone(self):
        return self.pheromone

    def __str__(self):
        return str(self.ville_depart) + '_' + str(self.ville_arrivee)


class Ville:

    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

    def __str__(self):
        return str(self.num)


"""
    * Création des villes en fonction des coordonnées,
    * Création des routes entre les villes avec point de départ et d'arrivée, niveau de pheromone sur les routes
    * Création des méthodes des fourmis pour avancer, step by step
    
    Création de N fourmis au point de départ
    Condition d'arrêt? ==> avoir fait N steps
    Faire un compteur pour voir où on en est sur le chemin, tant que la distance parcourue depuis ville < longeur route,
    on fait rien (la fourmi est en train de traverser la route)
    
    Quand les fourmis sont à la fin du bail, il faut les faire retourner au nid

"""


def step(fourmis, villes, routes):
    for fourmi in tqdm(fourmis):
        # faire avancer les fourmis

        # test si la fourmi est au nid
        if fourmi.ville_actuelle == villes[0]:
            # la fourmi est au nid, il faut la faire avancer
            possible_routes = []
            for route in routes:
                if route.ville_depart == fourmi.ville_actuelle:
                    possible_routes.append(route)
            weights = [route.get_pheromone() for route in possible_routes]
            next_route = rd.choices(possible_routes, weights)[0]
            fourmi.chemin_parcouru.append(next_route)
            next_route.deposer_pheromone()
            fourmi.ville_actuelle = next_route.ville_arrivee

        elif fourmi.ville_actuelle == villes[-1]:
            # la fourmi est arrivée au food
            # il faut faire demi-tour
            # print([str(chemin) for chemin in fourmi.chemin_parcouru])
            fourmi.ville_actuelle = villes[0]    # la fourmi retourne au nid
            for route in fourmi.chemin_parcouru:
                route.deposer_pheromone()    # en retournant au nid, la fourmi dépose de la phéromone
            fourmi.distance_parcourue_depuis_nid = 0
            fourmi.chemin_parcouru = []
            break

        # test si la fourmi est sur une route ou pas
        elif fourmi.distance_parcourue_depuis_nid > fourmi.chemin_parcouru[-1].longueur and len(fourmi.chemin_parcouru) > 0:
            # la fourmi a parcouru le chemin nécessaire, il faut choisir une route
            possible_routes = []
            for route in routes:
                if route.ville_depart == fourmi.ville_actuelle:
                    possible_routes.append(route)
            weights = [route.get_pheromone() for route in possible_routes]
            next_route = rd.choices(possible_routes, weights)[0]
            fourmi.chemin_parcouru.append(next_route)
            next_route.deposer_pheromone()
            fourmi.ville_actuelle = next_route.ville_arrivee
            fourmi.distance_parcourue_depuis_nid = 0

        fourmi.distance_parcourue_depuis_nid += 1    # faire avancer la fourmi

if __name__ == '__main__':

    fen = FenPrincipale()
    fen.mainloop()

    # Création des villes
    villes = []
    for k in range(6):
        villes.append(Ville(rd.random()*10, rd.random()*10, k))

    # création des routes entre les villes
    routes = []
    routes.append(Route(villes[0], villes[1]))
    routes.append(Route(villes[1], villes[2]))
    routes.append(Route(villes[1], villes[3]))
    routes.append(Route(villes[2], villes[4]))
    routes.append(Route(villes[3], villes[4]))
    routes.append(Route(villes[4], villes[5]))

    # plot des villes
    # plot_cities(villes,routes)

    # création des fourmis
    fourmis = []
    for k in range(15):
        fourmis.append(Fourmi(villes[0]))

    for t in range(1000):
        step(fourmis, villes, routes)

    show_pheromones(routes)
    # show_fourmis(fourmis)
    plot_cities(villes, routes)