# Toko Ikan hias
from tkinter import *
from tkinter import colorchooser


ikanhias = []
harganya = []
jumlah = 0

while True:
    ikan = input("Jenis Ikan Apaa? (q Untuk Selesai Memesan): ")
    if ikan.lower() == "q":
        break
    else:
        harga = float(input(f"Harga Ikan {ikan}: Rp."))
        ikanhias.append(ikan)
        harganya.append(harga)

print("----- Total Belanja -----")

for ikan in ikanhias:
    print(ikan, end=" ")

for harga in harganya:
    jumlah += harga

print()
print(f"Jumlah Belanja Ikan: ${jumlah}")