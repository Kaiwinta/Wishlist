import csv


with open('test2.txt') as csv_file, open("clone.txt",'w') as clone:
    
    #L'on ouvre en csv
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        #L'on lis les lignes
        clone.write(f'{row[0]},{row[1]},{row[2]}\n')
        if line_count == 0:
            
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]},{row[1]},{row[2]}')
            
            line_count += 1



def creerWishList(nom,elements,titre):
    """
        Objectif:
            Créer un fichier txt contenant toutes les données 
        Variables:
            nom = nom de la wishlist
            elements = nested list des données
            titre = titre des données
    """

    with open(f'{nom}.txt','w') as nom:
        nom.write(f'{titre[:]}\n')

        for i in range(len(elements)):
            nom.write(f'{elements[i]}\n')

nom = 'test3'

elements= [
    ["prix",'url',"nom"],
    ["p","url","nom"],
    ["p","url","nom"],
    ["p","url","nom"]

]
titre   = ["prix obj","url","nom"]

creerWishList(nom, elements , titre)