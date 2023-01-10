"""
DEFI: Instructions
Écrivez un programme qui accepte une séquence de mots séparés par des virgules en entrée et imprime les mots dans une séquence séparée par des virgules après les avoir triés par ordre alphabétique.
Utiliser la compréhension de liste
Exemple:

Supposons que l'entrée suivante soit fournie au programme : without,hello,bag,world
alors, la sortie doit être :bag,hello,without,world

"""
import re
#mot = input("\nEntrer la séquence de mots séparés par des virgules\nSéquence: ")
# word = sorted(re.findall(r"^(\s|\S)?[A-Za-z-_,]+(,\s|\S)?$", mot))
# print(word)

mot = sorted(input("\nEntrer la séquence de mots séparés par des virgules\nSéquence: ").split(","))
i=0
word=""
while i < len(mot):
    if i<len(mot)-1:
        word=word+mot[i]+","
        i+=1
    elif i == len(mot)-1:
        word=word+mot[i]
        i+=1
print("\n==>", word)
