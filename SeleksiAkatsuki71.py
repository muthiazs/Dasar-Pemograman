#Nama = Muthia Zhafira Sahnah 
#NIM = 24060122130071

#x integer <=100
x = int(input())
#list of integer 
nilaikandidat = list(map(int, input().split(' ')))
kandidatlolos = [i for i in nilaikandidat if i>x]
berapalolos = len(kandidatlolos)

print(berapalolos)




