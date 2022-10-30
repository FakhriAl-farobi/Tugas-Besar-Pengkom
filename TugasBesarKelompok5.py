#Deskripsi : Program Palang Pintu Tol Otomatis di Tol Jakarta - Tangerang
#KAMUS : 

#Algoritma 
from datetime import datetime
import random
import sys
import time
import os
from time import sleep
import datetime

Riwayat = []
f = datetime.datetime.now()
ID_EToll = ['1357', '7531', '5173', '3157', '5713', '7135', '3751', '5371']
Saldo_EToll = [2000, 3579900,7236,89239,90000,7800000,543211,89023]
No_Rek0 = ['1234 5678', '2345 6789', '3456 7890', '4567 8901', '5678 9012', '6789 0123', '7890 1234', '8901 2345', '9012 3456', '0123 4567']
tarif_tolJT = [8000, 12000, 12000, 15500, 15500]

def Cek():
    os.system('cls') 

    p = ""
    while (p==""):
        AsalPerjalanan = ['A : TomangIC', 'B : Tangerang', 'C : Cikupa']
        Gol_Kdr = ['|    Golongan    |        Jenis Kendaraan               |   Harga   |', '|    Golongan I  |Sedan,Jip,Pick Up/Truck Kecil, dan Bus| Rp8.000   |', '|    Golongan II |       Truk dengan 2(dua) gandar      | Rp12.000  |', 
        '|    Golongan III|       Truk dengan 3(tiga) gandar     | Rp12.000  |', '|    Golongan IV |       Truk dengan 4(empat) gandar    | Rp15.500  |', '|    Golongan V  |       Truk dengan 5(lima) gandar     | Rp15.500  |']     
        
        b = 0
        z = False
        a = False

        def mengetik(s): #membuat tulisan berjalan
            for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(random.random() * 0.04) #kecepatan mengetik

        #Pintu Masuk
        print('      ', end=''); mengetik('Selamat Datang di Tol Masuk Jakarta - Tangerang'); time.sleep(0.5)
        print('|----------------|--------------------------------------|-----------|'); time.sleep(0.1)
        for i in range(0, 6):
            print(Gol_Kdr[i]); time.sleep(0.1) #menuliskan daftar golongan kendaraan
            print('|----------------|--------------------------------------|-----------|'); time.sleep(0.1)
        mengetik('Jika Ada Kendala Silahkan Tekan Tombol Warna Merah atau Hubungi 1122 3344')
        print()
        
        #Pilih Golongan
        while (True):
            Gol_Kdr = int(input()); time.sleep(0.5)
            if Gol_Kdr == 1:    
                GolKdr = "Golongan I"
                break
            elif Gol_Kdr == 2:
                GolKdr = "Golongan II"
                break
            elif Gol_Kdr == 3:
                GolKdr = "Golongan III"
                break
            elif Gol_Kdr == 4:
                GolKdr = "Golongan IV"
                break
            elif Gol_Kdr == 5:
                GolKdr = "Golongan V"
                break
        
        #Pilih Pintu Tol Masuk
        print()
        print('                 ', end=''); mengetik('Pilih Tol Masuk :')
        for i in range(0, 3):
            mengetik(AsalPerjalanan[i]); time.sleep(0.1)
        print()
        
        
        masuk = ""
        while(masuk == ""):
            masuk = input()
            if masuk == 'a':
                masuk = 'TomangIC'
                AsalPerjalanan.remove(AsalPerjalanan[0])
                break
            elif masuk == 'b':
                masuk = 'Tangerang'
                AsalPerjalanan.remove(AsalPerjalanan[1])
                break
            elif masuk == 'c':
                masuk = 'Cikupa'
                AsalPerjalanan.remove(AsalPerjalanan[2])
                break
            else:
                masuk = ""
        
        print(); time.sleep(0.5)

        #Cek Kartu Masuk
        
        while(z == False):
            Tempel_Kartu1 = input('Tempelkan Kartu : ')
            for i in range(0, 8):
                if Tempel_Kartu1 == ID_EToll[i]:
                    z = True
                    mengetik(masuk)
                    mengetik(GolKdr) 
            if z == False :
                mengetik('Tempelkan Kartu Dengan Benar!')
        print()
        mengetik('=== Palang Pintu Terbuka ===\n   === Silahkan Lewat ===   \n=== Hati-Hati di Jalan ===')

        #Kendaraan melewati tol masuk
        time.sleep(1); print(); mengetik('      "Kendaraan melewati Tol"      \n => => => => => => => => => => => => => => => => =>'); print(); time.sleep(1)


        #Pintu Tol Keluar
        print('      ', end=''); mengetik('Selamat Datang di Tol Keluar Jakarta - Tangerang'); time.sleep(0.5)
        print()
        mengetik('Jika Ada Kendala Silahkan Tekan Tombol Warna Merah atau Hubungi 1122 3344')
        print()
        print('                 ', end=''); mengetik('Pilih Tol Keluar :')


        for i in range(0, 2):
            mengetik(AsalPerjalanan[i]); time.sleep(0.1)
        print()
        keluar = ""
        while(keluar == ""):
            keluar = input()
            if keluar == 'a':
                keluar = 'TomangIC'
                break
            elif keluar == 'b':
                keluar = 'Tangerang'
                break
            elif keluar == 'c':
                keluar = 'Cikupa'
                break
            else:
                keluar = ""

        Noid = 0
        print(); time.sleep(0.5)
        #mengetik('Tempelkan Kartu untuk Pembayaran')


        while(z == True):
            Tempel_Kartu2 = input('Tempelkan Kartu : ')
            for i in range(0, 8):
                if Tempel_Kartu2 == ID_EToll[i] and Tempel_Kartu1 == Tempel_Kartu2 :
                    Noid = Noid +i
                    b = Saldo_EToll[i]
                    while(b < tarif_tolJT[Gol_Kdr - 1]) : 
                        z = False
                        mengetik('Saldo anda kurang harap isi ulang terlebih dahulu')
                        print('         ', end=''); mengetik('=== Isi Ulang Kartu ===')
                        No_Rek = input('Nomor Rekening : ')
                        for i in range(0,10):
                            if No_Rek == No_Rek0[i]:
                                Isi_Ulang = int(input('Jumlah Pengisian Ulang : '))
                                b = b + Isi_Ulang
                                z = True
                                mengetik('Sisa Saldo : '+ 'Rp' + str(b))
                        if z == False :
                            print('       ', end=''); mengetik('=== Rekening Belum Terdaftar ===')

                    b = b - tarif_tolJT[Gol_Kdr - 1]
                    mengetik(keluar)
                    mengetik(GolKdr)
                    print()
                    mengetik('Sisa Saldo : '+ 'Rp' + str(b))
                    mengetik('=== Palang Pintu Terbuka ===\n   === Sampai Jumpa ===   \n=== Hati-Hati di Jalan  ===')
                    z = False
                elif Tempel_Kartu1 != Tempel_Kartu2 and Tempel_Kartu2 == ID_EToll[i] :
                    mengetik('Gunakan kartu yang sama saat tol masuk!')
                    a = True
            if z == True and a == False :
                mengetik('Kartu Tol Belum terdaftar')
        Saldo_EToll[Noid] = b
        riw = str(f.date())+'/'+str(f.time())+'/'+ID_EToll[Noid]+'/'+masuk+'/'+keluar+'/'+str(tarif_tolJT[Gol_Kdr - 1])
        Riwayat.append(riw)
        p = input()
        os.system('cls') 
        

def CetakRiwayat():
    os.system('cls')
    def mengetik(s): #membuat tulisan berjalan
            for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(random.random() * 0.04) #kecepatan mengetik
    print('      ', end=''); mengetik('Riwayat Transaksi Tol Masuk Jakarta - Tangerang'); time.sleep(0.5)
    print()
    print('|------------------------------------------------------|'); time.sleep(0.1)
    print()
    mengetik('Tanggal/Jam/ID Kartu Tol/Tol Masuk/Tol Keluar/Jumlah Transaksi')
    for i in Riwayat:
        print(i)
    n = input()
    os.system('cls')

v = True
while (v == True):
    os.system('cls') 
    print("====================================")
    print("========  PINTU TOL OTOMATIS =======")
    print("====================================")   
    print("")
    print("1. Transaksi pintu tol")
    print("2. Cek riwayat transaksi ")
    print("0. Keluar")
    print()
    a = input("Masukan: ")
    if a == '1':
        Cek()
    elif a == '2':
        pw = 'bismillahlulusitb2026'
        k = ''
        while(k == ""):
            password = input("Masukkan Password: ")
            if password == pw:
                break
        CetakRiwayat()
    elif a == '0':
        v = False
    os.system('cls') 

