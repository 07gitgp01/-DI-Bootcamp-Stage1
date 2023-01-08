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
# word = input(f"Entrer un nom\nNom: ")
# liste = []
# ilist = []
# dic = {}
# # for (ind, val) in enumerate(word):
# #     liste.append((ind, val))
# #     dic[]
# #     print(liste[list(ind)], liste[val])
    
#     #ilist.append(ind)
#     #print(ind, val)
# list1 = list(word)
# rep = []
# nt = 0
# for i in range(len(list1)):
#     #rep = [i]
#     #liste=[i]
#     #print(liste)
#     if not (list1[i] in dic.keys()):
#         dic[list1[i]] = [i]
#         #print(dic)
#         #rep = dic[list1[i]]
#         rep = [i-(nt-list1.index(list1[i]))]
#         #nt +=1
#     elif (list1[i] in dic.keys()):
#         dic[list1[i]] = rep
#     nt +=1
    
#     #ilist.append(list1[i])
# print(dic)

word = input("Entrez une chaine\nChaine: ")
mot=list(word)
i = 0
nb=len(mot)
dic= {}
while i<nb:
    if mot[i] in dic:
        for j in word:
            if j==mot[i]:
                n=word.index(j)
                liste.append(n) 
    else:
        liste=[]
        for j in word:
            if j==mot[i]:
                n=word.index(j)
                liste.append(n)
    dic.update({mot[i]:liste})
    i+=1
print(dic)
    
        

        

    


    


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