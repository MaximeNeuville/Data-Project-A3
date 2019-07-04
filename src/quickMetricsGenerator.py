import DataSetGenerator as dsg
import Pcc_recuit as algo1
import ResolverAlgo as algo2
import ToCsv


def metricsGenerator(cityNumber):

    # generating map
    for i in range (0,10,1):
        matrix = dsg.random_symmetric_matrix(cityNumber)
        # call the function that generates a symmetric matrix
        # TODO to run comment the plotes of the algo (simulated annealing)
        datas = algo1.simulated_annealing(matrix)
        # 2 means 2opt algo 1 means SA
        ToCsv.generateCSV(datas, 1)

        init_route = list(range(cityNumber))
        # print(init_route)
        # matrix = dsg.random_symmetric_matrix(cityNumber)
        mat = list(matrix)
        best_route = algo2.two_opt(init_route, mat)
        print(best_route)
        # 2 means 2opt algo 1 means SA
        ToCsv.generateCSV(best_route, 2)

def poolMetricsGenerator ():

    metricsGenerator(5)
    metricsGenerator(10)
    #metricsGenerator(25)
    metricsGenerator(50)
    #metricsGenerator(75)
    metricsGenerator(100)
    metricsGenerator(500)
    metricsGenerator(1000)
    #metricsGenerator(2500)
    #metricsGenerator(5000)

poolMetricsGenerator()