#Nama file = plat nomer ganjil genap
#Pembuat: Muthia Zhafira Sahnah
#Tanggal: 3 September 2022
#Deskripsi: menentukan plat nomer tersebut ganjil atau genap, apabila ganjil boleh lewat
#untuk menentukan sebuah plat nomer ganjil atau genap bisa melihat satu angka terakhir pada kendaraan mu

#Definisi dan spesifikasi dari program plat ganjil genap adalah :
#tahun kabisat : integer --> string
#program ini membuat kita tahu apakahkendaraan tersebut ganjil atau genap, jika ganjil maka boleh lewat jika genap tidak boleh lewat
#jika true maka tidak boleh lewat , jika false maka boleh lewat

#realisasi
def angkaterakhir_platnomer(x):
    if (x%2==0):
       print("kendaraan anda tidak boleh lewat")
    else:
        print("kendaraan anda boleh lewat")
#aplikasi
angkaterakhir_platnomer(6)
angkaterakhir_platnomer(5)
angkaterakhir_platnomer(8)
angkaterakhir_platnomer(7)