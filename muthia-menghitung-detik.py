#Nama file:menghitung detik
#Pembuat: Muthia Zhafira Sahnah
#Tanggal: 3 September 2022
#Deskripsi: menghitung detik

#Definisi dan spesifikasi dari program menghitung detik adalah :
#berapa_detik : integer --> integer 
#berapa_detik mengubah waktu tersebut menjadi detik

#realisasi

def berapa_detik(h,m,s) :
     return (h*3600 + m*60 + s)
     
#aplikasi
print(berapa_detik(16, 7, 4))
