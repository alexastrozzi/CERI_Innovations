import codecs # pour le formatage UTF8 lors de la lecture des fichiers
import os # pour accéder aux ressources FS
import glob # pour créer une liste avec le nom des fichiers FS
import time

start_time = time.time()
print("Veuillez patienter, programme en cours d'exécution ...")
# on va obtenir 30 millions de bigrammes
# vérifier qu'il n'y ait pas de doublons dans les bigrammes

# on se positionne dans le répertoire où se trouvent tous les fichiers contenant les bigrammes
# on a commencé par faire des tests avec un répertoire contenant peu de bigrammes pour tester le programme plus rapidement
# dossier_a_fusionner = "D:\Master 2 ILSEN 2022-2023\M2 - ILSEN\Applications d'Innovations\Sujet 4 - Génération de phrases\Projet/test_dossiers"
# mais le vrai dossier à fusionner est 'MEGALITE_FRANCAIS_bi'
dossier_a_fusionner = "D:\Master 2 ILSEN 2022-2023\M2 - ILSEN\Applications d'Innovations\Sujet 4 - Génération de phrases\Projet/MEGALITE_FRANCAIS_bi"
os.chdir(dossier_a_fusionner)

# la liste de tous les dossiers contenant les fichiers à examiner
liste_dossiers = []
for path, dirs, files in os.walk(os.getcwd()):
    for dir in dirs:
        liste_dossiers.append(dir)
# print("Liste des répertoires à parcourir : ", liste_dossiers)
# print("Nous somme actuellement dans le dossier : =>> ", os.getcwd())

# dictionnaire de tous les bigrammes que l'on va trouver dans les fichiers
dico_bigrammes = {}
for dir in liste_dossiers:
    os.chdir(os.getcwd() + '/' + dir)
    #print("le dossier courant est =>>", os.getcwd())
    liste_fichiers = glob.glob("*.bi")
    #print("liste de fichiers : ", liste_fichiers)
    for un_fichier in liste_fichiers:
        #print(un_fichier)
        # ce print pour aider à la détectio des 5 fichiers qui posaient problèmes 
        with codecs.open(un_fichier, 'r', 'utf8') as fichier_in:
            # il faut ignorer les 2 premières lignes qui ne contiennent pas de bigrammes
            next(fichier_in)
            next(fichier_in)
            # puis on récupère toutes les autres lignes
            toutes_les_lignes = fichier_in.readlines()
            for une_ligne in toutes_les_lignes:
                ligne_split = une_ligne.split()
                # la clé du dictionnaire est le bigramme sous forme de tuple
                cle = (ligne_split[0], ligne_split[1])
                if cle not in dico_bigrammes:
                    dico_bigrammes[cle] = int(ligne_split[2])
                else:
                    dico_bigrammes[cle] += int(ligne_split[2])
            # print("Dico bigramme en cours : ", dico_bigrammes)
        fichier_in.close()
    os.chdir('..')
    # print("Dico bigramme final : ", dico_bigrammes)

# puis écrire cette liste dans un fichier final
fichier_final = codecs.open("D:\Master 2 ILSEN 2022-2023\M2 - ILSEN\Applications d'Innovations\Sujet 4 - Génération de phrases\Projet/fichier_final.bi", "w", "utf-8")
for cle, valeur in dico_bigrammes.items():
    nouvelle_ligne = cle[0] + " " + cle[1] + " " + str(valeur) + "\n"
    fichier_final.write(nouvelle_ligne)
fichier_final.close()
end_time = time.time()
execution_time = end_time - start_time
print("Le programme s'est exécuté en ", execution_time, " secondes")
print("Pour ", len(dico_bigrammes), " bigrammes")