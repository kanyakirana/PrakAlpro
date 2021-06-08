# Nama - NIM : Kanya Kirana Litasari - 71200666
# Informatika - Universitas Kristen Duta Wacana 
# Topik : "Regular Expression"

''' Vira adalah seorang mahasiswa Informatika. Ia mempunyai tugas kuliah dalam materi regex. Kemudian Ia ingin membuat program untuk 
mengecek dalam inputan nama panggilan dengan syarat 3-30 karakter dan tidak boleh ada spasinya, mengecek email harus ada simbol @, 
mengecek password dengan syarat 6-20 karakter tidak boleh ada spasi terdiri atas huruf kapital dan huruf kecil dan menggunakan angka/simbol, 
dan mengecek pin atm harus berupa angka. Lalu, semua inputan yang sudah dicek tadi jika benar akan dituliskan ke dalam file txt yang jika
dibuka kapanpun akan tersedia inputannya tadi. Bantulah Vira dalam membuat program itu '''

'''
Input  : nama, email, password, pin atm

Proses : fungsi cek nama, cek email, cek password, cek pin atm, main untuk menjalankan fungsinya, dan menulis inputan yang sudah dicek
tadi dalam file txt

Output : nama, email, password, pin atm, file txt yang menampilkan nama, email, password, pin atm

'''
import re

list = []
nama = input("Nama Panggilan : ")
email = input("Email : ")
password = input("Password : ")
pinatm = input("Pin ATM Anda : ")

def ceknama(nama):
    if(len(nama)) >= 3 and (len(nama)) <= 30 and not (re.search("\s",nama)):
        print(nama)
    else:
        print("Nama gagal dibuat")

def cekemail(email):
    if (re.findall("@",email)):
        print("Email valid")
        print(email)
    else:
        print("Email invalid")

def cekpass(password):
    if(len(password))>= 6 and (len(password)) <= 30 and not (re.search("\s",password)):
        if(re.search("A-Z",password)) and (re.search("a-z",password)) and (re.search("|0-9|", password)) or (re.search("\S$",password)):
            print("Password berhasil dibuat")
            print(password)
            list.append(nama)
            list.append(email)
            list.append(password)
        else:
            print("Password masih lemah")
    else:
        print("Password tidak sesuai dengan ketentuan")

def cekpin(pinatm):
    if(re.search("|0-9|",pinatm)):
        print("Pin valid")
        print(pinatm)
        list.append(pinatm)
    else:
        print("Pin invalid")

def main():
    ceknama(nama)
    cekemail(email)
    cekpass(password)
    cekpin(pinatm)

    textfile = open("D:\\registrasi.txt","w")
    for i in list:
        textfile.write(i+"\n")
    textfile.close
main()