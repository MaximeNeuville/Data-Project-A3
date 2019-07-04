import DataSetGenerator as dsg
import Pcc_recuit as algo1
import Pcc_recuitC1 as algo1c1
import Pcc_recuitC2 as algo1c2
import ResolverAlgo as algo2
import ToCsv


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
    print("Please choose which Algorithm to run")
    # validating input
    while True:
        algo = input("tape 'sa' for Simulated Annealing or '2opt' for 2-Opt algorithm or 'both' to compare : ")
        if algo.lower() not in ('sa', '2opt', 'both'):
            print("Only 'sa', '2opt' and 'both' are accepted.")
        else:
            break
       
    if algo == 'sa':
        # validating input
        while True:
            condition = input("Do you want the condition of driver working time to be applied ? ('yes' or 'no') ")
            if condition.lower() not in ('yes', 'no'):
                print("Only 'yes' or 'no' are accepted.")
            else:
                break
        if condition == 'yes':
            while True:
                constraints = input("tape 'dwt' for driver working time condition or '2wt' for driver working time and opening time constraints ")
                if constraints.lower() not in ('dwt', '2wt'):
                    print("Only 'dwt' and '2wt' are accepted.")
                else:
                    break
            if constraints == 'dwt':
                datas = algo1.simulated_annealing(matrix)
                print(algo1c1.total_time(datas[0], matrix))
                print(" VS without constraint : ")
                print(datas[1])
                # 2 means 2opt algo 1 means SA
                # ToCsv.generateCSV(datas, 1)
            elif constraints == '2wt':
                datas = algo1.simulated_annealing(matrix)
                dataConstraint = algo1c2.total_time(datas[0], matrix)
                dataConstraint1 = algo1.total_time(datas[0], matrix)
                # print(total_time(datas[0], matrix))
                print("With 2 constraints : %d" % dataConstraint)
                # print("VS 1 constraints : %d" %dataConstraint1)
                print("VS without constraints : %d" % datas[1])
                print(algo1c2.total_time(datas[0], matrix))
                # 2 means 2opt algo 1 means SA
                # ToCsv.generateCSV(datas, 1)

        elif condition == 'no':
            datas = algo1.simulated_annealing(matrix)
            # 2 means 2opt algo 1 means SA
            ToCsv.generateCSV(datas, 1)

    elif algo == '2opt':
        init_route = list(range(cityNumber))
        # print(init_route)
        mat = list(matrix)
        best_route = algo2.two_opt(init_route, mat)
        print(best_route)
        # 2 means 2opt algo 1 means SA
        ToCsv.generateCSV(best_route, 2)

    elif algo == 'both':
        datas = algo1.simulated_annealing(matrix)
        # 2 means 2opt algo 1 means SA
        ToCsv.generateCSV(datas, 1)

        init_route = list(range(cityNumber))
        # print(init_route)
        mat = list(matrix)
        best_route = algo2.two_opt(init_route, mat)
        print(best_route)
        # 2 means 2opt algo 1 means SA
        ToCsv.generateCSV(best_route, 2)
