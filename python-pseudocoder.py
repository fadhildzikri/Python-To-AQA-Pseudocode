#Sensus Penduduk Kota Balikpapan

#batas
def batas1 ():
    print("=============================================================================================================")
def batas2 ():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
def batas3 ():
    print("........................................................................")



print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("                              SELAMAT  DATANG  DI  SENSUS  PENDUDUK                               ")
print("                               KOTA  BALIKPAPAN TINGKAT  KECAMATAN                                ")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("*******************************************MENU UTAMA*********************************************")
print("  |1 Balikpapan Timur                                               4 Balikpapan Utara         |")
print("  |2 Balikpapan Selatan                                             5 Balikpapan Barat         |")
print("  |3 Balikpapan Tengah                                              6 Balikpapan Kota          |")
print("**************************************************************************************************")

pilih=str(input("Pilih Menu yang Anda Inginkan: "))

#menu1
def menu1 ():
    batas1 ()
    print ("                                      Balikpapan Timur                                     ")
    batas1 () 
    print ("Kelurahan di Balikpapan Timur adalah sebagai berikut :")
    
    print ("1. Manggar")
    print ("2. Manggar Baru")
    print ("3. Lamaru")
    print ("4. Teritip")

#menu 2
def menu2 ():
    batas1 ()
    print ("                                     Balikpapan Selatan                                   ")
    batas1 () 
    print ("Kelurahan di Balikpapan Selatan adalah sebagai berikut :")
    
    print ("1. Damai Baru")
    print ("2. Damai Bahagia")
    print ("3. Sepinggan Baru")
    print ("4. Sungai Nangka")
    print ("5. Sepinggan Raya")
    print ("6. Gunung Bahagia")
    print ("7. Sepinggan")

#menu 3
def menu3 ():
    batas1 ()
    print ("                                    Balikpapan Tengah                                    ")
    batas1 ()  
    print ("Kelurahan di Balikpapan Tengah adalah sebagai berikut :")
    
    print ("1. Gunung Sari Ilir")
    print ("2. Gunung Sari Ulu")
    print ("3. Mekar Sari")
    print ("4. Karang Rejo")
    print ("5. Sumber Rejo")
    print ("6. Karang Jati")

#menu 4
def menu4 ():
    batas1 ()
    print ("                                    Balikpapan Utara                                    ")
    batas1 () 
    print ("Kelurahan di Balikpapan Utara adalah sebagai berikut :")
    
    print ("1. Gunung Samarinda")
    print ("2. Muara Rapak")
    print ("3. Batu Ampar")
    print ("4. Karang Joang")
    print ("5. Gunung Samarinda Baru")
    print ("6. Graha Indah")
    
#menu 5
def menu5 ():
    batas1 ()
    print ("                                    Balikpapan Barat                                  ")
    batas1 () 
    print ("Kelurahan di Balikpapan Barat adalah sebagai berikut :")
    
    print ("1. Baru Ilir")
    print ("2. Margo Mulyo")
    print ("3. Marga Sari")
    print ("4. Baru Tengah")
    print ("5. Baru Ulu")
    print ("6. Kariangau")

#menu 6
def menu6 ():
    batas1 ()
    print ("                                    Balikpapan Kota                                   ")
    batas1 () 
    print ("Kelurahan di Balikpapan Kota adalah sebagai berikut :")
    
    print ("1. Prapatan")
    print ("2. Telaga Sari")
    print ("3. Klandasan Ulu")
    print ("4. Klandasan Ilir")
    print ("5. Damai")


print()
if(pilih=="1" or pilih=="1."):
        menu1()
elif(pilih=="2" or pilih=="2."):
        menu2()
elif(pilih=="3" or pilih=="3."):
        menu3()
elif(pilih=="4" or pilih=="4."):
        menu4()
elif(pilih=="5" or pilih=="5."):
        menu5 ()
elif(pilih=="6" or pilih=="6."):
        menu6 ()
        
i=a=b=c=d=e=f=0
nama                 =[]
jumlah_penduduk      =[]
pertumbuhan_penduduk =[]
angka_kelahiran      =[]
angka_kematian       =[]
pendapatan           =[]

