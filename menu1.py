

print("----------------- Toko Ikan -----------------")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Jenis Dan Harga Ikan -----------------")
   print("1. Nasi Goreng - Rp 15000")
   print("2. Soto - Rp 9000")
   print("3. Mie Ayam - Rp 11000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalmkn=porsi*15000
       print (porsi," porsi Nasi Goreng Telur = Rp", totalmkn)
       mkn=("Nasi Goreng")
   elif nomor==2:
       totalmkn=porsi*9000
       print (porsi," porsi Soto = Rp", totalmkn)
       mkn=("Soto")
   elif nomor==3:
       totalmkn=porsi*11000
       print (porsi, " porsi Mie Ayam = Rp", totalmkn)
       mkn=("Mie Ayam")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()
fungsimakanan()      
totalsemua=totalmkn

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== S T R U K   B E L I =========")
print("==================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")
