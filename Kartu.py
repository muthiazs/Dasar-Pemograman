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

Jumlah(lol, Wadah)
print(Wadah)
print(len(Wadah))