# Nama-NIM : Kanya Kirana Litasari-71200666
# Informatika - Universitas Kristen Duta Wacana 
# Topik : "Percabangan dan Perulangan Kompleks"

''' Beberapa tahun yang lalu belum pernah ada orang yang membuat program ATM sederhana. Jika kita ingin melakukan transaksi seperti
setor, penarikan, dan transfer uang harus antri lama di bank. Karena kebanyakan orang itu ingin melakukan pekerjaan yang cepat dan praktis,
kemudian ada seorang yang bernama Zul ingin mencoba membuat program ATM agar dapat mempermudah proses transaksi. Bantulah Zul dalam membuat
program ATM sederhana tersebut. '''

'''
Input  : menginputkan pin, pilihan menu, nominal uang, nomor rekening tujuan, pilihan mengeluarkan kartu/tidak

Proses : penghitungan saldo

Output : setelah melakukan transaksi selalu ditampilkan hasil penghitungan saldo terbaru, jika transaksi selesai akan ditampilkan kalimat
terima kasih atas kunjungan Anda

'''
saldo = 1000000
setor = 0
tarik = 0
nominal = 0
print("=== SELAMAT DATANG DI ATM ===")
pin=int(input("Masukkan pin Anda: "))
while True:
    print("1. Setor Tunai\n2. Penarikan\n3. Transfer\n4. Keluar")
    menu=int(input("Masukkan menu yang Anda inginkan [1-4]: "))
    if menu==1:
        setor=int(input("Masukkan jumlah uang yang ingin ditabung: Rp "))
        saldo=saldo+setor
        print("Setoran Anda telah diterima")
        print("Saldo Anda saat ini Rp ",saldo)
        pil=input("Apakah Anda ingin mengeluarkan kartu [Y/T]: ")
        if pil == "Y":
            print("Terima kasih atas kunjungan Anda")
            break
    elif menu==2:
        tarik=int(input("Penarikan: Rp "))
        if tarik>saldo:
            print("Saldo Anda tidak mencukupi untuk melakukan transaksi ini")
        else:
            saldo=saldo-tarik
            print("Saldo Anda saat ini Rp "+str(saldo))
            pil=input("Apakah Anda ingin mengeluarkan kartu [Y/T]: ")
            if pil == "Y":
                print("Terima kasih atas kunjungan Anda")
                break
    elif menu==3:
        norek=int(input("Masukkan Nomor Rekening Tujuan: "))
        nominal=int(input("Nominal yang akan di Transfer: Rp "))
        if nominal > saldo:
            print("Saldo Anda tidak mencukupi untuk melakukan transaksi ini")
        else:
            saldo=saldo-nominal
            print("Transfer ke Nomor Rekening",norek,"Berhasil")
            print("Saldo Anda saat ini Rp ",saldo)
            pil=input("Apakah Anda ingin mengeluarkan kartu [Y/T]: ")
            if pil =="1":
                print("Terima kasih atas kunjungan Anda")
                break
    elif menu==4:
        pil=input("Apakah Anda ingin mengeluarkan kartu [Y/T]: ")
        if pil =="Y":
            print("Terima kasih atas kunjungan Anda")
            break
    else:
        print("Menu yang Anda masukkan tidak tersedia")
        continue