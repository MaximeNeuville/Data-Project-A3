import DataSetGenerator as dsg
import Pcc_recuit as algo1
import Pcc_recuitC1 as algo1c1
import ResolverAlgo as algo2
import ToCsv
import MatrixInJSON as mjson


if __name__ == '__main__':
    # TODO dois-je ajouter le cas ou on entre la matrice a partir d'un CSV ?
    '''print("Hello and welcome to the Route setter")
    # choosing map size
    while True:
        try:
            cityNumber = int(input("Please enter the number of cities that you want : "))
        except ValueError:
            print("Must be a number.")
            continue
        else:
            break'''
    cityNumber = int(input("Please enter the number of cities that you want : "))
    # generating map
    matrix = dsg.random_symmetric_matrix(cityNumber)

    # choosing algo
    print("Please chose which Algorithm to run")
    #validating input
    while True:
        algo = input("tape 'sa' for Simulated Annealing or '2opt' for 2-Opt algorithm or 'both' to compare ")
        if algo.lower() not in ('sa', '2opt', 'both'):
            print("Only 'sa', '2opt' and 'both' are accepted.")
        else:
            break
    if algo == 'sa':
        # validating input
        while True:
            condition = input("Do you want the condition of driver working time to be applied ? (answer by 'yes' or 'no') ")
            if condition.lower() not in ('yes', 'no'):
                print("Only 'yes' or 'no' are accepted.")
            else:
                break
        if condition == 'yes':
            # call the function that generates a symmetric matrix
            # matrix = dsg.random_symmetric_matrix(cityNumber)
            datas = algo1.simulated_annealing(matrix)
            print(algo1.total_time(datas[0], matrix))
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
        ToCsv.generateCSV(best_route, 2)

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
        ToCsv.generateCSV(best_route, 2)
