import csv
fichier = open("testtext.txt",encoding='utf-8')

liste_wish = fichier.readlines()

with open('testtext.txt') as csv_file:
    #L'on ouvre en csv
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        #L'on lis les lignes
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\tThis url {row[0]} is {row[1]} and cost {row[2]}.')
            line_count += 1