print(f"\n\n\n{'='*100}\nExercice 1 : Set\n\n")
"""
Exercice 1 : Set
Des Instructions
Créez un ensemble appelé my_fav_numbers avec tous vos numéros favoris.
Ajoutez deux nouveaux numéros à l'ensemble.
Supprimez le dernier numéro.
Créez un ensemble appelé friend_fav_numbers avec les numéros favoris de votre ami.
Concaténer my_fav_numbers et friend_fav_numbers à une nouvelle variable appelée our_fav_numbers.
"""
### Code ci-dessous
my_fav_numbers = {'75 52 55 48', '66 05 21 48', '78 15 46 89'}
print("my_fav_numbers\:n",my_fav_numbers)

my_fav_numbers.add('64 09 57 71')
my_fav_numbers.add('60 32 39 45')
print("\nAjout de deux numeros à my_fav_numbers:\n", my_fav_numbers)

friend_fav_numbers = {'55 55 55 60', '66 66 66 20', '68 68 68 55', '56 62 62 62'}
print("\nfriend_fav_numbers:\n", friend_fav_numbers)

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("\nour_fav_numbers:\n", our_fav_numbers)

#####################################################################################
print(f"\n\n\n{'='*100}\nExercice 2 : Tuple\n\n")

"""
Exercice 2 : Tuple
Des Instructions
Étant donné un tuple dont la valeur est un entier, est-il possible d'ajouter plus d'entiers au tuple ?
"""
### Code ci-dessous

print("Étant donné un tuple dont la valeur est un entier, il \nn'est pas possible d'ajouter plus d'entiers au tuple")

#####################################################################################
print(f"\n\n\n{'='*100}\nExercice 3 : Liste\n\n")
"""
🌟 Exercice 3 : Liste
Des Instructions
Utilisation de cette listebasket = ["Banana", "Apples", "Oranges", "Blueberries"];
Supprimez "Banane" de la liste.
Supprimez « Blueberries » de la liste.
Ajoutez "Kiwi" à la fin de la liste.
Ajoutez « Pommes » au début de la liste.
Comptez combien de pommes il y a dans le panier.
Videz le panier.
Impression(panier)
"""
### Code ci-dessous
listebasket = ["Banana", "Apples", "Oranges", "Blueberries"]
print("listebasket:\n", listebasket)

listebasket.remove("Banana")#==>Supprimez "Banane" de la liste.
listebasket.remove("Blueberries")#==>Supprimez « Myrtilles » de la liste.
print("\nlistebasket après suppression de Banana et Blueberries:\n", listebasket)

listebasket.append('Kiwi')#==>Ajoutez "Kiwi" à la fin de la liste.
print("\nlistebasket après ajout de 'Kiwi' à la fin de la liste:\n", listebasket)

listebasket.insert(0,"Apples")#==>Ajoutez « Pommes » au début de la liste.
print("\nlistebasket après ajout de 'Apples' au début de la liste:\n", listebasket)

print("\nLe nombre de 'Apples' dans la liste est:\n", listebasket.count("Apples"))

listebasket.clear()
print("\nlistebasket après vidage du panier:\n", listebasket)

#####################################################################################
print(f"\n\n\n{'='*100}\nExercice 4 : Flotteurs\n\n")
"""
🌟 Exercice 4 : Flotteurs
Des Instructions
Récapitulatif - Qu'est-ce qu'un float? Quelle est la différence entre un entier et un flottant ?
Pouvez-vous penser à une autre façon de générer une séquence de flottants ?
Créez une liste contenant la séquence suivante 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (ne codez pas la séquence en dur).
"""
### Code ci-dessous
print("*Un float est un nombre à virgule.\nA la différence avec le float qui réserve beaucoup plus d'espace mémoire pour une variable donnée, un entier permet à une variable \nd'avoir un espace mémoire moins important.")
print("\n*Une autre façon de générer une séquence de flottants serait de faire une concaténation de la façon \nsuivante <float(str('partie entière'+'.'+'partie décimale'))>\nPar exemple : \n>>>float(str('25'+'.'+'05')) donne : 25.05")
# list = ['1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5']
# print("\n*La liste des flottants est :\n", list)
#####################################################################################
print(f"\n\n\n{'='*100}\nExercice 5 : Boucle For\n\n")
"""
🌟 Exercice 5 : Boucle For
Des Instructions
Utilisez une forboucle pour imprimer tous les nombres de 1 à 20 inclus.
En utilisant une forboucle, qui boucle de 1 à 20 (inclus), imprimez chaque élément qui a un index pair.
"""
### Code ci-dessous
for i in range(1, 21):
    print(i, "\n")

