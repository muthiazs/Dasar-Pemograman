#Nama file = cumlaude atau tidak cumlaude
#Pembuat: Muthia Zhafira Sahnah
#Tanggal: 3 September 2022
#Deskripsi: menentukan mahasiswa tersebut cumlaude atau tidak

#Definisi dan spesifikasi dari program cumlaude atau tidak adalah :
#cumlaude_tidakya : integer,real --> string
#cumlaude_tidakya mengetauhi mahasiswa tersebut cumlaude atau tidak dengan mengetauhi lama studi dan IPK 
#studi=x
#IPK=y
#jika true maka cumlaude, jika false maka tidak cumlaude 

def cumlaude_tidakya(x,y):
    if (x<=4.5 and y>=3.5):
        print("cumlaude")
    else: 
        print("tidak cumlaude")
      
#aplikasi
(cumlaude_tidakya(3.5, 4))
(cumlaude_tidakya(3.5, 2))
(cumlaude_tidakya(5, 2.5))

