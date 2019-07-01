import numpy as np
import random 


def random_symmetric_matrix(n):

    # TO DO
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
    
    print("Matrice avant")
    print(P)


    # for i in range(0,n):
    #     # on teste si toutes les villes ont au moins une connexion
    #     if int(P[i].sum()) <= 0:
    #         # print("ERROR line : ")
    #         # print(i)
    #         # print(int(P[i].sum()))
    #         randomX = np.random.randint(0,n-1)
    #         # print("randomX")
    #         # print(randomX)

    #         randomTime = np.random.randint(1,maxTime)
            
    #         # print("randomTime")
    #         # print(randomTime)

    #         # On verifie qu'ils ne sont pas egaux pour ne pas ajouter une valeur dans la diagonale
    #         while randomX == i: 
    #             randomX = np.random.randint(0,n-1)
    #         P[i][randomX] = randomTime
    #         P[randomX][i] = randomTime

            
    #         # print("modified value")
    #         # print(P[randomX][i])

    print("------------------------------------\n")
    print(P)
    return P


CityNumber = input("Please enter the number of cities that you want : ")
random_symmetric_matrix(CityNumber)
# random_symmetric_matrix(4)