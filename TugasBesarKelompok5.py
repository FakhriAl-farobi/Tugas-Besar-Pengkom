#Deskripsi : Program Palang Pintu Tol Otomatis di Tol Jakarta - Tangerang
#KAMUS : 

#Algoritma 
import random
import sys
import time

tarif_tolJT = [8000, 12000, 12000, 15500, 15500, '-']
AsalPerjalanan = ['A : TomangIC', 'B : Tangerang', 'C : Cikupa']
Gol_Kdr = ['|    Golongan    |        Jenis Kendaraan               |', '|    Golongan I  |Sedan,Jip,Pick Up/Truck Kecil, dan Bus|', '|    Golongan II |       Truk dengan 2(dua) gandar      |', 
'|    Golongan III|       Truk dengan 3(tiga) gandar     |', '|    Golongan IV |       Truk dengan 4(empat) gandar    |', '|    Golongan V  |       Truk dengan 5(lima) gandar     |',
'|    Golongan VI |                    -                 |']
ID_EToll = ['1357', '7531', '5173', '3157', '5713', '7135', '3751', '5371']
Saldo_EToll = [2000, 3579900,7236,89239,90000,7800000,543211,89023]
No_Rek0 = ['1234 5678', '2345 6789', '3456 7890', '4567 8901', '5678 9012', '6789 0123', '7890 1234', '8901 2345', '9012 3456', '0123 4567']
b = 0
z = False
a = False

def mengetik(s): #membuat tulisan berjalan
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.04) #kecepatan mengetik

print('      ', end=''); mengetik('Selamat Datang di Tol Masuk Jakarta - Tangerang'); time.sleep(0.5)
print('|----------------|--------------------------------------|'); time.sleep(0.1)
for i in range(0, 7):
    print(Gol_Kdr[i]); time.sleep(0.1) #menuliskan daftar golongan kendaraan
    print('|----------------|--------------------------------------|'); time.sleep(0.1)
print()
Gol_Kdr = int(input()); time.sleep(0.5)
print()
print('                 ', end=''); mengetik('Pilih Tol Masuk :')
for i in range(0, 3):
    mengetik(AsalPerjalanan[i]); time.sleep(0.1)
print()
Masuk = input()
print(); time.sleep(0.5)
while(z == False):
    Tempel_Kartu1 = input('Tempelkan Kartu : ')
    for i in range(0, 8):
        if Tempel_Kartu1 == ID_EToll[i]:
            z = True
            mengetik('Sisa Saldo : '+ 'Rp' + str(Saldo_EToll[i]))
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
            mengetik('=== Palang Pintu Terbuka ===\n   === Silahkan Lewat ===   \n=== Hati-Hati di Jalan ===')
    if z == False :
        mengetik('Kartu Tol Belum Terdaftar')

#Kendaraan melewati tol masuk
time.sleep(1); print(); mengetik('      "Kendaraan melewati Tol"      \n => => => => => => => => => => => => => => => => =>'); print(); time.sleep(1)

print('      ', end=''); mengetik('Selamat Datang di Tol Keluar Jakarta - Tangerang'); time.sleep(0.5)
print('   ', end=''); mengetik('Daftar Tarif Harga Berdasarkan Golongan : ')
for i in range(0,6):
    mengetik('Golongan-'+str(i + 1) + ' : Rp' + str(tarif_tolJT[i]))
print()
print('                 ', end=''); mengetik('Pilih Tol Keluar :')
for i in range(0, 3):
    mengetik(AsalPerjalanan[i]); time.sleep(0.1)
print()
Masuk = input()
print(); time.sleep(0.5)
mengetik('Tempelkan Kartu untuk Pembayaran')
while(z == True):
    Tempel_Kartu2 = input('Tempelkan Kartu : ')
    for i in range(0, 8):
        if Tempel_Kartu2 == ID_EToll[i] and Tempel_Kartu1 == Tempel_Kartu2 :
            b = b - tarif_tolJT[Gol_Kdr - 1]
            mengetik('Sisa Saldo : '+ 'Rp' + str(b))
            mengetik('=== Palang Pintu Terbuka ===\n   === Sampai Jumpa ===   \n=== Hati-Hati di Jalan  ===')
            z = False
        elif Tempel_Kartu1 != Tempel_Kartu2 and Tempel_Kartu2 == ID_EToll[i] :
            mengetik('Gunakan kartu yang sama saat tol masuk!')
            a = True
    if z == True and a == False :
        mengetik('Kartu Tol Belum terdaftar')