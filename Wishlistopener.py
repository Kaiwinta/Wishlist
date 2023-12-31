from csv import reader
from os import listdir, rename, remove
"""
This is the logical part of the projekt:

The goal here is to deal only with list and files
    We muss turn a list into a certain files
    Or Open a file and extract dat in a list

    Or Find all the files in a specific folder(wishlist)

No tkinter are involved here, the tk part is in main.py and will call those functions
"""


def Savewishlist(nom,elements):
    """
        Objectif:
            Créer un fichier txt contenant toutes les données 
            Sert aussi a update les wishlist
        Variables:
            nom = nom de la wishlist
            elements = nested list des données
    """

    with open(f'wishlist/{nom}.txt', 'w') as file:
        for sublist in elements:
            file.write(','.join(sublist) + '\n')  # Write each element of the sublist separated by commas

def openWishlist(nom):
    """
        Objectif:
            Renvoie une liste utilisable en python 
            Cette liste contient tout les élements d'un fichier txt
    """
    with open(f'wishlist/{nom}') as csvfile:
        liste_wish = []
        csv_reader = reader(csvfile, delimiter=',')
        for line in csv_reader:
            liste_wish.append(line)

    return liste_wish

def getwishlistname():
    """
        Objectif:
            Renvoyer la liste de tout les fichier présent dans le dossier wishlist
    """
    
    liste_files = []
    dir = "wishlist"
    for path in listdir(dir):
        #Os.listdir permet de lister les fichier a partir d'un certain path (dans notre cas wishlist)
        liste_files.append(path)
    return liste_files

def change_Wishlist_name(new, old):
    rename(f'wishlist/{old}',f'wishlist/{new}')

def delete_Wishlist(name):
    remove(f'wishlist/{name}')

