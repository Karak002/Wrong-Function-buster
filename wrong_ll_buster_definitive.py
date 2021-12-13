import os
import re
from cfonts import render, say
from termcolor import colored, cprint

output = render('Wrong LL Buster', colors=['red', 'yellow'], align='center')
print(output)

class Errore:
    def __init__(self, key, numero_riga, nome_file):
        self.key = key
        self.numeroriga = numero_riga 
        self.nomefile = nome_file



keyConfronto = []


llinphp = []

with open('traduzioni.txt', 'r') as f:

    for line in f:
        match = re.search("'([^']*)'", line)
        if(match != None):
            keyConfronto.append(match.group(1))
        else:
            continue


regexWithDoubleQuotes = '(?<=ll\(\').+(?=\'\))'
regexWithSingleQuotes = '(?<=ll\(\").+(?=\"\))'

numero_riga= 0;
titolo_file = ''

directory_folder = input('Inserisci il percorso della cartella che contiene i file php da controllare: ')

Path = directory_folder + '/'
filelist = os.listdir(Path)
print(f'Sto controllando nei seguenti file: {filelist}')
for i in filelist:

    if i.endswith(".php"):  # You could also add "and i.startswith('f')
        with open(Path + i, 'r') as f:
            for line in f:
                numero_riga +=1
                try:
                    match = re.search(regexWithDoubleQuotes, line)
                    if(match != None):
                        llinphp.append(Errore(match.group(0), numero_riga, i))
                    else:
                        match = re.search(regexWithSingleQuotes, line)
                        if(match != None):
                            llinphp.append(Errore(match.group(0), numero_riga, i))
                except:
                    print('Inserimento fallito')
            numero_riga = 0

error_check = False

for traduzione in llinphp:
        if(traduzione.key not in keyConfronto):
            # cprint('OK ESISTE, ' + ' ' + traduzione.key, color='green')
            cprint('NON ESISTE' + ' ' + '-'+traduzione.key+'-' + ' Sulla riga numero: ' + str(traduzione.numeroriga) + ' Nel file: ' + traduzione.nomefile, color='red')
            error_check = True
if(error_check == False):
    cprint('Non ci sono errori', color='green')
