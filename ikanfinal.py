print("----------------- Toko Ikan -----------------")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def macamikan():
   global totalikan
   global bnykikan
   global ikan
   print ("----------------- Jenis Dan Harga Ikan -----------------")
   print("1. Ikan Maru - Rp 20.000")
   print("2. Ikan Limbata - Rp 25.000")
   print("3. Ikan Andrao - Rp 35.000")
   nomor=int(input("Pilih Nomor: "))
   bnykikan= int(input("Berapa Ekor: "))
   
   if nomor==1:
       totalikan=bnykikan*20000
       print (bnykikan,"Ekor Ikan Maru= Rp", totalikan)
       ikan=("Ikan Maru")
   elif nomor==2:
       totalikan=bnykikan*25000
       print (bnykikan,"Ekor ikan Limbata = Rp", totalikan)
       ikan=("Ikan Limbata")
   elif nomor==3:
       totalikan=bnykikan*35000
       print (bnykikan, "Ekor Ikan Andrao = Rp", totalikan)
       ikan=("Ikan Andrao")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      macamikan()
      
def mknikan():
   global totalmkn
   global mkn
   global bnykmkn
   print("----------------- Makanan Ikan -----------------")
   print("1. Pelet Ikan - Rp 15.000")
   print("2. Pelet Premium - Rp 25.000")
   print("3. Udang Kering - Rp 35.000")
   nomor=int(input("Pilih Nomor: "))
   bnykmkn= int(input("Berapa Banyak: "))

   if nomor==1:
       totalmkn=bnykmkn*15000
       print (bnykmkn,"Pelet Ikan = Rp", totalmkn)
       mkn=("Pelet Ikan")
   elif nomor==2:
       totalmkn=bnykmkn*25000
       print (bnykmkn, "Pelet Premium = Rp", totalmkn)
       mkn=("Pelet Premium")
   elif nomor==3:
       totalmkn=bnykmkn*35000
       print (bnykmkn, "Udang Kering = Rp", totalmkn)
       mkn=("Udang Kering")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      mknikan()
      
def peralatan():
   global totalalat
   global alat
   global bnykalat
   print("----------------- Peralatan -----------------")
   print("1. Saringan Ikan S - Rp 10.000")
   print("2. Saringan Ikan M - Rp 20.000")
   print("3. saringan Ikan L - Rp 30.000")
   nomor=int(input("Pilih Nomor: "))
   bnykalat= int(input("Berapa Banyak: "))

   if nomor==1:
       totalalat=bnykalat*10000
       print (bnykalat,"Saringan Ikan S = Rp", totalalat)
       alat=("Saringan Ikan S")
   elif nomor==2:
       totalalat=bnykalat*20000
       print (bnykalat, "Saringan Ikan M = Rp", totalalat)
       alat=("Saringan Ikan M")
   elif nomor==3:
       totalalat=bnykalat*30000
       print (bnykalat, "Saringan Ikan L = Rp", totalalat)
       alat=("Saringan Ikan L")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      peralatan()
      
macamikan() 
mknikan()
peralatan()

print("========List Belanja=======")
print ("Beli:",bnykikan,ikan,"( Rp", totalikan,")")
print("Beli:",bnykmkn,mkn,"(Rp",totalmkn,")")
print ("Beli:",bnykalat,alat,"( Rp", totalalat,")")
    
print("========Total Semuanya======")
totalsemua=totalikan+totalmkn+totalalat

print("Total harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("==================================")
print("========== S T R U K   B E L I =========")
print("==================================")
print ("Nama:",pembeli)
print ("Beli:",bnykikan,ikan,"( Rp", totalikan,")")
print("Beli:",bnykmkn,mkn,"(Rp",totalmkn,")")
print ("Beli:",bnykalat,alat,"( Rp", totalalat,")")
print ("Total Semuanya: Rp",totalsemua)
print ("Dibayar: Rp",uang)
print ("Kembalian: Rp",kembalian)
print("==================================")
print("==================================")