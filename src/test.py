import DataSetGenerator as dsg
import time
import ResolverAlgo as Ra
import numpy
import pandas as pd

for i in range (10, 1020, 50):



        start_time = time.time()
        i = dsg.random_symmetric_matrix(i)
        print(i)
        nb_city = len(i)
        print(nb_city)
        print('1st line : ')
        print(i[0])
        # Affichage du temps de generation
        generationTime = time.time() - start_time
        print("Temps de generation pour"+str(nb_city)+" villes : %s secondes ---" % generationTime)

        # on veut maintenant les envoyer dans le calcul du plus court chemin
        # Debut du decompte du temps
        start_timer = time.time()
        Ra.two_opt(i[0], i)
        # Affichage du temps d execution
        executionTime = time.time() - start_timer
        print("Temps d'execution pour"+ str(nb_city)+" villes : %s secondes ---" % executionTime)









