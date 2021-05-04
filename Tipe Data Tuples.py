# Nama - NIM : Kanya Kirana Litasari - 71200666
# Informatika - Universitas Kristen Duta Wacana 
# Topik : "Tipe Data Tuples"

''' Hana mempunyai cafe yang bernama Estuary Coffee. Ia mempunyai ide untuk membuat program pemesanan menu untuk pelanggan cafenya agar 
dapat memesan secara pribadi lewat teknologi seperti tablet. Jika pelanggan tersebut berhasil melakukan pemesanan maka akan otomatis keluar
nota yang dipesannya itu, sehingga pelanggan itu tidak usah menyebutkan apa yang dipesannya di depan pelayan kasir. Bantulah Hana dalam
membuat program itu yang menampilkan jenis menu yang dibeli, harga satuan, jumlah beli, total harga tiap jenis menu, ppn, total bayar, dan
kalimat terima kasih telah melakukan pemesanan silahkan bayar di kasir '''

'''
Input  : jumlah jenis menu yang dibeli, kode menu, jumlah beli, pilihan order ulang/tidak

Proses : penghitungan total harga tiap jenis menu, ppn, dan total bayar

Output : menampilkan jenis menu yang dibeli, harga satuan, jumlah beli, total harga tiap jenis menu, ppn, total bayar, dan
kalimat terima kasih telah melakukan pemesanan silahkan bayar di kasir

'''
order = "Y"
while True :
    print("""
            Estuary Coffee
    ==================================
    Kode  Menu\t\tHarga Satuan
    ==================================
    A    Kopi Susu\tRp 18.000
    B    Kopi Coklat\tRp 20.000
    C    Vanilla Latte\tRp 23.000
    D    Matcha Latte\tRp 25.000
    """)

    menu = ["","","",""]
    jml = [0,0,0,0]
    harga = [0,0,0,0]

    minuman = (1,2,3,4)
    kode = ("A","B","C","D")

    kode_menu = {"A":"Kopi Susu","B":"Kopi Coklat","C":"Vanilla Latte","D":"Matcha Latte"}
    kode_harga = {"A":18000,"B":20000,"C":23000,"D":25000}

    total = 0
    jenis = int(input("Berapa jenis menu yang dibeli [1-4] : "))
    if jenis not in minuman :
        print("Maaf, hanya ada 4 jenis menu saja")
        continue
    for i in range(jenis):
        pesan = input("Masukkan kode menu jenis " +str(i+1)+" [A-D] : ").upper()
        jml [i] = int(input("Jumlah beli : "))
        if pesan in kode:
            menu [i] = kode_menu[pesan]
            harga [i] = kode_harga[pesan]
        else :
            menu [i] = "Menu tidak tersedia"
            harga [i] = 0
    for j in range(jenis):
        print(45*"-")
        print("Jenis Menu ",j+1, ":", menu[j])
        print("Harga Jenis Menu ",j+1, ": Rp", harga[j])
        print("Jumlah Beli Jenis Menu ",j+1, ":", jml[j])
        print("Total Harga Jenis Menu ",j+1, ": Rp", harga[j]*jml[j])
        print(45*"-")
        total += harga[j]*jml[j]
        ppn = total * 0.1
        tot = total + ppn
    print("PPN(10%) : Rp", ppn)
    print("Total Bayar : Rp", tot)
    print("Terima kasih telah melakukan pemesanan dan silahkan bayar di kasir")
    order = input("Apakah ingin order kembali [Y/T] : ").upper()
    if order == "T":
        break