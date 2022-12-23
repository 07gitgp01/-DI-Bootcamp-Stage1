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
    