# CERI_Innovations
Projet applications d'innovations

Ce dépot contient 4 fichiers :
* Ce fichier README.md qui contient les explications ci-dessous

* Le fichier fusion_fichier.py permet de générer le fichier de bigramme qui a fusionné tous ceux du répertoire MEGALITE_FRANCAIS_bi

* Le fichier generateur_phrases existe en 2 versions. Il permet de gérérer une phrase de x mots (demandé lors de l'éxécution) à partir d'un mot de départ
Dans la version 1, on génére toujours la même phrase à partir du même mot de départ
Dans la version 2, La phrase varie d'une exécution à l'autre

Le code fonctionne si on enlève, dans le répertoire MEGALITE_FRANCAIS_bi, 5 fichiers corrompus à savoir : Keats,_John-La_veille_de_la_sainte_agnes=POESIA.pdf.seg.bi, Montesquieu,_Charles-Le_temple_de_gnide=POESIA.pdf.seg.bi, Verhaeren,_Emile-Les_heures_claires=POESIA.pdf.seg.bi, Verlaine,_Paul-Chansons_pour_elle=POESIA.pdf.seg.bi et Verlaine,_Paul-Les_poetes_maudits=POESIA.pdf.seg.bi

Je n'ai pas mis le répertoire MEGALITE_FRANCAIS_bi ni le fichier fusionné car ils sont trop grop pour l'archive.

Il faut donc commencer par :
1 - Copier ces fichiers dans un répertoire qui contient lui même le répertoire MEGALITE_FRANCAIS_bi
2 - Enlever les 5 fichiers de MEGALITE_FRANCAIS_bi qui font planter le programme
3 - Exécuter en premier fusion_fichier.py
4 - Puis generateur_phrases_2.py
 
