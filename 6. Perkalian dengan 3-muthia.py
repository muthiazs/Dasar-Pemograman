# NAMA  : Muthia Zhafira Sahnah
# NIM   : 24060122130071

def Perkalian_three (x) :
    if x == 0 :
        return 0
    elif x<0 :
        return Perkalian_three(x+1) - 3
    else :
        return Perkalian_three(x-1) + 3

print(Perkalian_three(18))
print(Perkalian_three(-8))
print(Perkalian_three(50))