"""
1.) À l'aide de la "input" fonction, demandez à l'utilisateur une chaîne.
La chaîne doit comporter 10 caractères.
.S'il contient moins de 10 caractères, imprimez un message indiquant "chaîne pas assez longue".
.Si c'est plus de 10 caractères, imprimez un message indiquant "chaîne trop longue".

2.) Ensuite, imprimez le premier et le dernier caractère du texte donné.

3.) À l' aide d'un "for loop", construisez la chaîne caractère par caractère : imprimez le premier caractère, puis le deuxième, puis le troisième, jusqu'à ce que la chaîne complète soit imprimée. Par exemple:
The user enters "Hello World"
Then, you have to construct the string character by character
H
He
Hel
... etc
Hello World


4. Bonus : Échangez quelques caractères puis imprimez la nouvelle chaîne mélangée ( indice : regardez dans la shuffleméthode). Par exemple:

Hlrolelwod
"""
# Voir code ci-dessous:
import random # Module comportant la fonctionnalité "shuffle"

# déclarations des variables
taillecaracteres = 10
mot=""
motliste = []
motrecup = ""
motrecu = ""

### 1.)
while not (bool(len(mot) == taillecaracteres)):
    print("===================================================")
    mot = input(f"Entrez une chaine de caractères d'une taille de {taillecaracteres} caractères.\nVotre mot est : ")
    if (len(mot) < taillecaracteres):
        print(f'"Chaîne pas assez longue"\n')
        
    if (len(mot) > taillecaracteres):
        print(f'"Chaîne trop longue"\n')
        

### 2.)
if (True):
    print (f"\nLa première lettre de la chaine est <{mot[0]}> et la dernière lettre est <{mot[-1]}> !")

### 3.)
for nt in mot:
    motliste.append(nt)

for i in range(len(motliste)):
    motrecup += motliste[i]+" " 
    print(motrecup,"\n\n")
    
random.shuffle(motliste) # motliste sera mélangéé

for j in range(1, taillecaracteres + 1):
    motrecu += motliste[j - 1]+" " 
    print(motrecu)




