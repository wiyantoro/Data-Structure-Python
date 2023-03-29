print("Tempat kursus Terbaru")
tempat={}
namatempat=input("Nama Tempat nya? : ")
print("Selamat Datang Di "+namatempat)

jumlahprogram=int(input("Berapa Banyak Programnya? : "))
tempat['program']=[None]*jumlahprogram


for i in range(jumlahprogram): 
    namaprogram=input("program"+str(i+1)+":")
    tempat['program'][i]=namaprogram

jumlahruang=int(input("Berapa Banyak Ruang? :"))
tempat['Fasilitas']['Ruang kelas']=[None]*jumlahruang

for i in range(jumlahruang):
    namaruang=input("Ruang "+str(i+1)+": ")
    tempat['Fasilitas']['Ruang kelas'][i]=namaruang
jumlahsistem=int(input("Berapa sistem Belajar yang ingin anda jalankan? : "))
tempat['Fasilitas']['Ruang kelas']=[None]*jumlahsistem

for i in range(jumlahsistem):
    namasistem=input("Sistem"+str(i+1)+": ")
    tempat['Fasilitas']['Sistem kelas'][i]=namasistem
    
    
