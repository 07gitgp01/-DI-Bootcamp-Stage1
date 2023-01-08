print(f"\n\n\n{'='*100}\nExercise 1 : Convert Lists Into Dictionaries\n\n")
"""
🌟 Exercise 1 : Convert Lists Into Dictionaries
Instructions
Convert the two following lists, into dictionaries.
Hint: Use the zip method
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
"""
# Code ci-dessous
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(dict(zip(keys, values)))

#####################################################################################
print(f"\n\n\n{'='*100}\nExercice 2 : Cinémax\n\n")
"""
🌟 Exercice 2 : Cinémax
Des Instructions
Une salle de cinéma facture des prix de billets différents en fonction de l'âge d'une personne.
si une personne a moins de 3 ans, le billet est gratuit.
s'ils sont entre 3 et 12, le billet est de 10 $.
s'ils ont plus de 12 ans, le billet est de 15 $.

Soit l'objet suivant :

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

Combien chaque membre de la famille doit-il payer ?

Imprimez le coût total de la famille pour les films.
Bonus : Demander à l'utilisateur de saisir les noms et âges au lieu d'utiliser la familyvariable fournie ( Astuce : demander à l'utilisateur les noms et âges et les ajouter dans un familydictionnaire initialement vide).

"""
### Code ci-dessous
print("\n**********family = {'rick': 43, 'beth': 13, 'morty': 5, 'summer': 8}************\n")

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
def billetcinema(dictioname):
    billet = 0
    for i in dictioname.items():
        if (i[1] < 3):
            billet +=0
            print(f"\n{i[0]} doit payer 0$ !")
        elif (i[1] >= 3 and i[1] <= 12):
            billet += 10
            print(f"\n{i[0]} doit payer 10$ !")
            
        else:
            billet += 15
            print(f"\n{i[0]} doit payer 15$ !")
            
    # Le montant total à payer      
    print("\nLe montant total de vos tickets s'élève à ", billet,"$\n")

billetcinema(family) # Appel de la fonction

### Stocker les noms et les âges dans un dictio vide
print("\n*********COTE BONUS************\n")
familys = {}
membres = int(input("Entrez le nombre de membres de votre famille\nNombre = "))
for j in range(1, membres + 1):
    nom = input("\nVeuillez entrer votre nom\nVotre nom : ")
    age = int(input("\nVeuillez entrer votre âge\nVotre âge : "))
    familys[nom] = age
print("\nLa famille est ==>", familys)
billetcinema(familys) # Appel de la fonction

#####################################################################################
print(f"\n\n\n{'='*100}\nExercise 3: Zara\n\n")

"""
🌟 Exercise 3: Zara
Instructions
Here is some information about a brand.
name: Zara 
creation_date: 1975 
creator_name: Amancio Ortega Gaona 
type_of_clothes: men, women, children, home 
international_competitors: Gap, H&M, Benetton 
number_stores: 7000 
major_color: 
    France: blue, 
    Spain: red, 
    US: pink, green


2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
3. Change the number of stores to 2.
4. Print a sentence that explains who Zaras clients are.
5. Add a key called country_creation with a value of Spain.
6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
7. Delete the information about the date of creation.
8. Print the last international competitor.
9. Print the major clothes colors in the US.
10. Print the amount of key value pairs (ie. length of the dictionary).
11. Print the keys of the dictionary.
12. Create another dictionary called more_on_zara with the following details:

creation_date: 1975 
number_stores: 10 000


13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
14. Print the value of the key number_stores. What just happened ?
"""
###Code ci-dessous
### Creation du dictionnaire
brand = {
        'name': 'Zara', 
        'creation_date': 1975,
        'creator_name': 'Amancio Ortega Gaona',
        'type_of_clothes': ['men', 'women', 'children', 'home'],
        'international_competitors': ['Gap', 'H&M', 'Benetton'],
        'number_stores': 7000,
        'major_color': {'France': 'blue',
                        'Spain': 'red',
                        'US': ['pink', 'green']
                        }
        }

print("\nLE DICTIONNAIRE EST :\n\n",brand)

###3). Changer le store en 2
brand['number_stores'] = 2

###4). Les clients de ZARA
print("\nLes clients de ZARA sont ci-dessous :\n ")

j=1
for i in brand['type_of_clothes']:
    print("\t"*(j)+f"Les {i}\n")
    j+=1
    
### 5).
brand['country_creation'] = 'Spain'

###6).
if 'international_competitors' in brand.keys():
    brand['international_competitors'].append('Desigual')
#print(brand['international_competitors'])
#print(brand)

### 7).
del brand['creation_date']
#print(brand)

### 8).
print(f"\n Le dernier magasin de international_competitors est {brand['international_competitors'][-1]}")

### 9).
print(f"\n Le major color in US est {brand['major_color']['US']}")

### 10).
print(f"\n la longueur du dictionnaire est : {len(brand)}")

### 11).
print("\nLa liste des clés du dictionnaire brand est :\n==>",brand.keys())

### 12).
more_on_zara = {
                'creation_date': 1975, 
                'number_stores': 10000
                }
print("\nVoici la liste more_on_zara :\n==>",more_on_zara)

### 13).
brand.update(more_on_zara)
print("\nLe new dictionnaire est :\n", brand)

### 14).
print(f"\nThe store value est : {brand['number_stores']}")
print(f"\n\t***Il n'ya pas de rédondance des clés au niveau des dictionnaires, c'est donc ainsi l'ancien 'number_stores' \n\t   a été remplacé par le nouveau***")

#####################################################################################
print(f"\n\n\n{'='*100}\nExercise 4 : Disney Characters\n\n")
"""
Exercise 4 : Disney Characters
Instructions
Use this list :

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
Analyse these results :

#1/

>>> print(disney_users_A)
{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

#2/

>>> print(disney_users_B)
{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

#3/ 

>>> print(disney_users_C)
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
Only recreate the 1st result for:
The characters, which names contain the letter “i”.
The characters, which names start with the letter “m” or “p”.
"""
### Code ci-dessous
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

##1/
dic1 = dict(zip(users, list(range(5))))
print("\n", dic1)

##2/
dic2 = dict(zip(list(range(5)), users))
print("\n", dic2)

##3/
dic3 = dict(zip(sorted(users), list(range(5))))
print("\n",dic3)

##4/
liste1 = []
for i in users:
    if 'i' in i.lower():
        liste1.append(i)
print("\n",dict(zip(liste1, list(range(4)))))

##4/
liste2 = []
for i in users:
    if (i[0].lower() == 'm' or i[0].lower() == 'p'):
        liste2.append(i)
print("\n",dict(zip(liste2, list(range(4)))))



