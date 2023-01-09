#####################################################################################
print(f"\n\n\n{'='*100}\nExercise 1 : What Are You Learning ?\n\n")
"""
Exercise 1 : What Are You Learning ?
Instructions
Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
Call the function, and make sure the message displays correctly.
"""
### Code ci-dessous:
"""
def display_message():
    print("\nWhat you are learning in this course?")
    
display_message()
"""
#####################################################################################
print(f"\n\n\n{'='*100}\nExercise 2: What’s Your Favorite Book ?\n\n")

"""
🌟 Exercise 2: What’s Your Favorite Book ?
Instructions
Write a function called favorite_book() that accepts one parameter called title.
The function should print a message, such as "One of my favorite books is <title>".
For example: “One of my favorite books is Alice in Wonderland”
Call the function, make sure to include a book title as an argument when calling the function.
"""
### Code ci-dessous:
"""
def favorite_book(title):
    print(f"\nOne of my favorite books is {title}")

favorite_book('Lords of Rings')
"""


#####################################################################################
print(f"\n\n\n{'='*100}\nExercise 3 : Some Geography\n\n")

"""
🌟 Exercise 3 : Some Geography
Instructions
Write a function called describe_city() that accepts the name of a city and its country as parameters.
The function should print a simple sentence, such as "<city> is in <country>".
For example “Reykjavik is in Iceland”
Give the country parameter a default value.
Call your function.
"""
### Code ci-dessous:
"""
def describe_city(city, country):
    print(f"\n{city} is in {country}")
describe_city('NewYork', 'USA')

def describe_citys(city, country = 'BURKINA FASO'):
    print(f"\n{city} is in {country}")
describe_citys('Ouagadougou')
"""
    
#####################################################################################
print(f"\n\n\n{'='*100}\nExercise 4 : Random\n\n")
"""
Exercise 4 : Random
Instructions
Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
"""
### Code ci-dessous:

import random as rd
"""while True:
    nbr = int(input("Entrer un nombre compris entre 1 et 100\nNombre: "))
    while nbr in range(1, 101):
        ran = rd.randrange(100)
        if nbr == ran:
            print(f"\nGreat ! Succed")
        else:
            print(f"\nNo match !, le mot secret était:  {ran}")
        break
    if not (nbr in range(1, 101)):
        continue
    break
"""  
#####################################################################################
print(f"\n\n\n{'='*100}\nExercise 5 : Let’s Create Some Personalized Shirts !\n\n")

"""
🌟 Exercise 5 : Let’s Create Some Personalized Shirts !
Instructions
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
Call the function make_shirt().

Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
Make a large shirt with the default message
Make medium shirt with the default message
Make a shirt of any size with a different message.

Bonus: Call the function make_shirt() using keyword arguments.
"""
###Code ci-dessous:
"""
# 1/
def make_shirt(size, text):
    print(f"\nThe size of the shirt is '{size}' and the text is '{text}'")

# 2/3/
make_shirt("XXL", " I'm a full-stack builder")

#4/
def make_shirts(size, text):
    if size == "Large":
        print(f"\nThe size of the shirt is '{size}' and the text is '{text}'")
    elif size == "Middle":
        print(f"\nThe size of the shirt is '{size}' and the text is '{text}'")
    else:
        make_shirt(size, text)
        
# 5/     
make_shirts(size = "Large", text = " I love Python ")

# 6/
make_shirts(size = "Middle", text = " I love Python ")

# 7/
make_shirts(size = "Small", text = " I love PhpMyAdmin ")
"""

#####################################################################################
print(f"\n\n\n{'='*100}\nExercise 6 : Magicians …\n\n")
"""
🌟 Exercise 6 : Magicians …
Instructions
Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
Call the function make_great().
Call the function show_magicians() to see that the list has actually been modified.
"""
## Code ci-dessous:
"""
# 1/
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# 2/
def show_magicians(s):
    for i in s :
        print("\n\t", i)
print("The magicians list below:")
show_magicians(magician_names)

# 3/
def make_great(s):
    for i in s:
        s[s.index(i)] = i+" the Great"

# 4/
print("======================================\nThe new list:")
make_great(magician_names)

# 5/
show_magicians(magician_names)
"""
#####################################################################################
print(f"\n\n\n{'='*100}\nExercise 7 : Temperature Advice\n\n")

"""
🌟 Exercise 7 : Temperature Advice
Instructions
Create a function called get_random_temp().
This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
Test your function to make sure it generates expected results.

Create a function called main().
Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
between 16 and 23
between 24 and 32
between 32 and 40

Change the get_random_temp() function:
Add a parameter to the function, named ‘season’.
Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
Now that we’ve changed get_random_temp(), let’s change the main() function:
Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
Use the season as an argument when calling get_random_temp().

Bonus: Give the temperature as a floating-point number instead of an integer.
Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.
"""
### Code ci-dessous:
# 1.1/
def get_random_temp():
    val = round(rd.uniform(-10, 40), 2)# pour le bonus 5/
    return val
    #print(val)
# 1.2/
get_random_temp()

# 2.1/
def main():
    tmp = get_random_temp()
    # 2.2/
    print(f"The temperature right now is {tmp} degrees Celsius.")
    # 3.1/
    if tmp < 0:
        print("\n Hrrrrrr ! Il gèle dehors")
    # 3.2/
    elif 0 <= tmp and tmp < 16:
        print("\nAssez froid ! N'oubliez pas votre manteau")
    # 3.3/
    elif 16 <= tmp and tmp <= 23:
        print("\nLe temps dehors est fréquentable !")
    # 3.4/
    elif 24 <= tmp and tmp < 32:
        print("\nIl fait un peu chaud aujourd'hui.")
    # 3.5/
    else:
        print("\nLa température est bien élévée ,mettez en marche votre climatisation")

# 4/
def get_random_temps(saison):
    val = round(rd.uniform(-10, 40), 2)
    #return val
    #if -10 <= val and val < 16:
    if (saison == 'hivers'):
        print("\nL'interval de température c'est entre -10 et 16")
    elif saison == 'printemps':
        print("\nL'interval de température c'est entre -16 et 23")
    elif saison == 'ete':
        print("\nL'interval de température c'est entre 24 et 32")
    elif saison == 'automne':
        print("\nL'interval de température c'est entre 32 et 40")
    else:
        print("\nVous avez entré une mauvaise saison !")

def mains():
    sai = input("\nEntrer la saison de votre choix!\nSaison: ").lower()
    get_random_temps(sai)
    # OR Le BONUS ci-dessous 6/
    mon = int(input("\nEntrer le numéro correspondant au mois de votre choix!\nMois: "))
    if mon in range(1, 4):
        get_random_temps('hivers')
    elif mon in range(4, 7):
        get_random_temps('printemps')
    elif mon in range(7, 10):
        get_random_temps('ete')
    elif mon in range(10, 13):
        get_random_temps('automne')
        
###### Execution des deux fonctions mains
main()
mains()   
