# Nama-NIM : Kanya Kirana Litasari-71200666
# Informatika - Universitas Kristen Duta Wacana 
# Topik : "String"

''' Vanessa Adelia Christy adalah mahasiswi di UKDW. Ia diminta untuk membuat program dalam SSAT UKDW khusus untuk mahasiswa baru. Ia 
berencana membuat program tersebut awalnya menampilkan proses dalam pembuatan password yang ditentukan oleh program. Jika password sudah 
diketahui maka mahasiswa baru tersebut dapat login untuk mengisikan username dan password yang sudah ditentukan tadi. Setelah itu, jika Ia 
berhasil login maka Ia dapat memilih beberapa menu yang ditampilkan seperti pengisian biodata, ubah password, dan logout. 
Bantulah Vanessa dalam pembuatan program SSAT UKDW tersebut! '''

'''
Input  : nama, nim, pilihan menu, username, password, biodata

Proses : menentukan password, login, pengubahan password

Output : menampilkan program untuk menentukan password, login, menampilkan menu yang terdiri atas pengisian biodata, ubah password, dan
logout

'''
print(""" === SSAT UKDW === """)
#password
namdep = input("Nama Depan : ")
nambel = input("Nama Belakang : ")
nim = input("NIM [3 Digit Belakang] : ")
passw = ""
if (len(nim) != 3):
    print("Masukkan NIM 3 Digit Belakang")
else :
    if (len(namdep) > 2):
        passw += namdep[:3]
    else :
        passw += namdep

    if (len(nambel) > 2):
        passw += nambel[:2]
    else :
        passw += nambel
    passw += nim
print("Password : ",passw)
#login
while True :
    print("LOGIN SSAT UKDW")
    username = input("Username (Nama Depan) : ").upper()
    password = input("Password : ")
    if password != passw:
        continue
    while True :
        print("SELAMAT DATANG",username)
        print("A. Pengisian Biodata\nB. Ubah Password\nC. Logout")
        pil = input("Masukkan Pilihan Menu [A-C] : ").upper()
        if pil == "A":
            print("PENGISIAN BIODATA MAHASISWA")
            nama = input("Nama Lengkap : ")
            tl = input("Tempat Lahir : ")
            tgl = input("Tanggal Lahir [dd-mm-yyyy] : ")
            agama = input("Agama : ")
            almt = input("Alamat : ")
            kota = input("Kota/Kabupaten : ")
            prop = input("Propinsi : ")
            while True :
                data = input("Apakah semua data yang Anda masukkan sudah benar [Y/T] : ").upper()
                if data == "Y":
                    print("Biodata Anda telah berhasil disimpan")
                    break
                else :
                    continue
        elif pil == "B":
            print("UBAH PASSWORD")
            #pengubahan password
            a = input("Password Lama : ")
            b = input("Password Baru : ")
            passw = passw.replace(a,b)
            print("Pengubahan password menjadi",passw,"telah berhasil disimpan")
        elif pil == "C":
            print("Anda telah keluar dari SSAT UKDW")
            break
        else :
            print("Menu tidak tersedia")
            continue