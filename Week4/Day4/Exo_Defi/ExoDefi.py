"""
Defi:Instructions
Soit une chaîne "Matrix":

    7i3
    Tsi
    h%x
    i #
    sM 
    $a 
    #t%
    ^r!

Decoder cette matrix
"""
from string import ascii_letters
### Code ci-dessous:
from string import ascii_letters

text = '7i3Tsih%xi #sM $a #t%^r!'
mot = ""
k = ""
line1 = []
line2 = []
line3 = []
matrix = list(text)
matrixi = []
for i in range(3):
    if i == 0:
        line1 = [matrix[j] for j in range(i, len(matrix), 3)]
        matrixi.append(line1)
    elif i == 1:
        line2 = [matrix[j] for j in range(i, len(matrix), 3)]
        matrixi.append(line2)
    else:
        line3 = [matrix[j] for j in range(i, len(matrix), 3)]
        matrixi.append(line3)
        
for i in matrixi:
    for j in range(len(i)):
        #k = matrixi[i]
        if i[j] in ascii_letters:
            mot +=i[j]
        else:
            if j == 0 or j == (len(i)-1):
                continue
            else:
                k = " "
            mot +=k
        

print("\nLe mot caché est: ", mot)
