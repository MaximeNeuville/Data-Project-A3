import DataSetGenerator as dsg
import time
import random
import copy
import math
import Pcc_recuit as pcc

travel = 12
rest = 12


def total_time(path, matrix):
    time = x = 0
    # time remaining for a day of work
    time_remaining = travel
    stops = []

    # len - 1 ?
    for i in range(1, len(path)):
        # variable used to store the remaining time to wait before traveling again
        time_remaining_to_node = matrix[x][path[i]]

        # true when we reach a node
        reached_node = False
        while not reached_node:
            # if time_remaining_to_node == 0 or time_remaining_to_node <= time_remaining:
            if time_remaining_to_node <= time_remaining:
                time_remaining = time_remaining - time_remaining_to_node
                if time_remaining == 0:
                    stops.append(path[i])
                    print("Rests at the node : %d" % path[i])
                    time_remaining = travel
                    time = time + rest
                time = time + matrix[x][path[i]]
                reached_node = True
            else:
                # has rested between two points
                time_remaining_to_node = time_remaining_to_node - time_remaining
                stops.append([x, path[i]])
                print("\tRests between %d and %d for %d hours" % (x, path[i], rest))
                # rests 12 hours
                time = time + rest
                time_remaining = travel
        x = path[i]

    return time


# IF main.py doesn't work just try here (dont forget to uncomment the import section)

'''
if __name__ == '__main__':

    nb_city = input("Please enter the number of cities that you want : ")

    # call the function that generates a symmetric matrix
    matrix = dsg.random_symmetric_matrix(nb_city)
    datas = pcc.simulated_annealing(matrix)
    print(total_time(datas[0], matrix))
    print(" VS without constraint : ")
    print(datas[1])
'''