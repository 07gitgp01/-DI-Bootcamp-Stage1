list1 = [5, 10, 15, 20, 25, 50, 20]

for i in range(len(list1)):
    for j in range(i,len(list1)):
        if (list1[j] == list1[i]):
            list1[i]=200
            break
    
    break
       
       
####### Ci-dessous est le reste du code de l'Exo2 XP day1 du WEEK4
"""
rep = input("Voulez vous voir le résultat de (99**3)*8 ? \n'y' ou 'n' : ")
while (rep.lower() == 'y' or rep.lower() == 'n' ):
    if (rep.lower() == 'y'):
        break
    if (rep.lower() == 'n'):
        #print("Continuons alors\n")
        break
if not (rep.lower() == 'y' or rep.lower() == 'n' ):
    print("Entrez correctement la réponse\n")
    rep = input("Voulez vous voir le résultat de (99**3)*8 ?\n'Y' ou 'N' : ")
"""
