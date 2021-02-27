# Nama : Kanya Kirana Litasari
# Informatika - Universitas Kristen Duta Wacana 
# Topik : "Fungsi"

''' Tiva adalah ibu yang memiliki seorang anak kelas 6 SD. Selama pandemi ini, Ia kerepotan untuk mengkoreksi PR anaknya karena
pelajaran anak SD sekarang sudah mulai sulit. Karena kelas 6 SD ada pelajaran matematika tentang bangun ruang, kemudian Ia ingin mencoba 
untuk membuat program kalkulator penghitung volume dan luas permukaan bangun ruang, agar setelah PR itu dikerjakan oleh anaknya Ia dapat
mengkoreksi dengan cepat. Bantulah Tiva dalam pembuatan kalkulator penghitung volume dan luas permukaan bangun ruang. '''

'''
Input  : pilihan bangun ruang, pilihan volume/luas permukaan, sisi-sisi yang akan dihitung pada bangun ruang

Proses : penghitungan rumus volume dan luas permukaan bangun ruang

Output : menampilkan hasil perhitungan volume/luas permukaan bangun ruang

'''

def kubus_volume(s):
    vk=s**3
    return vk
def kubus_luas(s):
    lk=6*s**2
    return lk
def balok_volume(p,l,t):
    vb=p*l*t
    return vb
def balok_luas(p,l,t):
    lb=(2*(p*l)+(p*t)+(l*t))
    return lb
def tabung_volume(p,r,t):
    vt=p*r**2*t
    return vt
def tabung_luas(p,r,t):
    lt=2*p*r*(r+t)
    return lt

print("""=== Kalkulator Penghitung Volume/Luas Permukaan Pada Bangun Ruang ===
1. Kubus\n2. Balok\n3. Tabung""")
p=str(input("Masukkan Pilihan Bangun Ruang [1-3] : "))
if p == "1":
    print("1.Volume Kubus\n2.Luas Permukaan Kubus")
    pi=str(input("Masukkan Pilihan [1-2] : "))
    if pi == "1":
        si=eval(input("Masukkan sisi Kubus : "))
        print("Volume Kubus dengan sisi",si,"adalah",kubus_volume(si))
    elif pi=="2":
        si=eval(input("Masukkan sisi Kubus: "))
        print("Luas Permukaan Kubus dengan sisi",si,"adalah",kubus_luas(si))
    else:
        print("Pilihan tidak tersedia")
elif p=="2":
    print("1.Volume Balok\n2.Luas Permukaan Balok")
    pi=str(input("Masukkan pilihan [1-2] : "))
    if pi == "1":
        pj=eval(input("Masukkan panjang Balok : "))
        le=eval(input("Masukkan lebar Balok : "))
        ti=eval(input("Masukkan tinggi Balok : "))
        print("Volume Balok dengan panjang",pj,"lebar",le,"dan tinggi",ti,"adalah",balok_volume(pj,le,ti))
    elif pi == "2":
        pj=eval(input("Masukkan panjang Balok : "))
        le=eval(input("Masukkan lebar Balok : "))
        ti=eval(input("Masukkan tinggi Balok : "))
        print("Luas Permukaan Balok dengan panjang",pj,"lebar",le,"dan tinggi",ti,"adalah",balok_luas(pj,le,ti))
    else :
        print("Pilihan tidak tersedia")
elif p=="3":
    print("1.Volume Tabung\n2.Luas Permukaan Tabung")
    pi=str(input("Masukkan pilihan [1-2] : "))
    if pi == "1":
        phi=eval(input("Masukkan phi : "))
        r=eval(input("Masukkan jari-jari Tabung : "))
        t=eval(input("Masukkan tinggi Tabung : "))
        print("Volume Tabung dengan phi",phi,"jari-jari",r,"dan tinggi",t,"adalah",tabung_volume(phi,r,t))
    elif pi == "2":
        phi=eval(input("Masukkan phi : "))
        r=eval(input("Masukkan jari-jari Tabung : "))
        t=eval(input("Masukkan tinggi Tabung : "))
        print("Luas Permukaan Tabung dengan phi",phi,"jari-jari",r,"dan tinggi",t,"adalah",tabung_luas(phi,r,t))
    else : 
        print("Pilihan tidak tersedia")
else :
    print("Pilihan yang diinputkan tidak tersedia")