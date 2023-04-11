

print("----------------- Toko Ikan -----------------")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def macamikan():
   global totalikan
   global bnyk
   global ikan
   print ("----------------- Jenis Dan Harga Ikan -----------------")
   print("1. Ikan Maru - Rp 20000")
   print("2. Ikan Limbata - Rp 25000")
   print("3. Ikan Andrao - Rp 35000")
   nomor=int(input("Masukan Pilihan: "))
   bnyk= int(input("Berapa Ekor: "))
   
   if nomor==1:
       totalikan=bnyk*20000
       print (bnyk,"Ekor Ikan Maru= Rp", totalikan)
       ikan=("Ikan Maru")
   elif nomor==2:
       totalikan=bnyk*25000
       print (bnyk,"Ekor ikan Limbata = Rp", totalikan)
       ikan=("Ikan Limbata")
   elif nomor==3:
       totalikan=bnyk*35000
       print (bnyk, "Ekor Ikan Andrao = Rp", totalikan)
       ikan=("Ikan Andrao")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      macamikan()
macamikan()      
totalsemua=totalikan

print("Total harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== S T R U K   B E L I =========")
print("==================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",bnyk,ikan,"( Rp", totalikan,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")