# NAMA  : Muthia Zhafira Sahnah
# NIM   : 24060122130071


def Pembagian (x,y) :
    if x == 0 and y == 0 :
        return ("Tak tentu")
    elif x == 0 :
        return 0
    elif y == 0 :
        return ("Tak hingga")
    elif y == 1 : 
        return x
    else :
        return 1 + Pembagian (x-y,y)

print (Pembagian(45,3))
print (Pembagian(35,7))
print (Pembagian(16,4))