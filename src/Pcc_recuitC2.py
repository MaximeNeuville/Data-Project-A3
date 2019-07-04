import DataSetGenerator as dsg
import Pcc_recuit as pcc
import Pcc_recuitC1 as pcc1

travel = 12
rest = 12


def total_time(path, matrix):
    time = x = 0
    # time remaining for a day of work
    time_remaining = travel

    # time during which the city is open to take the delivery from 8 to 20
    # we start the day at 8
    actual_time = 8
    stops = []

    # len - 1 ?
    for i in range(1, len(path)):
        # variable used to store the remaining time to wait before traveling again
        time_remaining_to_node = matrix[x][path[i]]
        # global time between two nodes
        time_between_node = matrix[x][path[i]]

        # true when we reach a node
        reached_node = False
        print('Starts at %d:00 at the node %d' % (actual_time, x))
        actual_time = (actual_time + time_between_node) % 24
        print('Should arrive to the node %d at %d:00 if no rest' % (path[i], actual_time))
        while not reached_node:
            if time_remaining_to_node <= time_remaining:
                time_remaining = time_remaining - time_remaining_to_node
                if time_remaining == 0:
                    stops.append(path[i])
                    print("\tRests at the node : %d" % path[i])
                    time_remaining = travel
                    time = time + rest
                    actual_time = (actual_time + rest) % 24
                    print('\tRests %d hours' % rest)
                time = time + time_between_node
                # actual_time = actual_time + 
                reached_node = True
                # if it's between 8AM or 8PM we can deliver, otherwise : wait
            else:
                # has rested between two points
                time_remaining_to_node = time_remaining_to_node - time_remaining
                stops.append([x, path[i]])
                print("\tRests between %d and %d for %d hours" % (x, path[i], rest))

                # rests 12 hours
                time = time + rest
                actual_time = (actual_time + rest) % 24
                time_remaining = travel
        if 8 <= actual_time <= 20:
            # pass
            print('\tArrives at %d:00, so he can deliver ' % actual_time)
        else:
            # print('\tNOT between 8 and 20, wait %d hour(s)' %actual_time)
            if 0 <= actual_time < 8:
                diff = 8 - actual_time
                time = time + diff 
            else:
                diff = 24 - actual_time + 8 
                time = time + diff
            print("The city %d was closed for %d hour(s)" % (path[i], diff)) 
            actual_time = 8

        x = path[i]
    return time

# IF main.py doesn't work just try here
'''
if __name__ == '__main__':

    nb_city = input("Please enter the number of cities that you want : ")

    # call the function that generates a symmetric matrix
    matrix = dsg.random_symmetric_matrix(nb_city)
    datas = pcc.simulated_annealing(matrix)
    dataConstraint = total_time(datas[0], matrix)
    dataConstraint1 = pcc1.total_time(datas[0], matrix)

    # print(total_time(datas[0], matrix))
    print("With 2 constraints : %d" % dataConstraint)
    # print("VS 1 constraints : %d" %dataConstraint1)
    print("VS without constraints : %d" % datas[1])
'''