pekerjaan = list(map(int, input().split(' ')))
ganjil= [i for i in sorted(pekerjaan) if i%2==1]
genap= [ i for i in sorted(pekerjaan) if i%2==0]
pekerjaanganjil= list(reversed(ganjil))
pekerjaangenap= list(reversed(genap))
prioritaspekerjaan= pekerjaanganjil + pekerjaangenap

print(ganjil)
print(genap)
print(pekerjaanganjil)
print(pekerjaangenap)
print(prioritaspekerjaan)