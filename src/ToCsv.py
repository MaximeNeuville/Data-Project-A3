import csv


def generateCSV(datas, algo_type):

    # it's a Simulated Annealing algo
    if algo_type == 1:
        with open('../Datas/SA_datas.csv', 'a') as f:
            writer = csv.writer(f,  delimiter=',', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([len(datas[0])-1, datas[2], datas[1], datas[5]])
            print("CSV generated and/or filled")
    # it's a 2opt algo
    elif algo_type == 2:
        with open('../Datas/2OPT_datas.csv', 'a') as f:
            writer = csv.writer(f,  delimiter=',', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([datas[0], datas[1], datas[2]])
            print("CSV generated and/or filled")
    else:
        print("Algo type missing")
