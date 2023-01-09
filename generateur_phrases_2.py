import time
import codecs
import random

def creation_graphe_mots():
    start_time = time.time()
    f = codecs.open("D:\Master 2 ILSEN 2022-2023\M2 - ILSEN\Applications d'Innovations\Sujet 4 - Génération de phrases\Projet/fichier_final.bi", "r", "utf-8")
    # on va insérer les bigrammes dans un dictionnaire de distionnaire
    graph_mots = {}
    for ligne in f:
        mots = ligne.split()
        if mots[0] not in graph_mots:
            graph_mots[mots[0]] = {mots[1] : int(mots[2])}
        else:
            if mots[1] not in graph_mots[mots[0]]:
                graph_mots[mots[0]][mots[1]] = int(mots[2])
            else:
                graph_mots[mots[0]][mots[1]] += int(mots[2])
    end_time = time.time()
    execution_time = end_time - start_time
    print("La création du graphe s'est exécutée en ", execution_time, " secondes")
    return graph_mots

def generation_phrase(graph_mots, nb_mots, cle):
    start_time = time.time()
    phrase_generee = cle
    for i in range(nb_mots - 1):
        hasard = random.randint(0, len(graph_mots[cle])-1)
        mot_suivant = list(graph_mots[cle])[hasard]
        phrase_generee = phrase_generee + " " + mot_suivant
        cle = mot_suivant
    end_time = time.time()
    execution_time = end_time - start_time
    print("La création de la phrase s'est exécutée en ", execution_time, " secondes")
    return phrase_generee


print("Veuillez patienter (50 secondes environ), exécution du programme en cours ... ")
mon_graphe = creation_graphe_mots()
mon_nb_mots = int(input("Saisir le NOMBRE de mots que l'on veut générer pour une nouvelle phrase : "))
ma_cle = input("Saisir le premier MOT : ")
print("\nLa phrase générée est : ", generation_phrase(mon_graphe, mon_nb_mots, ma_cle), "\n")
