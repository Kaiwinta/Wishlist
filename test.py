import csv

def Savewishlist(nom,elements,titre):
    """
        Objectif:
            Créer un fichier txt contenant toutes les données 
            Sert aussi a update les wishlist
        Variables:
            nom = nom de la wishlist
            elements = nested list des données
            titre = titre des données
    """

    with open(f'{nom}.txt','w') as nom:
        nom.write(f'{titre[:]}\n')

        for i in range(len(elements)):
            nom.write(f'{elements[i]}\n')

def openWishlist(nom):

    with open(f'{nom}.txt') as csvfile:
        liste_wish = []
        csv_reader = csv.reader(csvfile, delimiter=',')
        for line in csv_reader:
            liste_wish.append(line)

    return liste_wish


nom = 'test3'

elements= [
    ["prix",'url',"nom"],
    ["p","url","nom"],
    ["p","url","nom"],
    ["p"]
    

]
titre   = ["prix obj","url","nom"]

Savewishlist(nom, elements , titre)

print(openWishlist(nom))