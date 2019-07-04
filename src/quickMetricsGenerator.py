import DataSetGenerator as dsg
import Pcc_recuit as algo1
import ResolverAlgo as algo2
import ToCsv


def metrics_generator(city_number):

    # generating map
    for i in range(0, 9, 1):
        matrix = dsg.random_symmetric_matrix(city_number)
        # call the function that generates a symmetric matrix
        # TODO to run comment the plotes of the algo (simulated annealing)
        datas = algo1.simulated_annealing(matrix)
        # 2 means 2opt algo 1 means SA
        ToCsv.generateCSV(datas, 3)

        init_route = list(range(city_number))
        # print(init_route)
        # matrix = dsg.random_symmetric_matrix(cityNumber)
        mat = list(matrix)
        best_route = algo2.two_opt(init_route, mat)
        print(best_route)
        # 2 means 2opt algo 1 means SA
        ToCsv.generateCSV(best_route, 4)


def pool_metrics_generator():

    metrics_generator(5)
    metrics_generator(10)
    # metrics_generator(25)
    metrics_generator(50)
    # metrics_generator(75)
    metrics_generator(100)
    metrics_generator(500)
    metrics_generator(1000)
    # metrics_generator(2500)
    # metrics_generator(5000)


pool_metrics_generator()
