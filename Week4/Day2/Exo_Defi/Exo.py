
print(f"\n\n\n{'='*100}\nDéfi 1\n\n")
"""
Défi 1
Demandez à l'utilisateur un number et un length.
Créez un programme qui imprime une liste de multiples de number jusqu'à ce que la longueur de la liste atteigne length.
Exemples

number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]
"""
# Code ci-dessous:

nombre = int(input(f"Entrez un nombre  : "))
longueur = int(input(f"\nEntrez une longueur : "))
lmultiple = []
j = 1
for i in range(longueur):
    lmultiple.append(nombre*j)
    j +=1
print(f"\nnombre: {nombre} - longueur: {longueur} ➞  {lmultiple}")
  

#####################################################################################
print(f"\n\n\n{'='*100}\nDéfi 2\n\n")
"""
Défi 2
Écrivez un programme qui demande une chaîne à l'utilisateur et affichez une nouvelle chaîne avec toutes les lettres consécutives en double supprimées.
Exemples

user's word : "ppoeemm" ➞ "poem"

user's word : "wiiiinnnnd" ➞ "wind"

user's word : "ttiiitllleeee" ➞ "title"

user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
Remarques
Les chaînes finales n'incluront pas les mots avec des lettres doubles (par exemple « passant », « loterie »).
"""
# Code ci-dessous:
lchaine = []
motfinal = ""

chaine = input("Veuillez entrer votre chaine de cararactères:\nChaine : ")
for j in chaine:
    #nb=chaine.count(j)
    #print(f"{j} = {nb}")
    if j not in lchaine:
        lchaine.append(j)

for i in lchaine:
    motfinal += i
print("\nLe mot final est : ", motfinal)
