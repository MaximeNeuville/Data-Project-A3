import DataSetGenerator as dsg
import time 
import random
import copy
import math
import matplotlib.pyplot as plt
import ToCsv

# Calculates the travel time for a given path
def path_travel_time(path, matrix):
    time = x = 0

    for i in range(0, len(path)):
        time = time + matrix[x][path[i]]
        x = path[i]

    return time

# Randomly swap 2 elements
def swap_value(path):
    # generates 2 different random values
    v0, v1 = random.sample(range(0, nb_city - 1), 2)

    # swap 2 values
    temp = path[v1]
    path[v1] = path[v0]
    path[v0] = temp

    return path

# Shortest path (only one time each node)
def simulated_annealing(matrix):
    clock = time.clock()

    # value too high = too many iterations (diversification)
    # for big matrice, raise the temp
    temp = 7

    # intensification
    cooling_rate = 0.001

    # nb iteration
    d = 0

    # nb_city = the matrix dimensions
    nb_city = len(matrix)

    # all total time changes during the process
    total_len_history = []

    # total path
    selected = []

    # best path TOPRINT
    path = []

    # create an initial_route
    for i in range(0, nb_city):
        path.append(i)
    path.append(0)

    # Calculate timing for the first path
    timing = path_travel_time(path, matrix)
    total_len_history.append(timing)
    selected.append(timing)

    while temp > 1:

        # randomly swap 2 cities
        new_path = swap_value(copy.copy(path))

        # Calculate the new timing
        new_timing = path_travel_time(new_path, matrix)
        total_len_history.append(new_timing)

        # Compare both timing and new timing
        if math.exp((timing - new_timing) / temp) >= random.uniform(0, 1):
            timing = new_timing
            path = new_path

        selected.append(timing)
        temp = temp * (1 - cooling_rate)
        d = d + 1

    print("Total iterations : %d" % d )
    print("Total time : %d" % timing )
    print("Best path : ")
    print(path)
    plt.plot(total_len_history)
    plt.plot(selected)
    plt.show()

    # returns a list with, path, timing, execution time, and all 
    return [path, timing, time.clock() - clock, selected, total_len_history, d]


      
if __name__ == '__main__':

    nb_city = input("Please enter the number of cities that you want : ")

    # call the function that generates a symmetric matrix
    matrix = dsg.random_symmetric_matrix(nb_city)
    datas = simulated_annealing(matrix)

    # 2 means 2opt algo 1 means SA
    ToCsv.generateCSV(datas, 1)   

