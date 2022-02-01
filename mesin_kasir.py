barang = []

while True:
    print("""
    ==============================
    Toko Ada Semua
    List Barang 
    ==============================
    Sedang ada diskon spesial 
    **beli 5 indomie dapatkan diskon 20%**
    ==============================
    1. Pulpen : Rp 4.000
    2. Buku : Rp 7.000
    3. Akua : Rp 1.000
    4. Teh Segienam : Rp 6.600
    5. Indomie : Rp 2.500
    6. Telur : Rp 2.500
    7. AK-47 : Rp 69.420
    8. Sotgun Api : Rp 300.000
    9. Alok : Rp 360.420
    10. Immortal : Rp 2.210
    11. Mikoyan-Gurevich MiG-31 Foxhound supersonic interceptor aircraft carrying Kh-47 air-launched ballistic missiles : Rp 69.696
    
    ==============================
    """)
    
    kode = str(input('Masukkan Kode Barang : '))
    jumlahbarang=int(input("Masukkan jumlah barang : "))
    if kode == '1':
        barang.append('Pulpen')
        harga=int(4000*jumlahbarang)
        ppn = int(harga * 0.1)
        diskon=0
        total=(harga+ppn)
    elif kode == '2':
        barang.append('Buku')
        harga=int(7000*jumlahbarang)
        ppn = int(harga * 0.1)
        diskon=0
        total=(harga+ppn)
    elif kode == '3':
        barang.append('Akua')
        harga=int(1000*jumlahbarang)
        ppn =int(harga * 0.1)
        diskon=0
        total=(harga+ppn)
    elif kode == '4':
        barang.append('Teh Segienam')
        harga=int(6000*jumlahbarang)
        ppn = int(harga * 0.1)
        diskon=0
        total=(harga+ppn)
    elif kode == '5':
        barang.append('Indomie')
        harga=int(2500*jumlahbarang)
        if jumlahbarang >= 5:
            diskon = int(harga*0.2)
            total=int(harga-diskon)
        else:
            diskon =(0)
            total=int(harga)
    elif kode == '6':
        barang.append('Telur')
        harga=int(2500*jumlahbarang)
        ppn = int(harga * 0.1)
        diskon=0
        total=(harga+ppn)
    elif kode == '7':
        barang.append('AK-47')
        harga=int(69420*jumlahbarang)
        ppn = int(harga * 0.1)
        diskon=0
        total=(harga+ppn)
    elif kode == '8':
        barang.append('Shotgun Api')
        harga=int(300000*jumlahbarang)
        ppn = int(harga * 0.1)
        diskon=0
        total=(harga+ppn)
    elif kode == '9':
        barang.append('Alok')
        harga=int(360240*jumlahbarang)
        ppn = int(harga * 0.1)
        diskon=0
        total=(harga+ppn)
    elif kode == '10':
        barang.append('Immortal')
        harga=int(2210*jumlahbarang)
        ppn = int(harga * 0.1)
        diskon=0
        total=(harga+ppn)
    elif kode == '11':
        barang.append('Mikoyan-Gurevich MiG-31 Foxhound supersonic interceptor aircraft carrying Kh-47 air-launched ballistic missiles')
        harga=int(69696969*jumlahbarang)
        ppn = int(harga * 0.1)
        diskon=0
        total =(harga+ppn)
    else:
        print('kode yang anda masukkan tidak valid')

    #jika
    lanjut = input('lanjut belanja? (y/n)  : ')
    if lanjut == 'n':
        print('')
        break
    
print('--------------------------')
print('Toko Ada Semua')
print('--------------------------')
print('Barang yang dibeli : ', barang)
print('Harga Barang : ', harga)
print("Diskon :", diskon)
print('--------------------------')
print('Total Harga : ', total)
print('--------------------------')

uang = int(input('Uang Pembayaran : '))
if uang > total:
    print('Kembalian :', uang - total)
elif uang == total:
    print('Uang pas')
else:
    print('Uang Pembayaran kurang', uang - total)