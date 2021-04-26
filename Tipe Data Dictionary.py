# Nama - NIM : Kanya Kirana Litasari - 71200666
# Informatika - Universitas Kristen Duta Wacana 
# Topik : "Tipe Data Dictionary"

''' Vira mempunyai bisnis baru yang menjual aneka jajanan pasar bernama Violet Snacks. Karena sekarang sedang bulan puasa sehingga banyak 
sekali konsumen yang membeli, Ia ingin mempermudah para pekerjanya untuk melayani konsumen tersebut dalam membuat nota penjualan. Karena
sampai saat ini bisnis yang dibangunnya itu masih menulis tangan nota penjualannya sehingga mengakibatkan konsumennya menunggu lama. Lalu 
Vira mempunyai ide untuk membuat program dalam pembuatan nota yang menampilkan jumlah beli tiap jenis menu dikali harga satuan, total harga 
tiap jenis menu, dan total bayar. Bantulah Vira dalam membuat program tersebut '''

'''
Input  : jumlah jenis menu yang dibeli, kode menu, jumlah beli, pilihan order ulang/tidak

Proses : penghitungan total harga tiap jenis menu dan total bayar

Output : menampilkan jumlah beli tiap jenis menu kemudian dikali harga satuan, total harga tiap jenis menu, total bayar, kalimat terima
kasih atas kunjungan anda

'''
order = "Y"
while True:
    print("""               === VIOLET SNACKS ===
    -----------------------------------------
    Kode\tMenu\t\tHarga Satuan
    -----------------------------------------
    A\t\tPastel\t\tRp 2.000
    B\t\tRisol\t\tRp 2.500
    C\t\tPudding\t\tRp 4.000
    D\t\tPie Buah\tRp 1.500
    E\t\tMartabak\tRp 3.000""")

    pesanan = {}
    kode_nama = {'A':'Pastel','B':'Risol','C':'Pudding','D':'Pie Buah','E':'Martabak'}
    kode_harga = {'A':2000,'B':2500,'C':4000,'D':1500,'E':3000}

    jenis = int(input("Berapa jenis menu yang dibeli [1-5] : "))
    if jenis > 5 :
        print("Maaf, hanya ada 5 jenis menu saja")
        continue
    for i in range(jenis):
        kode = input("Kode menu jenis "+str(i+1)+" [A-E] : ").upper()
        beli = int(input("Jumlah beli : "))
        print()
        if kode in kode_nama:
            pesanan[kode] = beli
        else:
            while kode not in kode_nama:
                print("Menu tidak tersedia")
                kode = input("Kode menu jenis "+str(i+1)+" [A-E] : ").upper()
                beli = int(input("Jumlah beli : "))
                print()
            pesanan[kode] = beli
    total = 0
    for j in pesanan:
        print(50*"-")
        print("Jenis Menu",kode_nama[j],"\t",pesanan[j],"x",kode_harga[j],"\t= Rp",pesanan[j]*kode_harga[j])
        total += pesanan[j]*kode_harga[j]
    print(50*"-")
    print("Total Bayar\t\t\t\t= Rp",total)
    print("Terima Kasih Atas Kunjungan Anda\n")
    order = input("Apakah ingin order kembali [Y/T] : ").upper()
    if order == "T":
        break