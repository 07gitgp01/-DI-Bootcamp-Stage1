
""""
🌟 Exercise 1: Cats
Instructions
Using this class

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
Instantiate three Cat objects using the code provided above.
Outside of the class, create a function that finds the oldest cat and returns the cat.
Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
"""
### Code ci-dessous
"""
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
# 1/
first_cat = Cat('milou', 5)
second_cat = Cat('sym', 3)
third_cat = Cat('vox', 10)

# 2/
dic = dict(zip(['milou', 'sym', 'vox'], [5, 3, 10]))
#print(dic)

def incl(a):
    for i, j in dic.items():
        if a == j:
            #print(i," ", j)
            return (i, j)

def max(a, b):
    if a < b:
        return b
    else:
        return a
# 3/ 
rslt = incl(max(max(first_cat.age, second_cat.age), third_cat.age))
#print(rslt)
print(f"The oldest cat is {rslt[0]}, and is {rslt[1]} years old")
"""    

"""
🌟 Exercise 2 : Dogs
Instructions
Create a class called Dog.
In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
Create a method called bark that prints the following string “<dog_name> goes woof!”.
Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
Print the details of his dog (ie. name and height) and call the methods bark and jump.
Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
Print the details of her dog (ie. name and height) and call the methods bark and jump.
Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
"""
### Code ci-dessous:
"""
# 1/
class Dog:
    # 2/*
    def __init__(self, name, height):
        self.name = name
        self.height = height
    # 3/
    def bark(self):
        print(f"\n{self.name} goes woof!")
    # 4/
    def jump(self):
        print(f"\n{self.name} jumps {self.height*2} cm high!")
# 5/
davids_dog = Dog('Rex', 50)
# 6/
print(f"\n\nHis dog’s name is {davids_dog.name} and his height is {davids_dog.height} cm.")
davids_dog.bark() # ==> appel de bark()
davids_dog.jump() # ==> appel de jump()
print("\n\n")
# 7/
sarahs_dog = Dog('Teacup', 20)
# 8/
sarahs_dog.bark() # ==> appel de bark()
sarahs_dog.jump() # ==> appel de jump()
# 9/
if (davids_dog.height < sarahs_dog.height):
    print(f"\n{sarahs_dog.name} is bigger than {davids_dog.name} ")
elif (davids_dog.height > sarahs_dog.height):
    print(f"\n{davids_dog.name} is bigger than {sarahs_dog.name} ")
else:
    print(f"\n{davids_dog.name} is as bigger as {sarahs_dog.name} ")
    
"""



"""
🌟 Exercise 3 : Who’s The Song Producer?
Instructions
Define a class called Song, it will show the lyrics of a song.
Its __init__() method should have two arguments: self and lyrics (a list).
Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
Create an object, for example:

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


Then, call the sing_me_a_song method. The output should be:

There’s a lady who's sure
all that glitters is gold
and she’s buying a stairway to heaven
"""
### Code ci-dessous:
"""# 1/
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    # 2/
    def sing_me_a_song(self):
        for i in self.lyrics:
            print("\n", i)
# 3/
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()
"""


"""
Exercise 4 : Afternoon At The Zoo
Instructions
Create a class called Zoo.
In this class create a method __init__ that takes one parameter: zoo_name.
It instantiates two attributes: animals (an empty list) and name (name of the zoo).
Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
Create a method called get_animals that prints all the animals of the zoo.
Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
Example

{ 
    1: "Ape",
    2: ["Baboon", "Bear"],
    3: ['Cat', 'Cougar'],
    4: ['Eel', 'Emu']
}


Create a method called get_groups that prints the animal/animals inside each group.

Create an object called ramat_gan_safari and call all the methods.
Tip: The zookeeper is the one who will use this class.
Example
Which animal should we add to the zoo --> Giraffe
x.add_animal(Giraffe)
"""
### Code ci-dessous:
# 1/
class Zoo:
    # 2/
    def __init__(self, zoo_name):
        #self.animals = ["Ape","Baboon", "Bear",'Cat', 'Cougar','Eel', 'Emu']
        self.animals = []
        self.zoo_name = zoo_name
    # 3/
    def add_animal(self, new_animal):
        while new_animal.lower() not in self.animals:
            self.animals.append(new_animal.lower() )
        self.sortlist = sorted(self.animals)
    # 4/
    def get_animals(self):
        for ani in self.sortlist:
            print(f"\n", ani)
    # 5/
    def sell_animals(self, animal_sold):
        while animal_sold.lower() in self.animals:
            self.animals.remove(animal_sold.lower())
        self.sortlist = sorted(self.animals)
    # 6/
    def sort_animals(self):
        self.animalslist = []
        self.liste = []
        lettres=sorted({ x[0] for x in self.animals})
        for i in lettres:
            self.animalslist=[x  if x[0].lower()== i.lower() else None for x in self.sortlist]
            while None in self.animalslist:
                self.animalslist.remove(None)
            self.liste.append(self.animalslist)
        #print(self.liste)
        self.animalslists = dict(zip(range(1, len(self.liste)+1), self.liste))
        #print(self.animalslists)
    # 7/
    def get_groups(self):
        for i in self.animalslists.items():
            #print(f"\nGroup==>{i}:")
            #for j in i:
            print(f"\n\t{i[0]}: {i[1]}")

# 8/ Création de l'objet
ramat_gan_safari = Zoo('fasoparc')
    #### Ajout d'animaux
ramat_gan_safari.add_animal('Lion')
ramat_gan_safari.add_animal('lionne')
ramat_gan_safari.add_animal('Cougar')
ramat_gan_safari.add_animal('cat')
ramat_gan_safari.add_animal('Ape')
ramat_gan_safari.add_animal('lionceau')
ramat_gan_safari.add_animal('Giraffe')
ramat_gan_safari.add_animal('Yak')
ramat_gan_safari.add_animal('yak')
ramat_gan_safari.add_animal('epic porc')
ramat_gan_safari.add_animal('elephant')
ramat_gan_safari.add_animal('castor')
ramat_gan_safari.add_animal('agouti')
    ### Afficher toute la liste des animaux
print(f"\n***La liste des animaux apres ajout:")#, ramat_gan_safari.animals)
ramat_gan_safari.get_animals()
    ### Vendre des animaux (yak)
ramat_gan_safari.sell_animals('yak')
print(f"\n***La liste des animaux apres vente d'un 'yak':\n\t", ramat_gan_safari.sortlist)
    ### Ordonner la liste par ordre alphabetique
ramat_gan_safari.sort_animals()
    ### Afficher la liste par groupes
print(f"\n***Groupes=:")
ramat_gan_safari.get_groups()
  
            
    
                
                
                