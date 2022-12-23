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