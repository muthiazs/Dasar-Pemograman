import ast
lol= ast.literal_eval(input())

def is_list(s):
    return type(s) == list


Wadah = []

def Jumlah(x,y):
    for i in (x):
        if is_list(i):
            Jumlah(i, y)
        else:
            Wadah.append(i)

def IsPrima(n,i) :
  if (n < 2):
     return False
  if (n == 2):
      return True
  if (n % i == 0):
      return False
  if (i * i > n):
      return True
  else:
      return IsPrima(n, i + 1)

def is_prime(n):
  for i in range(3, n) and range(2,n):
    if n % i == 0:
      return False
    else:
      return True

Jumlah(lol, Wadah)
print(Wadah)

bilanganprima= [i for i in Wadah if IsPrima(i, 2)==True]
jumlahprima= sum(bilanganprima)

print(bilanganprima)
print(jumlahprima)


