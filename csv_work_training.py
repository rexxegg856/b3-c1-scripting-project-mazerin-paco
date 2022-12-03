#La librairie csv nous permettra de formater plus facilement le fichier csv
import csv

list_to_sort = []
#On ouvre le fichier qui nous intéresse et on l'enregistre sous la variable data_file :
with open("conso-annuelles_v1.csv") as data_file:
    data = csv.reader(data_file,delimiter = '\t') #...Création de l'objet csv.reader data...
    for row in data:                              #...L'argument du paramètre 'delimiter' est important...
        list_to_sort += row                       #...Sans lui les virgules rencontrées agiraient comme des séparateurs

#Affichage du fichier sous la forme d'une liste où chaque ligne du fichier csv est séparée par une virgule :
print(list_to_sort)
print(list_to_sort[18])
#Suppression de toutes les lignes avec au moins une cellule vide :
for position in range(len(list_to_sort)):
    if "" in list_to_sort[position]:
        list_to_sort.remove(list_to_sort[position])
print(list_to_sort)


