import numpy as np


def random_symmetric_matrix(n):

    max_time = 12
    
    # that way we are sure that it is the right type
    n = int(n)
    
    # we handle one exception
    if int(n) < 2: 
        random_symmetric_matrix(int(input("Error, please enter at least 2 cities : ")))
        exit()

    cost_mat = np.random.randint(1, max_time, size=(n, n))
    cost_mat += cost_mat.T
    np.fill_diagonal(cost_mat, 0)
    print(cost_mat)

    return cost_mat
