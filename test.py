
fichier = open("testtext.txt",encoding='utf-8')

liste_wish = fichier.readlines()

for i in range(len(liste_wish)-1):
    print(liste_wish[i][0])
fichier.close()