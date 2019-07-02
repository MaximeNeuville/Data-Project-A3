import csv
def generateCSV(datas, algoType):

    # it's a Simulated Annealing algo
    if algoType == 1:
        with open('../Datas/SA_datas.csv', 'a') as f:
            writer =  csv.writer(f,  delimiter=',', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([len(datas[0])-1, datas[2], datas[5], datas[0]])
            print("CSV generated and/or filled")
    # it's a 2opt algo
    elif algoType == 2:
        with open('../Datas/2OPT_datas.csv', 'a') as f:
            writer =  csv.writer(f,  delimiter=',', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([len(datas[0])-1, datas[2], datas[5], datas[0]])
            print("CSV generated and/or filled")
    else :
        print("Algo type missing")