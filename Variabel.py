# Nama : Kanya Kirana Litasari
# Informatika - Universitas Kristen Duta Wacana
# Topik : "Variabel"

''' Vanessa memiliki sebuah cafe baru yang menjual 4 menu minuman yaitu Kopi Susu (Rp 18.000), Kopi Americano (Rp 15.000), 
Kopi Latte (Rp 20.000), dan Caramel Macchiato (Rp 23.000). Setiap pembelian dikenakan pajak sebesar 10 %. Karena sedang ada
promo maka setiap pembelian minuman Caramel Macchiato diskon sebesar 20%. Kemudian ada pembeli yang bernama Savira yang hanya
membawa uang sebesar Rp 60.000 ingin membeli Kopi Susu berjumlah 3 gelas untuk diminum ditempat. Setelah itu ada pelanggan yang 
bernama Naufal membawa uang sebesar Rp 250.000 ingin membeli Caramel Macchiato berjumlah 8 gelas untuk dibawa pulang. 
Bantulah Vanessa membuat struk penjualan untuk pelanggan yang bernama Savira dan Naufal pada program kasir sederhana.
'''

'''

Input  : nama pelanggan, jenis penghidangan, pesanan, jumlah pesanan, harga satuan, diskon, uang tunai pembeli

Proses : penghitungan harga, penghitungan diskon, penghitungan pajak, penghitungan total harga, penghitungan kembalian

Output : menampilkan pesanan, jumlah pesanan, harga, diskon, pajak, total harga, uang tunai pembeli, kembalian

'''
print("""
             HAYATI COFFEE
Jalan Jendral Sudirman No 27, Yogyakarta
""")
print("----------------------------------")
nama=input("Nama Pelanggan : ")
jenispenghidangan=input("Dine In/Take Away : ")
pesanan=input("Pesanan Anda : ")
jumlahpesanan=int(input("Jumlah Pesanan : "))
hargasatuan=int(input("Harga Satuan : "))
diskon=eval(input("Diskon : "))
uangtunai=int(input("Uang Tunai Pembeli : "))

#Penghitungan Harga
harga=hargasatuan*jumlahpesanan
#Penghitungan Diskon
hitungdiskon=int(harga*diskon)
#Penghitungan Pajak
ppn=int(harga*0.1)
#Penghitungan Total Harga
totalharga=int(harga+ppn-diskon)
#Penghitungan Kembalian
kembalian=int(uangtunai-totalharga)

print("------------------------------")
print("Pesanan : ", pesanan)
print("Jumlah Pesanan : ", jumlahpesanan)
print("Harga : Rp ", harga)
print("Diskon : Rp ", hitungdiskon)
print("PPN (10%) : Rp ", ppn)
print("-----------------------------")
print("Jumlah Bayar : Rp ", totalharga)
print("Kembalian : Rp ", kembalian)
print("----------------------------")
print("TERIMA KASIH ATAS KUNJUNGAN ANDA")