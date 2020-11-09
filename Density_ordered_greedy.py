from time import perf_counter
import pandas as pd


def valeur_optimale(capacite, poids, valeurs):
    # On initialise la valeur a 0
    valeur = 0.
    # On ordonne dans l'ordre decroissant les objets selon leur densité
    valeurParPoids = sorted([[v / p, p] for v, p in zip(valeurs, poids)], reverse=True)
    # TQ la capacité du sac à dos n'est pas atteinte
    while capacite > 0 and valeurParPoids:
        # on initialise la densité max à 0
        maxi = 0
        idx = None
        for i, objet in enumerate(valeurParPoids):
            # si l'objet a un volume positif et une densité plus grande que maxi alors on le grand
            if objet[1] > 0 and maxi < objet[0]:
                # maxi = densité de l'objet
                maxi = objet[0]
                # on sauvegarde l'index de l'objet pris
                idx = i

        if idx is None:
            return 0.

        # on recupere la valeur de l'objet et son poids
        v = valeurParPoids[idx][0]
        p = valeurParPoids[idx][1]
        # si le poids de l'ojet est plus petit ou égal à de la capacité restante du sac à dos
        if p <= capacite:
            # on met a jour la nouvelle valeur du sac et le nouveau poids aussi
            valeur += v * p
            capacite -= p
        else:
            if p > 0:
                valeur += capacite * v
                return valeur
        valeurParPoids.pop(idx)
    return valeur


if __name__ == "__main__":
    capacite = 130
    objets = pd.read_csv("../METHODES_EXACTES/objets.csv")
    # capacite = 3897377
    # objets = pd.read_csv("../HEURISTIQUES/moyenne.csv")
    valeurs = objets.iloc[:, 1].values
    poids = objets.iloc[:, 0].values
    start_time = perf_counter()
    valeur_opt = valeur_optimale(capacite, poids, valeurs)
    print("La valeur maximum du sac à dos = {:.10f}".format(round(valeur_opt)))
    print("Temps d execution : %s secondes " % (perf_counter() - start_time))
