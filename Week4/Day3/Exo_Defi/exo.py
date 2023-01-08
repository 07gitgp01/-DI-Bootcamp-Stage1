"""
Instructions
Défi 1
Demander un mot à un utilisateur
Écrivez un programme qui crée un dictionnaire. Ce dictionnaire stocke les index de chaque lettre dans une liste.

Assurez-vous que les lettres sont les clés.
Assurez-vous que les lettres sont des chaînes.
Assurez-vous que les index sont stockés dans une liste et que ces listes sont des valeurs.
Exemples

"dodo" ➞ { "d": [0, 2], "o": [1, 3] }

"froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }

"grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}

""" 
### Code ci-dessous:
print("************************ DEFI1 *********************************")
dic1 = {}
dic2 = {}
word = input("Entrez une chaine de caractère\nChaine: ")
for ind, val in enumerate (word):
    if not (val in dic1.keys()):
        dic1[val] = [ind]
        dic2[val] = [ind]
    elif (val in dic1.keys() and val in dic2.keys()):
        dic1[val] = dic2[val]+[ind]
        dic2[val] += [ind] 
    else:
        continue
print(dic1)
        


"""
Défi 2
Créez un programme qui imprime une liste des articles que vous pouvez acheter dans le magasin avec l'argent que vous avez dans votre portefeuille.
Triez la liste par ordre alphabétique.
Renvoyez "Rien" si vous ne pouvez rien acheter du magasin.
Exemples

The key is the product, the value is the price

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"

➞ ["Bread", "Fertilizer", "Water"]

items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100" 

➞ ["Apple", "Bananas", "Fan", "Honey", "Pan", "Spoon"]

items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$1" 

➞ "Nothing"
"""
###Code ci-dessous:




### Defi 2
print("********************************** DEFI 2****************************\n\n*************************** WELCOME INTO OUR CHOP *********************")

items_Block1 = {
  "Water": "1",
  "Bread": "3",
  "TV": "1000",
  "Fertilizer": "20"
}

items_Block2 = {
  "Apple": "4",
  "Honey": "3",
  "Fan": "14",
  "Bananas": "4",
  "Pan": "100",
  "Spoon": "2"
}

items_Block3 = {
  "Phone": "999",
  "Speakers": "300",
  "Laptop": "5000",
  "PC": "1200"
}

Monwallet = input(f"Entrez la somme de votre portefeuille\nsomme: ")
liste1 = []
liste2 = []
liste3 = []
choix = 1
while ( choix == 1 or choix == 2 or choix == 3 or choix == 0):
    choix = int(input("\nEntrer un choix\n\t\t'1' ==> pour le block1\n\t\t'2' ==> pour lr block2\n\t\t'3' ==> pour le block3\n\t\t'0' pour quitter\nChoix: "))
    while (choix == 1):
        for prod, prix in items_Block1.items():
            if (int(Monwallet) >= int(prix)):
                liste1.append(prod)
            else:
                continue
        if liste1 == []:
            print("\nRien!")
        else:
            print(f"\nLa liste disponible pour vous dans Block1==>", liste1)  
        break

    while (choix == 2):
        for prod, prix in items_Block2.items():
            if (int(Monwallet) >= int(prix)):
                liste2.append(prod)
            else:
                continue
        if liste2 == []:
            print("\nRien!")
        else:
            print(f"\nLa liste disponible pour vous dans Block1==>", liste2)
        break

    while (choix == 3):
        for prod, prix in items_Block3.items():
            if (int(Monwallet) >= int(prix)):
                liste3.append(prod)
            else:
                continue
        if liste3 == []:
            print("\nRien!")
        else:
            print(f"\nLa liste disponible pour vous dans Block1==>", liste3)
        break

    if (choix == 0):
        break

