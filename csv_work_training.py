#La librairie csv nous permettra de formater plus facilement le fichier csv
import csv

list_to_sort = []
#On ouvre le fichier qui nous intéresse et on l'enregistre sous la variable data_file :
with open("conso-annuelles_v1.csv") as data_file:
    data = csv.reader(data_file,delimiter = '\t') #...Création de l'objet csv.reader data...
    for row in data:                              #...L'argument du paramètre 'delimiter' est important...
        list_to_sort += row                       #...Sans lui les virgules rencontrées agiraient comme des séparateurs

#Affichage du fichier sous la forme d'une liste où chaque ligne du fichier csv est séparée par une virgule :
print(len(list_to_sort))
print(list_to_sort)

# /!\ Attention, ici j'ai une liste de 2264 entrées, par contre, chacune de ces entrées est une donnée str et non ...
#...une liste imbriquée comme je le voulais.
#Il faut que je transfome chacune de ces entrées en une nouvelle liste avec ; comme séparateur !

for position1 in range(len(list_to_sort)):
    list_to_sort[position1] = list_to_sort[position1].split(";")

#Suppression de toutes les lignes avec au moins une cellule vide :   
#Gros soucis ici : la suppression d'entrées dans notre liste nous renvoie l'erreur : 'index : out of range'...
#...pour contourner ce problème j'ai dû faire intervenir une 3ème boucle : la boucle while.   
    
start_of_1range = 0
Not_out_of_range = True

while Not_out_of_range: 
    reset_entire_for_loops = False
    for position1 in range(start_of_1range,len(list_to_sort)): 
        if reset_entire_for_loops == True: 						#Nous sortons ainsi de la 1ère boucle for.
            break    
        for position2 in range(len(list_to_sort[position1])):
            if (list_to_sort[position1][position2] == '') and (position1 == len(list_to_sort)-1):
               del list_to_sort[position1]					
               Not_out_of_range = False            				#Suppression + sortie de la boucle while.
            elif list_to_sort[position1][position2] == '':
               del list_to_sort[position1]						#Suppression de l'entrée ne comprenant pas 5 cellules pleines.
               start_of_1range = position1						#Pour éviter de repartir de 0 à la première boucle for.
               reset_entire_for_loops = True					#Il nous faut réinitialiser la 1ère boucle for : 1ère étape, sortir de la 2ème boucle for.
               break
            elif position1 == len(list_to_sort)-1:
                Not_out_of_range = False						#Nous sortons de la boucle while et donc des 3 boucles.

            
print(len(list_to_sort))        
print(list_to_sort)


#Suppression des colonnes ID logement :

for position1 in range(len(list_to_sort)):
    del list_to_sort[position1][1]								#La colonne ID logement se trouve en deuxième position dans chacune des entrées de la liste,
                                                                #...d'où le [1].
    
print(len(list_to_sort))        
print(list_to_sort)


#Addition des consommations sur les deux années :
#1ère étape, remplacer la virgule par un point

start_of_range = 1												#On ne compte pas la première ligne : c'est le titre de chaque colonne.

for position1 in range(start_of_range, len(list_to_sort)):
    list_to_sort[position1][1] = list_to_sort[position1][1].replace(',','.')
    list_to_sort[position1][2] = list_to_sort[position1][2].replace(',','.').replace('-','0')  #Anticipation pour la 3ème étape '-' ==> '0'

print(len(list_to_sort))        
print(list_to_sort)
 
#3ème étape, convertir ces données de type string en type float

start_of_range = 1												#On ne compte pas la première ligne : c'est le titre de chaque colonne.

for position1 in range(start_of_range, len(list_to_sort)):
    list_to_sort[position1][1] = float(list_to_sort[position1][1])
    list_to_sort[position1][2] = float(list_to_sort[position1][2])
    
print(len(list_to_sort))        
print(list_to_sort)

#4ème étape, nous pouvons enfin additionner ces deux colonnes.