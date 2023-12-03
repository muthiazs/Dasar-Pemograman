def konso(e, L):
    if L == []:
        return [e]
    else:
        return L + [e]

def firstElmt(L):
    return L[0]

def tail(L):
    return L[1:]

n = int(input())
L1 = [int(x) for x in input().split()]
L2 = [int(x) for x in input().split()]
L3= list()
L4= list()

def Tukerpermen(L1,L2,L3,L4):
    if firstElmt(L1)<firstElmt(L2):
        return konso(firstElmt(L2), L3) and konso(firstElmt(L1), L4)
        Tukerpermen(tail(L1), tail(L2), L3, L4)
    elif firstElmt(L1)>=firstElmt(L2):
        return konso(firstElmt(L1), L3) and konso(firstElmt(L2), L4)
    

BerapaTuker = 

print(Tukerpermen(L1, L2, L3, L4))
print(L3)
print(L4)
