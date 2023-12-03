#Nama = Muthia Zhafira Sahnah 
#NIM = 24060122130071

BanyakKegiatan = int(input())

kegiatanTobi =[]
daftarKegiatan = 0

if BanyakKegiatan>=1 and BanyakKegiatan<=50:
     for i in range(BanyakKegiatan):
       Kegiatan=[str(x) for x in input().split()] 
       kegiatanTobi= kegiatanTobi+[Kegiatan[0]]
       daftarKegiatan= kegiatanTobi
     print(daftarKegiatan)
else:
  if BanyakKegiatan<1:
        print("Tobi tidak ingin bermalas-malasan!")
  else:
        print("Tobi tidak bisa bekerja terlalu keras")
