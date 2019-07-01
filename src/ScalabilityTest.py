import DataSetGenerator as Dsg
import time
import ResolverAlgo as Ra


start_time = time.time()
#on recupere les matrices avec une grande difference de villes
matrice10 = Dsg.random_symmetric_matrix(10)
# Affichage du temps de generation
generationTime = time.time() - start_time
print("Temps de generation pour 10 villes : %s secondes ---" % generationTime)

start_time = time.time()
matrice100 = Dsg.random_symmetric_matrix(100)
# Affichage du temps de generation
generationTime = time.time() - start_time
print("Temps de generation pour 100 villes : %s secondes ---" % generationTime)

start_time = time.time()
matrice1000 = Dsg.random_symmetric_matrix(1000)
# Affichage du temps de generation
generationTime = time.time() - start_time
print("Temps de generation pour 1000 villes : %s secondes ---" % generationTime)


start_time = time.time()
matrice10000 = Dsg.random_symmetric_matrix(10000)
# Affichage du temps de generation
generationTime = time.time() - start_time
print("Temps de generation pour 10000 villes : %s secondes ---" % generationTime)



# TEST 1
#on veut maintenant les envoyer dans le calcul du plus court chemin
# Debut du decompte du temps
start_time = time.time()
Ra.two_opt(list(range(10)), matrice10)
# Affichage du temps d execution
executionTime = time.time() - start_time
print("Temps d'execution pour 10 villes : %s secondes ---" % executionTime)

# TEST 2 
start_time = time.time()
Ra.two_opt(list(range(100)), matrice100)
# Affichage du temps d execution
executionTime = time.time() - start_time
print("Temps d'execution pour 100 villes : %s secondes ---" % round(executionTime,3))

# TEST 3 
start_time = time.time()
Ra.two_opt(list(range(1000)), matrice1000)
# Affichage du temps d execution
executionTime = time.time() - start_time
print("Temps d'execution pour 1000 villes : %s secondes ---" % round(executionTime,3))

# TEST 4 
start_time = time.time()
Ra.two_opt(list(range(10000)), matrice10000)
# Affichage du temps d execution
executionTime = time.time() - start_time
print("Temps d'execution pour 10000 villes : %s secondes ---" % round(executionTime,3))


# Enfin on recupere les stats et on les envoie a la fonction de calcul de stat