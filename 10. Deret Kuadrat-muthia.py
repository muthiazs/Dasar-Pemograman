# NAMA  : Muthia Zhafira Sahnah
# NIM   : 24060122130071


def DeretKuadrat (y) :
    if y == 1 :
        return 1
    else :
        return y*y + DeretKuadrat (y-1)

print (DeretKuadrat(3))
print (DeretKuadrat(4))
print (DeretKuadrat(1))