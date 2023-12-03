#Muthia Zhafira Sahnah
#24060122130071
def NamaSamaran(nama1,nama2):
    return (nama2[0] + nama1[1:] + " " + nama1[0] + nama2[1:])
namaAsli= input(str())
nama = namaAsli.split(' ')
nama1= nama[0]
nama2= nama[1]

print(nama1)
print(nama2)
print(NamaSamaran(nama1, nama2))