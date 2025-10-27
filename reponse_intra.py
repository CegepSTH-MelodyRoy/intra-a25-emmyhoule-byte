##########################################
# Houle,Emmy, <6286591>
##########################################
#Question 1: Température
import random
def question_1():
    for jour in range(1,10+1):
        temperature = round(random.uniform(20, 35), 1)
        print("Jour",jour,":",temperature)
        if temperature < 24:
            print("Trop froid")
        elif temperature > 30:
            print("Trop chaud")
        else:
            print("Ok")
    print("Fin")

question_1()

#Question 2: Population bactérienne
import matplotlib.pyplot as plt
import numpy as np

def question_2():
    nb_bacterie = int(input("Quelle est la population de bactérie initiale:"))
    #Initialement le temps est à zéro
    heure = 0
    # Création du graphique de croissance bactérienne
    plt.figure(figsize=(10,10))
    plt.xlabel("Heures")
    plt.ylabel("Population")
    plt.title("Croissance bactérienne")
    while heure <=10:
        nb_bacterie = float(nb_bacterie * (np.pi/1.5))
        plt.plot([heure],[nb_bacterie],"*b")
        heure += 1
    plt.plot([0,10],[50000,50000],"r--")
    plt.grid()
    plt.show()
#je n'arrive pas à mettre la graduation de l'axe des y exactement comme dans l'exemple d'affichage, mais tout le reste est présent
question_2()











