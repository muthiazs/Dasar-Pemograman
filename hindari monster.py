import ast
lol= ast.literal_eval(input())
batas = int(input())

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


hindarin_monster = [i for i in Wadah if i%batas !=0]
print(hindarin_monster)