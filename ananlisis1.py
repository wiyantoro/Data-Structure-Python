tempat={'Program':[]}
jmlprogram=2
tempat['Program']=[None]*jmlprogram
var1='IT'
var2='Desigh'
var3='Fasilitas'
var4='Sistem Belajar'
var5='Fasilitas'
var6='Sistem Belajar'
tempat={'Program':{var1:{var3:[],var4:[]},var2:{var5:[],var6:[]}}}
jmlfasilitas=2
jmlsb=2
tempat['Program'][var1][var3]=[None]*jmlfasilitas
tempat['Program'][var1][var3][0]='Ruang kelas'
tempat['Program'][var1][var3][1]='AC'
tempat['Program'][var1][var4]=[None]*jmlsb
tempat['Program'][var1][var4][0]='Online'
tempat['Program'][var1][var4][1]='Ofline'
tempat['Program'][var2][var5]=[None]*jmlfasilitas
tempat['Program'][var2][var5][0]='Ruang kelas'
tempat['Program'][var2][var5][1]='AC'
tempat['Program'][var2][var6]=[None]*jmlsb
tempat['Program'][var2][var6][0]='Online'
tempat['Program'][var2][var6][1]='Ofline'


print(tempat)