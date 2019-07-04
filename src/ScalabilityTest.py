import DataSetGenerator as dsg
import time
import ResolverAlgo as Ra
import Pcc_recuit as pcc
import csv


def scalability2opt():
    with open("../Datas/linearRegression2opt.csv", 'w+') as f:
        writer = csv.writer(f)
        header = ['', 'number', 'time']
        writer.writerow(header)
        k = 0

        for i in range(10, 1020, 50):
            j = i
            start_time = time.time()
            i = dsg.random_symmetric_matrix(i)
            nb_city = len(i)
            init_route = list(range(nb_city))
            # Affichage du temps de generation
            gen_time = time.time() - start_time
            # print("Temps de generation pour"+str(nb_city)+" villes : %s secondes ---" % gen_time)

            # on veut maintenant les envoyer dans le calcul du plus court chemin
            # Debut du decompte du temps
            start_timer = time.time()
            Ra.two_opt(init_route, i)
            # Affichage du temps d execution
            exec_time = time.time() - start_timer
            # print("Temps d'execution pour" + str(nb_city)+" villes : %s secondes ---" % exec_time)
            row = [k, j, exec_time]
            writer.writerow(row)
            print(row)
            k += 1


def scalabilitySA():
    with open("../Datas/linearRegressionSA.csv", 'w+') as f:
        writer = csv.writer(f)
        header = ['', 'number', 'time']
        writer.writerow(header)
        k = 0

        for i in range(10, 1020, 50):
            j = i
            start_time = time.time()
            i = dsg.random_symmetric_matrix(i)
            # Affichage du temps de generation
            gen_time = time.time() - start_time
            # print("Temps de generation pour"+str(nb_city)+" villes : %s secondes ---" % gen_time)

            # on veut maintenant les envoyer dans le calcul du plus court chemin
            # Debut du decompte du temps
            start_timer = time.time()
            datas = pcc.simulated_annealing(i)
            # Affichage du temps d execution
            exec_time = time.time() - start_timer
            # print("Temps d'execution pour" + str(nb_city)+" villes : %s secondes ---" % exec_time)
            row = [k, j, exec_time]
            writer.writerow(row)
            print(row)
            k += 1

scalability2opt()
scalabilitySA()