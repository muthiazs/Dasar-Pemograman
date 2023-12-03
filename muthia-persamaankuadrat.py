#Nama file = jumlah kuadrat akar persamaan kuadrat
#Pembuat: Muthia Zhafira Sahnah
#Tanggal: 3 September 2022
#Deskripsi: mencari jumlah kuadrat akar2 persamaan kuadrat jika diketahui abc

#Definisi dan spesifikasi dari program jumlah_akarkuadrat adalah :
#jumlah_akarkuadrat : integer --> integer 
#jumlah_akarkuadrat menghitung jumlahan kuadrat dari akar-akar persamaan kuadrat (x1^2 + x2^2) tersebut jika diberikan nilai a, b, dan c. 

def x1_ditambah_x2(a,b,c):
    return (-b/a)
def x1_dikali_x2(a,b,c):
    return (c/a)
def jumlah_akarkuadrat(a,b,c):
    return (x1_ditambah_x2(a, b, c)*x1_ditambah_x2(a, b, c)- 2*x1_dikali_x2(a, b, c))

#aplikasi
print(jumlah_akarkuadrat(3,-36,30))
