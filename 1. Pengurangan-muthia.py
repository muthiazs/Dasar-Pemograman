# NAMA  : Muthia Zhafira Sahnah
# NIM   : 24060122130071

def Pengurangan (x,y) :
    if y == 0 :
        return x
    else :
        return Pengurangan (x,y-1) - 1

print (Pengurangan(27,17))
print (Pengurangan(18,6))
print (Pengurangan(6,7))