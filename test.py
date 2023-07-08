import csv

def Savewishlist(nom,elements):
    """
        Objectif:
            Créer un fichier txt contenant toutes les données 
            Sert aussi a update les wishlist
        Variables:
            nom = nom de la wishlist
            elements = nested list des données
    """

    with open(f'{nom}.txt', 'w') as file:
        for sublist in elements:
            file.write(','.join(sublist) + '\n')  # Write each element of the sublist separated by commas

def openWishlist(nom):

    with open(f'{nom}.txt') as csvfile:
        liste_wish = []
        csv_reader = csv.reader(csvfile, delimiter=',')
        for line in csv_reader:
            liste_wish.append(line)

    return liste_wish



nom = 'test3'

elements= [
    ["prix obj","url","nom"],
    ["prix",'url',"nom"],
    ["p","url","nom"],
    ["p","url","nom"],
    ["p","url",'nom']
    

]
nom2 = 'test5'

Savewishlist(nom2, elements)

liste = openWishlist(nom)

Savewishlist(nom, liste)
print(liste)
