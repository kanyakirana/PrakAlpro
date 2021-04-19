# Nama-NIM : Kanya Kirana Litasari - 71200666
# Informatika - Universitas Kristen Duta Wacana 
# Topik : "Tipe Data List"

''' Nessa adalah salah satu guru di SMA N 1 Jaya. Karena zaman sekarang sudah mulai canggih, Ia ingin membuat program yang bisa menambah,
menghapus, dan melihat data siswa. Data yang ingin ditampilkan berisi nama, kelas, jurusan, nilai UH, nilai UTS, nilai UAS, dan rerata 
nilai yang muncul otomatis setelah diinputkan ketiga nilai itu. Bantulah Nessa dalam membuat program tersebut. '''

'''
Input  : pilihan menu, banyak siswa, nama, kelas, jurusan, nilai UH, nilai UTS, nilai UAS, nama siswa yang ingin dihapus datanya

Proses : menambah atau menghapus data siswa dan penghitungan rerata nilai

Output : menampilkan data siswa

'''
siswa = []
while True:
    print("=== SMA N 1 JAYA ===")
    print("1. Tambah Data Siswa\n2. Hapus Data Siswa\n3. Tampilkan Data Siswa\n4. Keluar")
    pil = int(input("Masukkan Pilihan [1-4] : "))
    if pil == 1:
        print(">>> TAMBAH DATA SISWA <<<")
        banyak = int(input("Berapa banyak siswa : "))
        for i in range(banyak):
            print("Data ke-"+str(i+1))
            nama = input("Nama : ").title()
            kelas = int(input("Kelas : "))
            jurusan = input("Jurusan [IPA/IPS/BAHASA] : ").upper()
            uh = float(input("Nilai UH : "))
            uts = float(input("Nilai UTS : "))
            uas = float(input("Nilai UAS : "))
            rerata = (uh+uts+uas)/3
            siswa.append([nama,kelas,jurusan,uh,uts,uas,round(rerata,2)])
        print("Data siswa berhasil ditambahkan")
    elif pil == 2 :
        print(">>> HAPUS DATA SISWA <<<")
        hapus = input("Nama siswa yang ingin dihapus datanya : ").title()
        for i in siswa:
            if hapus in i:
                siswa.remove(i)
                print("Data siswa bernama",hapus,"berhasil dihapus")
            else:
                print("Data siswa bernama",hapus,"tidak ditemukan")
    elif pil == 3 :
        print(">>> DATA SISWA <<<")
        print(95*"-")
        print("Nama\tKelas\tJurusan\t\tNilai UH\tNilai UTS\tNilai UAS\tRerata Nilai")
        print(95*"-")
        for i in siswa:
            print(i[0],end="\t")
            print(i[1],end="\t")
            print(i[2],end="\t\t")
            print(i[3],end="\t\t")
            print(i[4],end="\t\t")
            print(i[5],end="\t\t")
            print(i[6])
    elif pil == 4 :
        print("Anda telah berhasil keluar")
        break
    else:
        print("Pilihan tidak tersedia")
        continue