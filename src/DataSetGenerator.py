import numpy as np
import random 


def random_symmetric_matrix(n):

    # cree les valeurs random necessaire pour remplir la matrice finale 
    # (on genere seulement le nb de valeur necessaire a un triange)
    R = np.random.randint(0, 12, size=(n*(n-1)/2))

    # cree une matrice remplie de 0
    P = np.zeros((n,n))

    # 1 = partie top du triange, -1 partie bottom
    P[np.triu_indices(n, 1)] = R
    
    # On prend la partie du triange bas de la matrice transposée
    P[np.tril_indices(n, -1)] = P.T[np.tril_indices(n, -1)]

    print(P)
    return P
    # TODOOOO
#tester si au moins une valeur non nulle
random_symmetric_matrix(4)