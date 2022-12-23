"""
Exercice 8 : Comment T'appelles-Tu ?
Des Instructions
Écrivez un code qui demande à l'utilisateur son nom et détermine si 
vous avez le même nom ou non, imprimez un message amusant en 
fonction du résultat.
"""
# Voir code ci-dessous:

TonNom = input("Veuillez entrer votre nom USER !\nVotre nom est = ")
if (TonNom == "Paulin"):
    print(f"** Hii!! Vous avez le même nom que moi.")
    
if not (TonNom == "Paulin"):
    print(f"** Ouf!! Vous avez pas le même nom que moi, hii hii!!")
