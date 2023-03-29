inputprogram=int(input("Berapa Program Yang ada? "))
tempat={'Program':{}}
for i in range(inputprogram):
    namaprogram=input("Nama program IT?")
    tempat['Program'][namaprogram]={}
    inputfasilitas=int(input("Berapa Fasilitas "+namaprogram+"yang ada? "))
    for j in range(inputfasilitas):
        namafasilitas=input("Nama Fasilitas "+namaprogram+":")
        input2=int(input("Berapa "+namafasilitas+" "+namaprogram+"yang ada? "))
        tempat['Program'][namaprogram][namafasilitas]=[None]*input2
        for k in range(input2):
            namainput2=input("Nama "+namafasilitas+" "+namaprogram+" :")
            tempat['Program'][namaprogram][namafasilitas][k]=namainput2
    print(tempat)
