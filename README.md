data_pasien = [
    {'kode' : 'P001',
     'nama' : 'Andi Malarang',
     'jenis_kelamin' : 'Pria',
     'usia' : 30,
     'alamat' : 'Jl. Jeruk',
     'ruang' : 'Mawar'},

     {'kode' : 'P002',
     'nama' : 'Budi Sutrisno',
     'jenis_kelamin' : 'Pria',
     'usia' : 45,
     'alamat' : 'Jl. Semangka',
     'ruang' : 'Mawar'},

     {'kode' : 'P003',
     'nama' : 'Caca Marica',
     'jenis_kelamin' : 'Wanita',
     'usia' : 10,
     'alamat' : 'Jl. Apel',
     'ruang' : 'Melati'}]

def back_read():
# Pernyataan untuk kembali ke menu utama
    utm = input("Ketik 0 untuk kembali ke menu utama : ")
    while True:
        if utm == "0":
            main_menu1 ()
        else:
            read()
        break

## READ
def read() :
# Mencetak semua data dengan pilihan kembali ke menu utama
    print ('''==========================================
DAFTAR PASIEN RAWAT INAP RS BAHAGIA SELALU
==========================================''')
    print("NO\tNO PENDAFTARAN\tNAMA PASIEN\t\tJENIS KELAMIN\tUSIA\tALAMAT\t\tKAMAR")
    global data_pasien
    for i in range(len(data_pasien)) :
        print(f"{i+1}\t{data_pasien[i]['kode']}\t\t{data_pasien[i]['nama']}\t\t{data_pasien[i]['jenis_kelamin']}\t\t{data_pasien[i]['usia']}\t{data_pasien[i]['alamat']}\t{data_pasien[i]['ruang']}")
    back_read()

def read1() :
# Mencetak semua data saja
    print ('''==========================================
DAFTAR PASIEN RAWAT INAP RS BAHAGIA SELALU
==========================================''')
    print("NO\tNO PENDAFTARAN\tNAMA PASIEN\t\tJENIS KELAMIN\tUSIA\tALAMAT\t\tKAMAR")
    global data_pasien
    for i in range(len(data_pasien)) :
        print(f"{i+1}\t{data_pasien[i]['kode']}\t\t{data_pasien[i]['nama']}\t\t{data_pasien[i]['jenis_kelamin']}\t\t{data_pasien[i]['usia']}\t{data_pasien[i]['alamat']}\t{data_pasien[i]['ruang']}")

def read2() :
# Mencetak data
    print("NO PENDAFTARAN\tNAMA PASIEN\t\tJENIS KELAMIN\tUSIA\tALAMAT\t\tKAMAR")
    print(f"{data_pasien['kode']}\t\t{data_pasien['nama']}\t\t{data_pasien['jenis_kelamin']}\t\t{data_pasien['usia']}\t{data_pasien['alamat']}\t{data_pasien['ruang']}")

## CREATE
# Membuat daftar data pasien baru
def create() :
    print ('''====================================================
PENDAFTARAN PASIEN RAWAT INAP BARU RS BAHAGIA SELALU
====================================================''')
    print("Masukkan data pasien")
    print(f"Kode Pasien terakhir adalah {data_pasien[-1]['kode']}")
    # global data_pasien
    add_no = (input("Kode \t: ")).capitalize()
    add_nama= (input("Nama Pasien : ")).title()
    add_jk = (input("Jenis Kelamin : ")).capitalize()
    add_usia = (input("Usia \t: "))
    add_alamat = (input("Alamat \t: ")).title()
    add_ruang = (input("Ruang \t: ")).capitalize()
    tabel_data = {'kode' : add_no,
                  'nama' : add_nama,
                  'jenis_kelamin' : add_jk,
                  'usia' : add_usia,
                  'alamat' : add_alamat,
                  'ruang' : add_ruang}
    data_pasien.append(tabel_data)
    print("Selamat data berhasil ditambahkan ^_^ ")

