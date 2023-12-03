# NAMA  : Muthia Zhafira Sahnah
# NIM   : 24060122130071

def Pangkat (n,m) :
    if (m==0) :
        return 1
    else :
        return n * Pangkat (n,m-1)

print (Pangkat(2,8))
print (Pangkat(7,2))
print (Pangkat(3,4))