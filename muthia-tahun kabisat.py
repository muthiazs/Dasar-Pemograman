#Nama file = tahun kabisat
#Pembuat: Muthia Zhafira Sahnah
#Tanggal: 3 September 2022
#Deskripsi: mengecek apakah tahun tersebut tahun kabisat atau bukan

#Definisi dan spesifikasi dari program tahun kabisat adalah :
#tahun kabisat : integer --> string
#program ini membuat kita tahu apakah tahun yang diinput merupakan tahun kabisat atau bukan

#realisasi
def tahun_kabisat(tahun):
    if (tahun%400==0) or ((tahun%4==0) and (tahun%100 !=0)):
        print(str(tahun), "adalah tahun kabisat")
    else:
        print(str(tahun),"bukan tahun kabisat")

#aplikasi
tahun_kabisat(2004)
tahun_kabisat(2003)
tahun_kabisat(1600)
tahun_kabisat(1999)
