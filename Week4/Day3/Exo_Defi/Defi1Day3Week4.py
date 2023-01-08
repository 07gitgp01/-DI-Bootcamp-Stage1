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

