# NAMA  : Muthia Zhafira Sahnah
# NIM   : 24060122130071


def DeretGeometri (x) :
    if x == 0 :
        return 0
    elif x==1 :
        return 1
    else :
        return 1 + 3*DeretGeometri(x-1)

print (DeretGeometri(4))
print (DeretGeometri(3))
print (DeretGeometri(2))