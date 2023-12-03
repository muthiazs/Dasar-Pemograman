#Nama:Muthia Zhafira Sahnah
#NIM: 24060122130071

def Perkalian (x,y) :
    if x == 1 :
        return y
    elif y == 1 :
        return x
    elif x == 0 or y == 0 :
        return 0
    else :
        return x + Perkalian(x, y-1)

print (Perkalian(2, 4))
print (Perkalian(4, 1))
print (Perkalian(0, 3))