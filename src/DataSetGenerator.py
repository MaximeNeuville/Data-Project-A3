import numpy as np
import random 


def random_symmetric_matrix(n):

    # On gere les exceptions
    if int(n) < 2: 
        random_symmetric_matrix(input("Error, please enter at least 2 cities : "))
        exit()

    maxTime = 12
    # cree les valeurs random necessaire pour remplir la matrice finale 
    # (on genere seulement le nb de valeur necessaire a un triange superieur)
    R = np.random.randint(1, maxTime, size = int((n*(n-1)/2)))
    # cree une matrice remplie de 0
    P = np.zeros((n,n))

    # 1 = partie top du triange, -1 partie bottom
    P[np.triu_indices(n, 1)] = R

    # On prend la partie du triange bas de la matrice transposee
    P[np.tril_indices(n, -1)] = P.T[np.tril_indices(n, -1)]
    
    print("------------------------------------\n")
    return P

