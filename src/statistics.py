import pandas as pd
import numpy as np
import statistics as sta
import matplotlib.pyplot as plt

results_2opt = pd.read_csv("../Datas/QMGSA_datas.csv", sep=",", skiprows= 1, usecols=[1, 2])

dfsa = pd.DataFrame(results_2opt)

print(results_2opt)


# results_sa = pd.read_csv("../Datas/QMGSA_datas.csv", sep=",", skiprows= 1)
# #results_2opt = pd.read_csv("../Datas/QMG2OPT_datas.csv", sep=",")
#
#
# # xaxe = pd.read_csv(r'../Datas/linearRegressionSA.csv', usecols=[2], skiprows=1)
# # yaxe = pd.read_csv(r'../Datas/linearRegressionSA.csv', usecols=[2], skiprows=1)
# # print(results_sa)
#
#
#
# print(df)


#print(dfsa.groupby(1)[2].mean())
#print(dfsa)
# df = pd.DataFrame(results_2opt)
# print(results_2opt)
# print (df)
# df = pd.DataFrame(results_2opt)
#
# da = df.groupby(['Nombre de ville']).mean()
# da = df.groupby([1945])
# da = df.mean(skipna = True)
# print(type(dfsa))
# print(type(results_2opt))
# np.split(a[:,1], np.unique(idx,return_index = True)[1][1:])
# print(da)






m5sa = pd.read_csv("../Datas/M5SA_datas.csv", sep=",", usecols=[1, 2])
m50sa = pd.read_csv("../Datas/M50SA_datas.csv", sep=",", usecols=[1, 2])
m500sa = pd.read_csv("../Datas/M500SA_datas.csv", sep=",", usecols=[1, 2])

m52opt = pd.read_csv("../Datas/M52OPT_datas.csv", sep=",", usecols=[1, 2])
m502opt = pd.read_csv("../Datas/M502OPT_datas.csv", sep=",", usecols=[1, 2])
m5002opt = pd.read_csv("../Datas/M5002OPT_datas.csv", sep=",", usecols=[1, 2])

m5samean = m5sa.mean(skipna = True)
m50samean = m50sa.mean(skipna = True)
m500samean = m500sa.mean(skipna = True)

m52optmean = m502opt.mean(skipna = True)
m502optmean = m502opt.mean(skipna = True)
m5002optmean = m5002opt.mean(skipna = True)


print(m50samean)



def graph_2opt():


    data = pd.read_csv('../Datas/QMG2OPT_datas.csv',usecols=[1, 2])
    data.head()

    axes = data.columns.drop("time")
    y = data.time
    x = data[axes]

    plt.plot(x, y)
    plt.grid()
    plt.title("Evolution du temps de traitement en fonction du nombre de villes (2-opt)", fontsize=10)
    plt.xlabel('villes')
    plt.ylabel('temps (s)')
    plt.show()



def graph_sa():


    data = pd.read_csv('../Datas/QMGSA_datas.csv',usecols=[1, 2])
    data.head()

    # Create y and X
    # créer y et X
    axes = data.columns.drop("time")
    y = data.time
    x = data[axes]


    plt.plot(x, y)
    plt.grid()
    plt.title("Evolution du temps de traitement en fonction du nombre de villes (Recuit simulé)", fontsize=10)
    plt.xlabel('villes')
    plt.ylabel('temps (s)')
    plt.show()


graph_sa()
graph_2opt()