## UPDATE
# Mengedit daftar pasien yang sudah ada
def update() :
    global data_pasien
    read1()
    a = int(input("Pilih No pasiena yang akan di edit : "))
    counter = 0
    for i in data_pasien[a-1]:
        counter += 1
        print(f"{counter}. {i.capitalize()} \t: {data_pasien[a-1][i]}")
    b = int(input("Nomor mana yang mau di edit: "))
    if b == 1:
        data_pasien[a-1]['kode'] = input("Silahkan isi dengan data yang benar : ").upper()
    if b == 2:
        data_pasien[a-1]['nama'] = input("Silahkan isi dengan data yang benar : ").title()
    if b == 3:
        data_pasien[a-1]['jenis_kelamin'] = input("Silahkan isi dengan data yang benar : ").capitalize()
    if b == 4:
        data_pasien[a-1]['usia'] = input("Silahkan isi dengan data yang benar : ")
    if b == 5:
        data_pasien[a-1]['alamat'] = input("Silahkan isi dengan data yang benar : ").title()
    if b == 6:
        data_pasien[a-1]['ruang'] = input("Silahkan isi dengan data yang benar : ").title()
    counter = 0
    print("Selamat Data Berhasi diperbarui ^_^")
    for i in data_pasien[a-1]:
        counter += 1
        print(f"{counter}. \t {i} : {data_pasien[a-1][i]}")


## DELETE
# Menghapus data pasien
def delete(i):
    global data_pasien
    del data_pasien[i-1]


# # search
# def search(cari) :
#     global data_pasien
#     cari = input("Masukkan Nama Pasien : ")
#     x = data_pasien.find(cari)


## MAIN MENU
def main_menu1 ():
# Menu utama untuk user admin
    global data_pasien
    print ('''=============================================================
SELAMAT DATANG ADMIN DI MENU UTAMA APLIKASI RS BAHAGIA SELALU
=============================================================''')
    print ("1. Melihat daftar pasien")
    print ("2. Pendaftaran pasien rawat inap")
    print ("3. Edit data pasien")
    print ("4. Hapus pasien rawat inap")
    print ("5. Keluar program")

    menu = input("Masukkan nomor yang ingin dijalankan : ")
    while True:
        if menu == "1":
            read()
            # back_read()
        elif menu == "2":
            create()
            read()
        elif menu == "3":
            update()
            read()
        elif menu == "4":
            read1()
            i = int(input("Masukkan nomer pasien chekout : "))
            print(f"Data pasien {data_pasien[i-1]['kode']} sudah dihapus dari daftar rawat inap !")
            delete(i)
            read()
        elif menu == "5":
            print("Terima kasih, sampai jumpa kembali")
            dasbor()
        dasbor()

def main_menu2 ():
# Menu utama untuk user dokter
    global data_pasien
    print ('''==============================================================
SELAMAT DATANG DOKTER DI MENU UTAMA APLIKASI RS BAHAGIA SELALU
==============================================================''')
    print ("1. Melihat daftar pasien")
    print ("2. Keluar program")

    menu = input("Masukkan nomor yang ingin dijalankan : ")
    while True:
        if menu == "1":
            read()
            # back_read()
        elif menu == "2":
            print("Terima kasih, sampai jumpa kembali")
            dasbor()
        dasbor()

## DASHBOARD
# Tampilan pertama kali buka aplikasi
def dasbor():
    print('''============================================
SELAMAT DATANG DI APLIKASI RS BAHAGIA SELALU
============================================''')
    while True:
        print('''Silahkan Pilih User
            1. Admin
            2. Dokter
            3. Pasien''')
        usr = input("Ketik angka sesuai user : ")
        if usr == "1":
            print('''===========================================
SELAMAT DATANG USER ADMIN RS BAHAGIA SELALU
===========================================''')
        # Login user admin
            while True :
                user = input("Masukkan username anda : ")
                pasw = input("Masukkan password anda : ")
                if user == "admin" and pasw == "12":
                    main_menu1()
                else :
                    print("Username atau Password anda salah")
        elif usr == "2":
            print('''===========================================
SELAMAT DATANG USER DOKTER  RS BAHAGIA SELALU
===========================================''')
        # Login user dokter
            while True :
                user = input("Masukkan username anda : ")
                pasw = input("Masukkan password anda : ")
                if user == "dokter" and pasw == "12":
                    main_menu2()
                else :
                    print("Username atau Password anda salah")
        elif usr == "3":
            print("Mohon Maaf Aplikasi untuk user tersebut sedang dalam proses")
        else:
            print("Silahkan pilih user yang sudah ada")

dasbor()
