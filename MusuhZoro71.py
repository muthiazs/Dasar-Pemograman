#Nama = Muthia Zhafira Sahnah 
#NIM = 24060122130071

kekuatan = [int(x) for x in input().split()]
Musuh = sorted(kekuatan)

def MusuhZoro(Musuh):
    return Musuh[3]

print(kekuatan)

print(MusuhZoro(Musuh))

