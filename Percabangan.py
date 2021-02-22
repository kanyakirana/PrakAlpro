# Nama : Kanya Kirana Litasari
# Informatika - Universitas Kristen Duta Wacana 
# Topik : "Percabangan"

''' Tahun lalu belum ada program pemesanan tiket kereta api yang dilakukan secara online. Karena program itu belum pernah ada yang
membuatnya, kemudian ada seorang yang bernama Nizam ingin mencoba membuat program tersebut yang menampilkan kota tujuan,nama kereta 
yang dipilih, waktu keberangkatan dan kedatangan, serta harga tiket. Bantulah Nizam dalam pembuatan program pemesanan tiket kereta api.
'''

'''
Input  : pilihan tujuab, kode kereta, jumlah tiket

Proses : penghitungan total harga

Output : menampilkan jumlah tiket kereta yang dipesan disertai nama kereta dengan waktu keberangkatan dan kedatangan, menampilkan total 
harga, menampilkan kalimat anda telah berhasil melakukan pemesanan tiket kereta api dan silahkan lakukan pembayaran

'''

print("-----------------------------------")
print("PROGRAM PEMESANAN TIKET KERETA API")
print("-----------------------------------")
print("1. Jakarta")
print("2. Surabaya")
print("3. Exit")
pilihan=str(input("Masukkan pilihan [1-3] : "))

if pilihan=="1":
    print("Kode  Nama\tKota\t\tWaktu\t\tWaktu\t\tHarga")
    print("      Kereta\tTujuan\t\tKeberangkatan\tKedatangan\tTiket")
    print("--------------------------------------------------------------------------------------------")
    print("101.  Taksaka\tJakarta\t\t20.15\t\t03.29\t\tRp 290.0000")
    print("102.  Gajayana\tJakarta\t\t09.22\t\t16.29\t\tRp 355.000")
    print("--------------------------------------------------------------------------------------------")
    kode=str(input("Masukkan Kode Kereta yang dipilih : "))
    if kode=="101":
        tiket=int(input("Masukkan jumlah tiket : "))
        kereta="Kereta Taksaka Waktu Keberangkatan Pukul 20.15 dan Waktu Kedatangan Pukul 03.29"
        harga=290000
        total=harga*tiket
        print("--------------------------------------------------------------------------------------------------")
        print((tiket), "tiket", (kereta))
        print("Total Harga : Rp ", (total))
        print("Anda telah berhasil melakukan pemesanan tiket kereta api dan silahkan lakukan pembayaran")
        print("--------------------------------------------------------------------------------------------------")
    elif kode=="102":
        tiket=int(input("Masukkan jumlah tiket : "))
        kereta="Kereta Gajayana Waktu Keberangkatan Pukul 09.22 dan Waktu Kedatangan Pukul 16.29"
        harga=355000
        total=harga*tiket
        print("---------------------------------------------------------------------------------------------------")
        print((tiket), "tiket", (kereta))
        print("Total Harga : Rp ", (total))
        print("Anda telah berhasil melakukan pemesanan tiket kereta api dan silahkan lakukan pembayaran")
        print("---------------------------------------------------------------------------------------------------")
    else :
        print("Kode Kereta yang Diinputkan Tidak Tersedia")
elif pilihan=="2":
    print("Kode  Nama\tKota\t\tWaktu\t\tWaktu\t\tHarga")
    print("      Kereta\tTujuan\t\tKeberangkatan\tKedatangan\tTiket")
    print("201.  Turangga\tSurabaya\t01.44\t\t06.37\t\tRp 220.000")
    print("202.  Jayakarta\tSurabaya\t14.52\t\t19.01\t\tRp 240.000")
    kode=str(input("Masukkan Kode Kereta yang Dipilih : "))
    if kode=="201":
        tiket=int(input("Masukkan jumlah tiket : "))
        kereta="Kereta Turangga Waktu Keberangkatan Pukul 01.44 dan Waktu Kedatangan Pukul 06.37"
        harga=220000
        total=harga*tiket
        print("---------------------------------------------------------------------------------------------------")
        print((tiket), "tiket", (kereta))
        print("Total Harga : Rp ", (total))
        print("Anda telah berhasil melakukan pemesanan tiket kereta api dan silahkan lakukan pembayaran")
        print("---------------------------------------------------------------------------------------------------")
    elif kode=="202":
        tiket=int(input("Masukkan jumlah tiket : "))
        kereta="Kereta Jayakarta Waktu Keberangkatan Pukul 14.52 dan Waktu Kedatangan Pukul 19.01"
        harga=240000
        total=harga*tiket
        print("---------------------------------------------------------------------------------------------------")
        print((tiket), "tiket", (kereta))
        print("Total Harga : Rp ", (total))
        print("Anda telah berhasil melakukakn pemesanan tiket kereta api dan silahkan lakukan pembayaran")
        print("---------------------------------------------------------------------------------------------------")
    else :
        print("Kode Kereta yang diinputkan tidak tersedia")
elif pilihan=="3":
    print("Anda telah keluar dari Program Pemesanan Tiket Kereta Api")
else :
    print("Pilihan yang diinputkan tidak tersedia")