import time
import codecs

print("Veuillez patienter (50 secondes environ), exécution du programme en cours ... ")
# lecture du fichier
#f = codecs.open("D:\Master 2 ILSEN 2022-2023\M2 - ILSEN\Applications d'Innovations\Sujet 4 - Génération de phrases\Projet/bigramme.bi", "r", "utf-8")
f = codecs.open("D:\Master 2 ILSEN 2022-2023\M2 - ILSEN\Applications d'Innovations\Sujet 4 - Génération de phrases\Projet/fichier_final.bi", "r", "utf-8")
# print(f.read()) 

# l'insérer dans un dictionnaire
start_time_dico = time.time()
dico_mots = {}
for ligne in f:
    mots = ligne.split()
    if mots[0] not in dico_mots:
        dico_mots[mots[0]] = [mots[1], int(mots[2])]
    elif dico_mots[mots[0]][1] < int(mots[2]):
        dico_mots[mots[0]][0] = mots[1]
        dico_mots[mots[0]][1] = int(mots[2])

end_time_dico = time.time()
execution_time = end_time_dico - start_time_dico
print("La création du dico s'est exécutée en ", execution_time, " secondes")

# Génération de la phrase
nb_mots = int(input("Saisir le nombre de mots pour générer une phrase : "))

#print(dico_mots)
cle = input("Saisir le premier mot : ")
phrase_generee = cle
start_time_phrase = time.time()
for i in range(nb_mots - 1):
    mot_suivant = dico_mots[cle][0]
    phrase_generee = phrase_generee + " " + dico_mots[cle][0]
    cle = mot_suivant
print("\nLa phrase générée est : ", phrase_generee, "\n")
end_time_phrase = time.time()
execution_time = end_time_phrase - start_time_phrase
print("La création de la phrase s'est exécutée en ", execution_time, " secondes")


