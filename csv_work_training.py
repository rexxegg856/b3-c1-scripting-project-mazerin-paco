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
print(list_to_sort[1])
# /!\ Attention, ici j'ai une liste de 2264 entrées, par contre, chacune de ces entrées est une donnée str et non ...
#...une liste imbriquée comme je le voulais.
#Il faut que je transfome chacune de ces entrées en une nouvelle liste avec ; comme séparateur !

for position1 in range(len(list_to_sort)):
    list_to_sort[position1] = list_to_sort[position1].split(";")

#Suppression de toutes les lignes avec au moins une cellule vide :   

start_of_1range = 0
Not_out_of_range = True

while Not_out_of_range:
    reset_entire_for_loops = False
    for position1 in range(start_of_1range,len(list_to_sort)): 
        if reset_entire_for_loops == True: 							#Nous sortons ainsi de la 1ère boucle for.
            break    
        for position2 in range(len(list_to_sort[position1])):
            if (list_to_sort[position1][position2] == '') and (position1 == len(list_to_sort)-1):
               del list_to_sort[position1]					
               Not_out_of_range = False            
            elif list_to_sort[position1][position2] == '':
               del list_to_sort[position1]						#Suppression de l'entrée ne comprenant pas 5 cellules pleines.
               start_of_1range = position1						#Pour éviter de repartir de 0 à la première boucle for.
               reset_entire_for_loops = True							#Il nous faut réinitialiser la 1ère boucle for : 1ère étape, sortir de la 2ème boucle for.
               break
            elif position1 == len(list_to_sort)-1:
                Not_out_of_range = False

            
    
    
    
    
        
print(list_to_sort)

