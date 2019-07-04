import DataSetGenerator as dsg
import Pcc_recuit as algo1
import Pcc_recuitC1 as algo1c1
import Pcc_recuitC2 as algo1c2
import ResolverAlgo as algo2
import ToCsv


if __name__ == '__main__':
    cityNumber = int(input("Please enter the number of cities that you want : "))
    # generating map
    matrix = dsg.random_symmetric_matrix(cityNumber)

    # choosing algo
    print("\nPlease choose which Algorithm to run")
    # validating input
    while True:
        algo = input("\tTape 'sa' for Simulated Annealing or '2opt' for 2-Opt algorithm or 'both' to compare : ")
        print("\n")
        if algo.lower() not in ('sa', '2opt', 'both'):
            print("\tOnly 'sa', '2opt' and 'both' are accepted.")
        else:
            break
       
    if algo == 'sa':
        # validating input
        while True:
            condition = input("\tDo you want the condition of driver working time to be applied ? ('yes' or 'no') : ")
            if condition.lower() not in ('yes', 'no'):
                print("\tOnly 'yes' or 'no' are accepted.")
            else:
                break
        if condition == 'yes':
            while True:
                constraints = input("\tTape 'dwt' for driver working time condition or '2wt' for driver working time and opening time constraints : ")
                if constraints.lower() not in ('dwt', '2wt'):
                    print("\tOnly 'dwt' and '2wt' are accepted.")
                else:
                    break
            if constraints == 'dwt':
                datas = algo1.simulated_annealing(matrix)
                dataConstraint = algo1c1.total_time(datas[0], matrix)
                print("Total time with 1 constraints : %d hours" % dataConstraint)
                print("Total time without constraints : %d hours" % datas[1])

            elif constraints == '2wt':
                datas = algo1.simulated_annealing(matrix)
                dataConstraint = algo1c2.total_time(datas[0], matrix)
                # print(total_time(datas[0], matrix))
                print("Total time with 2 constraints : %d hours" % dataConstraint)
                print("Total time without constraints : %d hours" % datas[1])

        elif condition == 'no':
            datas = algo1.simulated_annealing(matrix)

    elif algo == '2opt':
        init_route = list(range(cityNumber))
        mat = list(matrix)
        best_route = algo2.two_opt(init_route, mat)
        print("\n2OPT algorithm :")
        print("\tTotal time : %d hours" % best_route[2])
        print("\tExecution time : %d s" % best_route[1])
        print("\tBest path for : %s" % best_route[3])

    elif algo == 'both':
        datas = algo1.simulated_annealing(matrix)
        init_route = list(range(cityNumber))
        mat = list(matrix)
        best_route = algo2.two_opt(init_route, mat)
        print("\n2OPT algorithm :")
        print("\tTotal time : %d hours" % best_route[2])
        print("\tExecution time : %d s" % best_route[1])
        print("\tBest path for : %s" % best_route[3])     