print ()
batas2 ()
while True:
        print ("INPUT DATA KE-",i+1)
        nama.append(str(input                ("Nama Kelurahan       :")))
        jumlah_penduduk.append(int(input     ("Jumlah Penduduk      :")))
        pertumbuhan_penduduk.append(int(input("Pertumbuhan Penduduk :")))
        angka_kelahiran.append(int(input     ("Angka Kelahiran      :")))
        angka_kematian.append(str(input      ("Angka Kematian       :")))
        pendapatan.append(int(input          ("Pendapatan           :")))

        print()
        batas2()
        input_lagi=''
        while input_lagi!="Y" and input_lagi!="T":
             input_lagi=input("APAKAH ANDA INGIN MENGINPUT DATA LAGI? [Y/T] :")
        i+=1
        batas2()
        if input_lagi=="T":
            break
print()
batas1 ()
print(" SENSUS PENDUDUK KOTA BALIKPAPAN TINGKAT KECAMATAN  ")
batas1 ()
print(" NO / Nama Kecamatan / Jumlah Penduduk / Pertumbuhan penduduk / Angka Kelahiran / Angka Kematian / Pendapatan")
batas1 ()

for n in range (i):
          print(n+1,' ',nama[n],' ',jumlah_penduduk[n],' ',pertumbuhan_penduduk[n],' ',angka_kelahiran[n],' ',angka_kematian[n],' ',pendapatan[n],'')
batas1 ()
print()
print()


   
print("*******************************************************************************************************************")
print("                                                 HASIL DATA STATISTIK                                              ")
print("*******************************************************************************************************************")
                                                                                                                                
print("JUMLAH PENDUDUK")
print("Jumlah Penduduk                                :" + str(sum(jumlah_penduduk+[])))
print("Jumlah Penduduk Terendah                       :" + str(min(jumlah_penduduk+[])))
terendah=jumlah_penduduk.index(min(jumlah_penduduk))
print("Kelurahan dengan penduduk terendah adalah      :" + str(nama[terendah]))
print("Jumlah Penduduk Tertinggi                      :" + str(max(jumlah_penduduk+[])))
tertinggi=jumlah_penduduk.index(max(jumlah_penduduk))
print("Kelurahan dengan penduduk tertinggi adalah     :" + str(nama[tertinggi]))
print("Rata-rata Jumlah Penduduk                      :" + str(sum(jumlah_penduduk+[]) / len(jumlah_penduduk)))
print ()
batas3 ()

print("PERTUMBUHAN PENDUDUK")
print("Rata-rata Pertumbuhan Penduduk                 :" + str(sum(pertumbuhan_penduduk+[]) / len(pertumbuhan_penduduk)))
print ()
batas3 ()

print("ANGKA KELAHIRAN")
print("Angka Kelahiran Terendah                       :" + str(min(angka_kelahiran+[])))
terendah=angka_kelahiran.index(min(angka_kelahiran))
print("Angka Kelahiran Terendah terdapat di Kelurahan :" + str(nama[terendah]))
print("Angka Kelahiran Tertinggi                      :" + str(max(angka_kelahiran+[])))
tertinggi=angka_kelahiran.index(max(angka_kelahiran))
print("Angka Kelahiran Tertinggi terdapat di Kelurahan:" + str(nama[tertinggi]))
print ()
batas3 ()

print("ANGKA KEMATIAN")
print("Angka Kematian Terendah                        :" + str(min(angka_kematian+[])))
terendah=angka_kematian.index(min(angka_kematian))
print("Angka Kematian Terendah terdapat di Kelurahan  :" + str(nama[terendah]))
print("Angka Kematian Terendah                        :" + str(max(angka_kematian+[])))
tertinggi=angka_kematian.index(max(angka_kematian))
print("Angka Kematian Tertinggi terdapat di Kelurahan :" + str(nama[tertinggi]))
print ()
batas3 ()

print("PENDAPATAN")
print("Pendapatan Terendah                            :" + str(min(pendapatan+[])))
terendah=pendapatan.index(min(pendapatan))
print("Pendapatan Terendah terdapat di Kelurahan      :" + str(nama[terendah]))
print("Pendapatan Tertinggi                           :" + str(max(pendapatan+[])))
tertinggi=pendapatan.index(max(pendapatan))
print("Pendapatan Tertinggi terdapat di Kelurahan     :" + str(nama[tertinggi]))
print("Rata-rata Pendapatan                           :",sum(pendapatan+[])/int(len(pendapatan)))
print ()
batas3 ()
