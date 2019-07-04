import DataSetGenerator as dsg
import Pcc_recuit as algo1
import ResolverAlgo as algo2


if __name__ == '__main__':

    cityNumber = input("Please enter the number of cities that you want : ")
    mat = dsg.random_symmetric_matrix(cityNumber)
    datas = algo1.simulated_annealing(mat)
    matList = list(mat)
    
    # with a random path
    init_route = list(range(int(cityNumber)))
    bad_route = algo2.two_opt(init_route, matList)

    print("\n2-OPT algorithm:")
    print("\tTotal time : %d hours" % bad_route[2])
    print("\tBest path for after 2 algorithms : %s" % bad_route[3])

    # with an optimized path

    best_route = algo2.two_opt(datas[0], matList)

    print("\nBoth algorithm combined:")
    print("\tTotal time : %d hours" % best_route[2])
    print("\tBest path for after 2 algorithms : %s" % best_route[3])