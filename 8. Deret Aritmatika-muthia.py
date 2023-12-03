# NAMA  : Muthia Zhafira Sahnah
# NIM   : 24060122130071


def DeretAritmatika (y) :
    if y == 0 :
        return 0
    else:
        return 3*y + DeretAritmatika (y-1)

print (DeretAritmatika(1))
print (DeretAritmatika(2))
print (DeretAritmatika(3))