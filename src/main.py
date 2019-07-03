import DataSetGenerator as dsg
import Pcc_recuit as algo1
import Pcc_recuitC1 as algo1c1
import ResolverAlgo as algo2
import ToCsv
import numpy as np
import json
import codecs


# try:
# algo = 'SA' or '2opt'
# else:
# print(algo)

# if algo != 'SA' or '2opt':
# print(algo)
# else:
# exit()

def saveMatrix(matrix):
    matrixJSON = matrix
    # print(type(matrixJSON))
    save = matrixJSON.tolist()
    # print(type(matrixJSON))
    # print(mat)

    json.dump(save, codecs.open('matrix.json', 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)


def restoreMatrix():
    obj_text = codecs.open('matrix.json', 'r', encoding='utf-8').read()
    b_new = json.loads(obj_text)
    a_new = np.array(b_new)
    # print("saved matrix is")
    # print(a_new)
    return a_new


if __name__ == '__main__':
    # TODO dois-je ajouter le cas ou on entre la matrice a partir d'un CSV ?
    print("Hello and welcome to the Route setter")
    # choosing map size
    cityNumber = input("Please enter the number of cities that you want : ")
    # generating map
    matrix = dsg.random_symmetric_matrix(cityNumber)

    # choosing algo
    print("Please chose which Algorithm to run")
    # TODO validation try catch
    algo = input("tape 'SA' for Simulated Annealing or '2opt' for 2-Opt algorithm or 'both' to compare ")
    if algo == 'SA':
        # TODO validation try catch
        condition = input("Do you want the condition of driver working time to be applied ? (answer by 'yes' or 'no') ")
        if condition == 'yes':
            # call the function that generates a symmetric matrix
            # matrix = dsg.random_symmetric_matrix(cityNumber)
            datas = algo1c1.simulated_annealing(matrix)
            print(algo1c1.total_time(datas[0], matrix))
            print(" VS without constraint : ")
            print(datas[1])
            # 2 means 2opt algo 1 means SA
            # ToCsv.generateCSV(datas, 1)

        elif condition == 'no':
            # call the function that generates a symmetric matrix
            # matrix = dsg.random_symmetric_matrix(cityNumber)
            datas = algo1.simulated_annealing(matrix)
            # 2 means 2opt algo 1 means SA
            ToCsv.generateCSV(datas, 1)

    elif algo == '2opt':
        init_route = list(range(cityNumber))
        # print(init_route)
        # matrix = dsg.random_symmetric_matrix(cityNumber)
        mat = list(matrix)
        best_route = algo2.two_opt(init_route, mat)
        print(best_route)
        # TODO define datas into 2opt algo
        # 2 means 2opt algo 1 means SA
        # ToCsv.generateCSV(datas, 2)

    elif algo == 'both':
        # call the function that generates a symmetric matrix
        # matrix = dsg.random_symmetric_matrix(cityNumber)
        datas = algo1.simulated_annealing(matrix)
        # 2 means 2opt algo 1 means SA
        ToCsv.generateCSV(datas, 1)

        init_route = list(range(cityNumber))
        # print(init_route)
        # matrix = dsg.random_symmetric_matrix(cityNumber)
        mat = list(matrix)
        best_route = algo2.two_opt(init_route, mat)
        print(best_route)
        # TODO define datas into 2opt algo
        # 2 means 2opt algo 1 means SA
        # ToCsv.generateCSV(datas, 2)