for i in range(1, 21):
    if (i % 2 == 0):
        print(f"{i} est d'index PAIR\n")

#####################################################################################
print(f"\n\n\n{'='*100}\nExercice 6 : Boucle While\n\n")
"""
🌟 Exercice 6 : Boucle While
Des Instructions
Écrivez une boucle while qui demandera continuellement à l'utilisateur son nom, à moins que l'entrée ne soit égale à votre nom.
"""
### Code ci-dessous

nom = None
while (bool(nom != "MOUSSA")):
    nom=input("\nEntrez votre nom svp (Le nom secret est 'MOUSSA')\nVotre nom = ")

if True:
    print("\nTROUVE !")

#####################################################################################
print(f"\n\n\n{'='*100}\nExercice 7 : Fruits Préférés\n\n")
"""
🌟 Exercice 7 : Fruits Préférés
Des Instructions
Demander à l'utilisateur de saisir son/ses fruit(s) préféré(s) (un ou plusieurs fruits).
Astuce : Utilisez la inputméthode intégrée. Demandez à l'utilisateur de séparer les fruits avec un seul espace, par ex. "apple mango cherry".
Stocker le(s) fruit(s) préféré(s) dans une liste (convertir la chaîne de mots en une liste de mots).
Maintenant que nous avons une liste de fruits, demandez à l'utilisateur d'entrer le nom de n'importe quel fruit.
Si l'entrée de l'utilisateur se trouve dans la liste des fruits favoris, écrivez « Vous avez choisi l'un de vos fruits préférés ! Prendre plaisir!".
Si l'entrée de l'utilisateur n'est PAS dans la liste, écrivez : « Vous avez choisi un nouveau fruit. J'espère que tu apprécies".
"""
### Code ci-dessous

listefruits = []
mes_fruits = input("Entrz vos fuits préférfés\nVos fruits sont : ")
res = mes_fruits.split()
print("La liste de vos fruits préférés:" + str(res))

nomfruit = input("Entrez le nom du fruit recherché\nNom du fruit : ")
if nomfruit in res:
    print("\nVous avez choisi l'un de vos fruits préférés ! Prendre plaisir!")
else:
    print("\nVous avez choisi un nouveau fruit. J'espère que tu apprécies")

#####################################################################################
print(f"\n\n\n{'='*100}\nExercice 8 : Qui A Commandé Une Pizza ?\n\n")
"""
Exercice 8 : Qui A Commandé Une Pizza ?
Des Instructions
Écrivez une boucle qui demande à un utilisateur d'entrer une série de garnitures de pizza, lorsque l'utilisateur saisit "quitter", arrêtez de demander des garnitures.
Au fur et à mesure qu'ils entrent chaque garniture, imprimez un message indiquant que vous ajouterez cette garniture à leur pizza.
À la sortie de la boucle, imprimez toutes les garnitures sur la pizza et quel est le prix total (10 + 2,5 pour chaque garniture).
"""
### Code ci-dessous

garn = ""
prix = 0
listgarn = []
while (bool(garn.lower() != "quitter")):

    garn = input("Entrez une garniture et ou taper 'quitter' si vous souhaitez abandonner\nVotre garniture : ")
    listgarn.append(garn)
    print("J'ajouterai cette garniture à votre pizza\n")
    
