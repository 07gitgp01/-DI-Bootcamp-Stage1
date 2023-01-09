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
text = '7i3Tsih%xi #sM $a #t%^r!'
mot = ""
line1 = []
line2 = []
line3 = []
matrix = list(text)
# for i in range(0, 8):
#     line1.append(matrix[i])
# for i in range(8, 16):
#     line2.append(matrix[i])
# for i in range(16, 24):
#     line3.append(matrix[i])
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
        


print(line1)
print(line2)
print(line3)
print(matrixi)
for i in matrixi:
    for j in matrixi[i]:
        k = matrixi[i]
        if j in ascii_letters:
            mot +=j
        else:
            while True:
                if k.index(j) == 0:
                    pass
                elif matrixi[i][k.index(j)+1] :
                    n=0


#print(block1)
