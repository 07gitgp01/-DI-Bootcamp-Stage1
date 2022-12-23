print(f"\n\n\n{'='*100}\nExercice 1 : Bonjour Le Monde\n\n")

"""
Exercice 1 : Bonjour Le Monde
Des Instructions
Imprimez la sortie suivante dans une ligne de code :

Hello world
Hello world
Hello world
Hello world
"""
# Voir code ci-dessous:
print("Hello world\nHello world\nHello world\nHello world\nHello world")

##########################################################################
print(f"\n\n\n{'='*100}\nExercice 2 : Quelques Maths\n\n")

"""
Exercice 2 : Quelques Maths
Des Instructions
Ecrire un code qui calcule le résultat de : (99^3) * 8(99 à la puissance 3 fois 8)
"""

# Voir code ci-dessous:
rlt=(99**3)*8
rep = input("Voulez vous voir le résultat de (99**3)*8 ? : ")
while (rep.lower() == 'y' or rep.lower() == 'n' ):
    if (rep.lower() == 'y'):
        print(f"Le résultat est : {rlt}")
        break
    if (rep.lower() == 'n'):
        #print("Continuons alors\n")
        break
if not (rep.lower() == 'y' or rep.lower() == 'n' ):
    print("Entrez correctement la réponse\n")
    rep = input("Voulez vous voir le résultat de (99**3)*8 ?\n'Y' ou 'N' : ")



################################################################################
print(f"\n\n\n{'='*100}\nExrecice 3: Prédire le résultat des extraits de code suivants :\n\n")

#Exrecice 3: Prédire le résultat des extraits de code suivants :

print("\n>>> 5 < 3")
print("False\n\n")

print(">>> 3 == 3")
print("True\n\n")

print('>>> 3 == "3"')
print("False\n\n")

print('>>> "3" > 3')
print("TypeError\n\n")

print('>>> "Hello" == "hello"')
print("False")
    
###############################################################################
print(f"\n\n\n{'='*100}\nExercice 4 : Votre Marque D'ordinateur\n\n")

"""
Exercice 4 : Votre Marque D'ordinateur
Des Instructions
Créez une variable appelée computer_brand dont la valeur est le nom de marque de votre ordinateur.
À l'aide de la computer_brand variable, imprimez une phrase indiquant ce qui suit : "I have a <computer_brand> computer".
"""
# Voir code ci-dessous:
computer_brand="HP Celeron"
print(f'"I have a {computer_brand} computer"')

################################################################################"
print(f"\n\n\n{'='*100}\nExercice 5 : Vos Informations\n\n")

"""
Exercice 5 : Vos Informations
Des Instructions
Créez une variable appelée "name" et définissez sa valeur sur votre nom.
Créez une variable appelée "age" et définissez sa valeur sur votre âge.
Créez une variable appelée "shoe_size" et définissez sa valeur sur votre pointure.
Créez une variable appelée "info" et définissez sa valeur sur une phrase intéressante sur vous-même. 
    La phrase doit contenir toutes les variables créées dans les parties 1, 2 et 3.
Demandez à votre code d'imprimer le infomessage.
Exécutez votre code
"""
# Voir code ci-dessous:
name = "GUIGMA W.Paulin"
age = 24
shoe_size = 45
info = f"Moi je suis {name}, j'ai {24} ans.\nJe suis considéré comme le plus jeune âgé parmis tous\nmes promotionnaires et je fais {shoe_size} comme pointure niveau chaussure !"
print(info)

##############################################################################
print(f"\n\n\n{'='*100}\nExercice 6 : A & B\n\n")

"""
Exercice 6 : A & B
Des Instructions
Créez deux variables, aet b.
Chaque valeur de variable doit être un nombre.
Si aest plus grand alors b, faites imprimer votre code Hello World.
"""
# Voir code ci-dessous:
a=45
b=65
if (a<b):
    print("Hello World")
    
##############################################################################
print(f"\n\n\n{'='*100}\nExercice 7 : Pair Ou Impair\n\n")

"""
Exercice 7 : Pair Ou Impair
Des Instructions
Écrivez un code qui demande à l'utilisateur un nombre
et détermine si ce nombre est pair ou impair.
"""
# Voir code ci-dessous:
nombre = float(input("Entrez le nombre que vous voulez :\nnombre = "))
if (nombre % 2 == 0):
    print(f"**Le nombre {nombre} entré est PAIR !")
if not (nombre % 2 == 0):
    print(f"**Le nombre {nombre} entré est IMPAIR !")
    
##############################################################################
print(f"\n\n\n{'='*100}\nExercice 8 : Comment T'appelles-Tu ?\n\n")

"""
Exercice 8 : Comment T'appelles-Tu ?
Des Instructions
Écrivez un code qui demande à l'utilisateur son nom et détermine si 
vous avez le même nom ou non, imprimez un message amusant en 
fonction du résultat.
"""
# Voir code ci-dessous:
TonNom = input("Veuillez entrer votre nom USER !\nVotre nom est = ")
if (TonNom == "Paulin"):
    print(f"** Hii!! Vous avez le même nom que moi.")
    
if not (TonNom == "Paulin"):
    print(f"** Ouf!! Vous avez pas le même nom que moi, hii hii!!")

#####################################################################################
print(f"\n\n\n{'='*100}\nExercice 9 : Assez Grand Pour Faire Des Montagnes Russes\n\n")
"""
Exercice 9 : Assez Grand Pour Faire Des Montagnes Russes
Des Instructions
Écrivez un code qui demandera à l'utilisateur sa taille en pouces.
S'ils mesurent plus de 145 cm, imprimez un message indiquant qu'ils sont assez grands pour rouler.
S'ils ne sont pas assez grands, imprimez un message indiquant qu'ils doivent grandir un peu plus pour rouler.
"""
# Voir code ci-dessous:

Taille = 0
while (bool(Taille <= 0)):
    Taille = float(input("Entrez votre taille en pouce s'il vous plaît!\nVotre taille = "))
    
if ((Taille*2.54) > 145):
    print(f"** Vous êtes assez grand pour rouler .")
if not ((Taille*2.54) > 145):
    print(f"** Vous dever grandir un peu plus pour rouler.")