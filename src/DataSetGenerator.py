import numpy as np
import random 


def random_symmetric_matrix(n):

    maxTime = 12

    # On gere les exceptions
    if int(n) < 2: 
        random_symmetric_matrix(input("Error, please enter at least 2 cities : "))
        exit()

    cost_mat = np.random.randint(1, maxTime, size=(n, n))
    cost_mat += cost_mat.T
    np.fill_diagonal(cost_mat, 0)
    print(cost_mat)

    return cost_mat

