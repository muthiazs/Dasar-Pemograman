# NAMA  : Muthia Zhafira Sahnah
# NIM   : 24060122130071


def DeretInteger (x) :
    if x == 1 :
        return 1
    else :
        return x + DeretInteger (x-1)

print (DeretInteger(4))
print (DeretInteger(3))
print (DeretInteger(2))