for i in range(len(listgarn)):
    prix += (10 + 2.5)
print("\n\nVoici la liste de vos garnitures\n", listgarn, "\nEt le prix total est de", prix)

#####################################################################################
print(f"\n\n\n{'='*100}\nExercice 9 : Cinémax\n\n")
"""
Exercice 9 : Cinémax
Des Instructions
Une salle de cinéma facture des prix de billets différents en fonction de l'âge d'une personne.
si une personne a moins de 3 ans, le billet est gratuit.
s'ils sont entre 3 et 12, le billet est de 10 $.
s'ils ont plus de 12 ans, le billet est de 15 $.
Demandez à une famille l'âge de chaque personne qui veut un billet.
Enregistrez le coût total de tous les billets de la famille et imprimez-le.

Un groupe d'adolescents vient dans votre salle de cinéma et souhaite regarder un film réservé aux personnes âgées de 16 à 21 ans.
Compte tenu d'une liste de noms, écrivez un programme qui demande à l'adolescent son âge, s'il n'est pas autorisé pour regarder le film, supprimez-les de la liste.
À la fin, imprimez la liste finale.
"""
### Code ci-dessous

billet = 0
membres = int(input("Entrez le nombre de membres de votre famille\nNombre = "))
for i in range(1, membres + 1):
    age = int(input("\nVeuillez entrer votre âge\nVotre âge : "))
    if (age < 3):
        billet +=0
    elif (age >= 3 and age <= 12):
        billet += 10
    else:
        billet += 15
print("\nLe montant total de vos tickets s'élève à ", billet,"$\n")


#### Goupes d'adolescents
listado = ['moussa', 'ali', 'rahim', 'paulin', 'Steve', 'Siméon']
listadocopy = []
listadocopy = listado.copy()
for nom in listadocopy:
    ages = int(input(f"Entrez votre âge\nVotre âge : "))
    if ( ages not in range(16, 22)):
        listado.remove(nom)

print("\n", listado)

#####################################################################################
print(f"\n\n\n{'='*100}\nExercice 10 : Commandes Sandwich\n\n")
"""
Exercice 10 : Commandes Sandwich
Des Instructions
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
Utilisez la liste ci-dessus appelée sandwich_orders.
Créez une liste vide appelée finished_sandwiches.
Au fur et à mesure que chaque sandwich est préparé, déplacez-le vers la liste des sandwichs finis.
Une fois que tous les sandwichs ont été préparés, imprimez un message répertoriant chaque sandwich qui a été préparé , tel que I made your tuna sandwich.
"""
### Code ci-dessous

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []
nt = 0
while (nt >= 0):
    if (nt == len(sandwich_orders) + 1):
        break
    
    sandwich = input("Quel est le plat qui est prêt?: ")
    if (sandwich in sandwich_orders):
        finished_sandwiches.append(sandwich)
        sandwich_orders.remove(sandwich)
        
    if (sandwich.lower() == "rien"):
        pass
    nt +=1

for word in finished_sandwiches:  
    print ("I made your ", word)

#####################################################################################
print(f"\n\n\n{'='*100}\nExercice 11 : Sandwich Orders#2\n\n")
"""
Exercice 11 : Sandwich Orders#2
Des Instructions
En utilisant la liste sandwich_ordersde l'exercice précédent, assurez-vous que le sandwich 'pastrami' apparaît dans la liste au moins trois fois.
Ajoutez du code au début de votre programme pour imprimer un message indiquant que la charcuterie n'a plus de pastrami, puis utilisez une whileboucle pour supprimer toutes les occurrences de 'pastrami' de sandwich_orders.
Assurez-vous qu'aucun sandwich au pastrami ne se retrouve dans finished_sandwiches.
"""
### Code ci-dessous
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich"]
finished_sandwiches = []
print("La charcuterie n'a plus de pastrami !")
while("Pastrami sandwich" in sandwich_orders):
    sandwich_orders.remove("Pastrami sandwich")
print("\nVoir liste :\n", sandwich_orders)


