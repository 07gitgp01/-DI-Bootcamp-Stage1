#####################################################################################
print(f"\n\n\n{'='*100}\n🌟 Défi1 : Old MacDonald’s Farm\n\n")

"""
Instructions : Old MacDonald’s Farm
Take a look at the following code and output:
File: market.py

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
Output

McDonald's farm

cow : 5
sheep : 2
goat : 12

    E-I-E-I-0!


Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:

Create a class called Farm. How should it be implemented?
Does the Farm class need an __init__ method? If so, what parameters should it take?
How many methods does the Farm class need?
Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
Test your code and make sure you get the same results as the example above.
Bonus: nicely line the text in columns as seen in the example above. Use string formatting.

Agrandir La Ferme
Ajoutez une méthode appelée get_animal_types à la Farmclasse. 
Cette méthode doit renvoyer une liste triée de tous les types d'animaux (noms) de la ferme. Avec l'exemple ci-dessus, la liste devrait être : ['cow', 'goat', 'sheep'].

Ajoutez une autre méthode à la Farmclasse appelée get_short_info. Cette méthode doit renvoyer la chaîne suivante : "La ferme McDonald's possède des vaches, 
des chèvres et des moutons.". 
La méthode doit appeler la get_animal_typesfonction pour obtenir une liste des animaux.

"""
# Code ci-dessous:
#I
##1)
class Farm:
    #2)
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.reg = {}
        self.liste = []
        self.L = []

    # 3) Far a besoin de deux methodes  add_animal()  et   get_info()
    # 4) add_animal()  ne prendra qu'un seul parametre  *nom  en plus du self
    def add_animal(self,*nom):
        
        if len(nom)>1:
            if nom[0] not in self.reg.keys():
                #nom[0] = nom
                self.reg[nom[0]] = nom[1]
            else:
                self.reg[nom[0]] +=nom[1]
            

        elif len(nom) == 1:
            if nom[0] not in self.reg.keys():
                #nom[0] = nom
                self.reg[nom[0]] = 1
            else:
                self.reg[nom[0]] +=1
                

        
    def get_info(self):
        for i, j in self.reg.items():
            print(f"{i} : {j}")
        return f"\t\tE-I-E-I-0!"
    # II)
    #1)
    def get_animal_types(self):
        for i in self.reg.keys():
            self.liste.append(i)
        return sorted(self.liste)
    #2)
    def get_short_info(self):
        #L = get_animal_types()
        #print(self.liste)
        print(f"La ferme McDonaself.listed's possède des {self.liste[0]}s, des {self.liste[1]}s et des {self.liste[2]}s.")


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
#macdonald.get_info()
print(macdonald.get_info())
print(macdonald.get_animal_types())
#macdonald.get_short_info()
