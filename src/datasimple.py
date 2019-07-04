import DataSetGenerator as dsg
import Pcc_recuit as algo1
import ResolverAlgo as algo2
import ToCsv
import matrixinjson as mjson


city_number = 7


def generate_matrix():

    matrix = dsg.random_symmetric_matrix(city_number)
    generate = mjson.save_matrix(matrix)
    return generate


def call_stored_matrix():

    matrix = mjson.restore_matrix()
    # call the function that generates a symmetric matrix
    datas = algo1.simulated_annealing(matrix)
    # 2 means 2opt algo 1 means SA
    ToCsv.generateCSV(datas, 1)

    init_route = list(range(city_number))
    # print(init_route)
    # matrix = dsg.random_symmetric_matrix(cityNumber)
    mat = list(matrix)
    best_route = algo2.two_opt(init_route, mat)
    print(best_route)
    # 2 means 2opt algo 1 means SA
    ToCsv.generateCSV(best_route, 2)


# TODO run only one time to generate the matrix
# generate_matrix()
call_stored_matrix()


