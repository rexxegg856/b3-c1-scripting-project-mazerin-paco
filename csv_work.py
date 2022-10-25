
# #ouverture d'un fichier CSV...
# #... création de la liste des lignes nommée tableau...
# #... et affichage des lignes.
# import csv
# with open('conso-annuelles_v1.csv',newline='',encoding='latin-1') as f:    
#     reader = csv.reader(f)
#     for row in reader :
#         print(row)


#ouverture d'un fichier CSV...
#... création de la liste des lignes nommée tableau...
#... et affichage des lignes.
import csv
with open('conso-annuelles_v1.csv',newline='',encoding='latin-1') as f:         #Ouverture du fichier CSV
    tableau=[]
    lire=csv.reader(f)                            #chargement des lignes du fichier csv
    print('',end='\n')
    print('Affichage des lignes du tableau',end='\n')
    for ligne in lire:                            #Pour chaque ligne... 
        print(ligne, end='\n')                    #...affichage de la ligne dans la console ...
        tableau.append(ligne)                     #...on ajoute la ligne dans la liste ...
                                                  #...de liste nommée tableau