# Nama - NIM : Kanya Kirana Litasari - 71200666
# Informatika - Universitas Kristen Duta Wacana 
# Topik : "Tipe Data Set"

''' Christin adalah ibu yang memiliki seorang anak kelas 7 SMP. Selama pandemi ini, Ia kerepotan untuk mengkoreksi PR anaknya karena
pelajaran anak SMP sekarang sudah mulai sulit. Karena kelas 7 SMP ada pelajaran matematika tentang himpunan, kemudian Ia ingin mencoba 
membuat program himpunan untuk mendapatkan hasil dari operasi irisan/gabungan/komplemen dari kedua data, agar setelah PR itu dikerjakan 
oleh anaknya Ia dapat mengkoreksi dengan cepat. Bantulah Christin dalam membuat program tersebut '''

'''
Input  : pilihan menu, jumlah anggota datanya, data 1 dan data 2

Proses : mengubah data menggunakan set untuk mencari irisan/gabungan/komplemen dari kedua data

Output : menampilkan data hasil dari operasi himpunannya

'''
while True:
    print("=== PROGRAM HIMPUNAN ===\n1. Irisan\n2. Gabungan\n3. Komplemen\n4. Keluar")
    pil = int(input("Masukkan pilihan [1-4] : "))
    if pil == 1:
        print(">> IRISAN <<")
        da1 = int(input("Jumlah anggota Data 1 : "))
        print("Data 1 :")
        l1 = []
        for i in range(da1):
            a = input()
            l1.append(a)
        da2 = int(input("Jumlah anggota Data 2: "))
        print("Data 2 :")
        l2 = []
        for i in range(da2):
            b = input()
            l2.append(b)
        irisan = set(l1) & set(l2)
        print("Irisan dari kedua data adalah",irisan)
    elif pil == 2:
        print(">> GABUNGAN <<")
        dat1 = int(input("Jumlah anggota Data 1 : "))
        print("Data 1 :")
        ls1 = []
        for i in range(dat1):
            c = input()
            ls1.append(c)
        dat2 = int(input("Jumlah anggota Data 2 : "))
        print("Data 2 :")
        ls2 = []
        for i in range(dat2):
            d = input()
            ls2.append(d)
        gabungan = set(ls1) | set(ls2)
        print("Gabungan dari kedua data adalah", gabungan)
    elif pil == 3:
        print(">> KOMPLEMEN <<")
        data1 = int(input("Jumlah anggota Data 1 : "))
        print("Data 1 :")
        lst1 = []
        for i in range(data1):
            e = input()
            lst1.append(e)
        data2 = int(input("Jumlah anggota Data 2 : "))
        print("Data 2 :")
        lst2 = []
        for i in range(data2):
            f = input()
            lst2.append(f)
        komplemen = set(lst1) ^ set(lst2)
        print("Komplemen dari kedua data adalah", komplemen)
    elif pil == 4:
        print("Anda telah keluar dari program himpunan")
        break
    else:
        print("Menu tidak tersedia")
        continue