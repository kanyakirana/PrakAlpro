# Nama-NIM : Kanya Kirana Litasari-71200666
# Informatika - Universitas Kristen Duta Wacana 
# Topik : "Perulangan"

''' Vina mempunyai warung yang menjual aneka jajanan pasar bernama Warung Murah Meriah. Karena warung tersebut memiliki konsumen yang 
banyak tetapi pekerjanya sedikit Ia kerepotan menulis tangan nota penjualan untuk konsumennya. Kemudian Ia ingin membuat nota pada 
program kasir sederhana yang menampilkan jenis menu yang dibeli, harga satuan, jumlah beli, total harga, dan total bayar. 
Bantulah Vina dalam pembuatan nota pada program kasir sederhana menggunakan perulangan. '''

'''
Input  : jumlah jenis menu yang dibeli, kode menu, jumlah beli, pilihan order ulang/tidak

Proses : penghitungan total harga dan total bayar

Output : menampilkan jenis menu yang dibeli, harga satuan, jumlah beli, total harga, total bayar, kalimat terima kasih atas kunjungan anda

'''

bela = "Ya"
while True :
    print("""                           === WARUNG MURAH MERIAH ===
    -----------------------------------------------------------------------------------
    KODE\t\tMenu\t\t\t\t\tHarga Satuan
    -----------------------------------------------------------------------------------
    A\t\t\tMartabak\t\t\t\tRp 2.000
    B\t\t\tTerang Bulan Mini\t\t\tRp 2.500
    C\t\t\tPie Buah\t\t\t\tRp 1.500
    D\t\t\tPudding\t\t\t\t\tRp 3.000""")

    pesanan=[]
    harga=[]
    jumlah=[]

    tot = 0 
    jenis = int(input("Jenis menu yang ingin dibeli [1-4] : "))
    if jenis > 4 :
        print("Maaf, hanya ada 4 jenis menu saja")
        continue
    for i in range(jenis):
        kode=input("Masukkan kode menu jenis "+str(i+1)+" [A-D] : ")
        beli=int(input("Jumlah beli : "))
        def total(a,b):
            t=a*b
            return t
        if kode == "A":
            pesanan.append('Martabak')
            harga.append(2000)
            jumlah.append(beli) 
        elif kode == "B":
            pesanan.append('Terang Bulan Mini')
            harga.append(2500)
            jumlah.append(beli)
        elif kode == "C":
            pesanan.append('Pie Buah')
            harga.append(1500)
            jumlah.append(beli)
        elif kode == "D":
            pesanan.append('Pudding')
            harga.append(3000)
            jumlah.append(beli)
        else:
            print("Menu tidak tersedia")
    for j in range(0,jenis):
        print("----------------------------------------------")
        print("Jenis Menu",j+1, ":",pesanan[j]) 
        print("Harga Jenis Menu",j+1, ":",harga[j]) 
        print("Jumlah Beli Jenis Menu",j+1,":",jumlah[j]) 
        print("Total Harga Jenis Menu",j+1,":",total(harga[j],jumlah[j]))
        print("----------------------------------------------")
        tot += total(harga[j],jumlah[j])
    print("Total Bayar : ",tot)
    print("Terima Kasih Kunjungan Anda")
    bela = input("Apakah Anda ingin order kembali [Ya/Tidak] : ")
    if bela == "Tidak":
        break