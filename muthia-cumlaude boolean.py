#Nama file = cumlaude atau tidak cumlaude
#Pembuat: Muthia Zhafira Sahnah
#Tanggal: 3 September 2022
#Deskripsi: menentukan mahasiswa tersebut cumlaude atau tidak

#Definisi dan spesifikasi dari program cumlaude atau tidak adalah :
#cumlaude_tidakya : integer,real --> boolean
#cumlaude_tidakya mengetauhi mahasiswa tersebut cumlaude atau tidak dengan mengetauhi lama studi dan IPK 

#studi=x
#IPK=y

def cumlaude_tidakya(x,y):
    return (x<=4.5 and y>=3.5)
       
#aplikasi
print (cumlaude_tidakya(3.5, 4))
print (cumlaude_tidakya(5, 3))
print (cumlaude_tidakya(4, 4))