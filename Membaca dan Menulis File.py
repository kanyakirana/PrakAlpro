# Nama-NIM : Kanya Kirana Litasari-71200666
# Informatika - Universitas Kristen Duta Wacana 
# Topik : "Membaca dan Menulis File"

''' Savira mempunyai Toserba yang baru saja buka bernama Rejeki. Karena karyawannya masih sedikit, Ia ingin membuat program yang bisa
membuka file txt yang berisi kode, nama, dan qty barang untuk mempermudah karyawannya dalam mengecek data barang. Program yang ingin 
dibuat oleh Savira yaitu seperti menambah, menghapus, dan melihat data barang yang ada pada toserba itu. Bantulah Savira dalam membuat
program tersebut. '''

'''
Input  : pilihan menu, jumlah jenis barang, kode barang, nama barang, qty barang, angka urutan barang

Proses : membuka file untuk menambah atau menghapus data barang

Output : menampilkan data barang

'''
print("=== TOSERBA REJEKI ===")
while True:
    print("1. Tambah Data Barang\n2. Hapus Data Barang\n3. Data Barang\n4. Keluar")
    no = int(input("Masukkan pilihan [1-4] : "))
    if no == 1:
        gabung = " "
        myfile = open("D:\\barang.txt","w")
        print(">>> TAMBAH DATA BARANG <<<")
        jenis = int(input("Berapa Jumlah Jenis Barang : "))
        j = 1
        for i in range(jenis):
            kode = input("Kode Barang : ")
            nama = input("Nama Barang : ")
            qty = input("QTY : ")
            if i == j:
                gabung += kode+"\t\t\t"+nama+"\t\t\t"+qty
            else:
                gabung += kode+"\t\t\t"+nama+"\t\t\t"+qty+"\n"
            j += 1
        myfile.write(gabung)
        myfile.close()
        print("Data berhasil ditambahkan")
    elif no == 2 :
        print(">>> HAPUS DATA BARANG <<<")
        tampung = " "
        myfile = open("D:\\barang.txt")
        hps = int(input("Masukkan urutan angka yang ingin dihapus datanya : "))
        iden = 1
        for i in myfile:
            if iden != hps and i != "\n":
                tampung += i + "\n"
            iden += 1
        myfile.close()
        # print(tampung)
        myfile = open("D:\\barang.txt","w")
        myfile.write(tampung)
        myfile.close()
        print("Data berhasil dihapus")
    elif no == 3:
        print(">>> DATA BARANG <<<")
        myfile = open("D:\\barang.txt","r")
        urut = 1
        for i in myfile:
            if i != "\n":
                print("No\tKode Barang\t\tNama Barang\t\t\tQTY")
                print(str(urut)+"\t"+i)
                urut += 1
    elif no == 4:
        print("Anda telah berhasil keluar")
        break
    else :
        print("Pilihan tidak tersedia, silahkan masukkan pilihan angka yang ada")
        continue