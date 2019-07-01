import DataSetGenerator as Dsg
import time


#on recupere les matrices avec une grande difference de villes
matrice10 = Dsg.random_symmetric_matrix(10)
matrice100 = Dsg.random_symmetric_matrix(100)
matrice1000 = Dsg.random_symmetric_matrix(1000)

#on veut maintenant les envoyer dans le calcul du plus court chemin
# Debut du decompte du temps
start_time = time.time()

# Mettre code ICI

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))



#Enfin on recupere les stats et on les envoie a la fonction de calcul de stat
