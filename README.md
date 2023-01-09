# CERI_Innovations
Projet applications d'innovations

Ce dépot contient 3 fichiers :
- GAT & Hallucinations - Alexa STROZZI.pdf
Correspond à l'article, en pdf, rédigé pour ce projet 

- Article STROZZI Alexa - Application Innovation.rar
Correspond aux sources Latex d l'article ci-dessus

- Code du Projet Innovation - Défi 4 - Alexa STROZZI.rar 
Correspond au code source du projet
Ce fichier contient lui-même :
* Le fichier A_lire qui contient les explications ci-dessous

* Le fichier fusion_fichier.py permet de générer le fichier de bigramme qui a fusionné tous ceux du répertoire MEGALITE_FRANCAIS_bi

* Le fichier generateur_phrases existe en 2 versions. Il permet de gérérer une phrase de x mots (demandé lors de l'éxécution) à partir d'un mot de départ
Dans la version 1, on génére toujours la même phrase à partir du même mot de départ
Dans la version 2, La phrase varie d'une exécution à l'autre

Le code fonctionne si on enlève, dans le répertoire MEGALITE_FRANCAIS_bi, les 5 fichiers qui se trouvent dans le répertoire "Fichiers éccartés de MEGALITE" que j'ai mis dans le zip
Je n'ai pas mis le répertoire MEGALITE_FRANCAIS_bi ni le fichier fusionné car ils sont trop grop pour l'archive.

Il faut donc commencer par :
1 - Déziper ce fichier dans un répertoire qui contient lui même le répertoire MEGALITE_FRANCAIS_bi
2 - Enlever les 5 fichiers qui font planter le programme
3 - Exécuter en premier fusion_fichier.py
4 - Puis generateur_phrases_2.py
 
