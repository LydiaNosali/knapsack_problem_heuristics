# Nous pouvons avoir deux catégories de problèmes de sac à dos:
# [1] 0/1 Problème de sac à dos:
# Ici, les éléments ne sont pas divisibles.
# [2] Problème fractionné de sac à dos:
# Ici, les articles sont divisibles afin que nous puissions également collecter des parties de l'article.
# On cherche à maximiser le nombre d'objets dans la sac a dos

from time import perf_counter
import pandas as pd


class ObjetVal:
    """La valeur des objets """

    def __init__(self, p, val, ind):
        self.p = p
        self.val = val
        self.ind = ind
        self.cout = val // p

    def __lt__(self, autres):
        return self.cout < autres.cout


class Fractionnaire_Poids:

    @staticmethod
    def ValeurMax(p, val, capacite):

        """fonction pour trouver la valeur maximum  """
        iVal = []
        for i in range(len(p)):
            iVal.append(ObjetVal(p[i], val[i], i))
        # On ordonne dans l'ordre croissant les objets selon leur poids
        iVal.sort(reverse=False)

        Valeurtotal = 0
        for i in iVal:
            pcourrant = int(i.p)
            Valcourrante = int(i.val)
            # comparer le poids donné avec la capacité
            # si le poid est inferieur ou egal a la capacite
            if capacite - pcourrant >= 0:
                # soustraire le poids de l'article du poids courant
                capacite -= pcourrant
                # ajouter la valeur de l'article a la valeur courante
                Valeurtotal += Valcourrante
            else:  # sinon
                # on calcul la fraction
                fraction = capacite / pcourrant
                # on collecte la valeur selon le poid restant
                Valeurtotal += Valcourrante * fraction
                capacite = int(capacite - (pcourrant * fraction))
                break
        return Valeurtotal


if __name__ == "__main__":
    capacite = 130
    objets = pd.read_csv("../METHODES_EXACTES/objets.csv")
    # capacite = 3897377
    # objets = pd.read_csv("../HEURISTIQUES/moyenne.csv")
    valeurs = objets.iloc[:, 1].values
    poids = objets.iloc[:, 0].values
    start_time = perf_counter()
    maxValue = Fractionnaire_Poids.ValeurMax(poids, valeurs, capacite)
    print("La valeur maximum du sac à dos =", round(maxValue))
    print("Temps d execution : %s secondes " % (perf_counter() - start_time))
