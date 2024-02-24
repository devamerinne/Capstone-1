data_pasien = [
    {'kode' : 'P001',
     'nama' : 'Andi Malarang',
     'jenis_kelamin' : 'Pria',
     'usia' : 30,
     'alamat' : 'Jl. Jeruk',
     'ruang' : 'Mawar',
     'penyakit' : 'Jantung'},

     {'kode' : 'P002',
     'nama' : 'Bili Wongka',
     'jenis_kelamin' : 'Pria',
     'usia' : 45,
     'alamat' : 'Jl. Semangka',
     'ruang' : 'Mawar',
     'penyakit' : 'Demam Berdarah'},

     {'kode' : 'P003',
     'nama' : 'Caca Marica',
     'jenis_kelamin' : 'Wanita',
     'usia' : 10,
     'alamat' : 'Jl. Apel',
     'ruang' : 'Melati',
     'penyakit' : 'Diabetes'}]

def back_read_admin():
# Pernyataan untuk kembali ke menu utama 
    utm = input("\nKetik 0 untuk kembali ke menu utama : ")
    while True:
        if utm == "0":
            main_menu_admin()
        else:
            read_admin()
        break

def back_read_dokter():
# Pernyataan untuk kembali ke menu utama
    utm = input("\nKetik 0 untuk kembali ke menu utama : ")
    while True:
        if utm == "0":
            main_menu_dokter()
        else:
            read_dokter()
        break

## HIASAN
def bintang():
    string = ""

    x = 3
    bar = x
    # Looping Baris
    while bar >= 0:
        # Looping Kolom Spasi Kosong
        kol = bar
        while kol > 0:
            string = string + "   "
            kol = kol - 1
        # Looping Kolom Bintang Sisi Kiri		
        kiri = 1
        while kiri < (x - (bar-1)):
            string = string + " * "
            kiri = kiri + 1		
        # Looping Kolom Bintang Sisi Kanan
        kanan = 1
        while kanan < kiri -1:
            string = string + " * "
            kanan = kanan + 1	

        string = string + "\n"
        bar = bar - 1

    bar = 1	
    # Looping Baris
    while bar <= x:
        kol = bar+1
        # Looping Kolom Spasi Kosong
        while kol > 1:
            string = string + "   "
            kol = kol - 1
        # Looping Kolom Bintang Sisi Kiri	
        kiri = 0
        while kiri < (x - bar):
            string = string + " * "
            kiri = kiri + 1	
        # Looping Kolom Bintang Sisi Kanan
        kanan = kiri	
        while kanan > 1:
            string = string + " * "
            kanan = kanan - 1

        string = string + "\n"
        bar = bar + 1
    print (string)


## READ
def read_admin() :
# Mencetak semua data dengan pilihan kembali ke menu utama
    print ('''\n==========================================
DAFTAR PASIEN RAWAT INAP RS BAHAGIA SELALU
==========================================\n''')
    print("--------------------------------------------------------------------------------------------------------")
    print("NO\tNO PENDAFTARAN\tNAMA PASIEN\t\tJENIS KELAMIN\tUSIA\tALAMAT\t\tKAMAR\tPENYAKIT")
    print("--------------------------------------------------------------------------------------------------------")
    global data_pasien
    for i in range(len(data_pasien)) :
        print(f"{i+1}\t{data_pasien[i]['kode']}\t\t{data_pasien[i]['nama']}\t\t{data_pasien[i]['jenis_kelamin']}\t\t{data_pasien[i]['usia']}\t{data_pasien[i]['alamat']}\t{data_pasien[i]['ruang']}\t{data_pasien[i]['penyakit']}")
        print("--------------------------------------------------------------------------------------------------------")
    back_read_admin()

def read_dokter() :
# Mencetak semua data dengan pilihan kembali ke menu utama
    print ('''\n==========================================
DAFTAR PASIEN RAWAT INAP RS BAHAGIA SELALU
==========================================\n''')
    print("--------------------------------------------------------------------------------------------------------")
    print("NO\tNO PENDAFTARAN\tNAMA PASIEN\t\tJENIS KELAMIN\tUSIA\tALAMAT\t\tKAMAR\tPENYAKIT")
    print("--------------------------------------------------------------------------------------------------------")
    global data_pasien
    for i in range(len(data_pasien)) :
        print(f"{i+1}\t{data_pasien[i]['kode']}\t\t{data_pasien[i]['nama']}\t\t{data_pasien[i]['jenis_kelamin']}\t\t{data_pasien[i]['usia']}\t{data_pasien[i]['alamat']}\t{data_pasien[i]['ruang']}\t{data_pasien[i]['penyakit']}")
        print("--------------------------------------------------------------------------------------------------------")
    back_read_dokter()

def read1() :
# Mencetak semua data saja
    print ('''\n==========================================
DAFTAR PASIEN RAWAT INAP RS BAHAGIA SELALU
==========================================\n''')
    print("--------------------------------------------------------------------------------------------------------")
    print("NO\tNO PENDAFTARAN\tNAMA PASIEN\t\tJENIS KELAMIN\tUSIA\tALAMAT\t\tKAMAR\tPENYAKIT")
    print("--------------------------------------------------------------------------------------------------------")
    global data_pasien
    for i in range(len(data_pasien)) :
        print(f"{i+1}\t{data_pasien[i]['kode']}\t\t{data_pasien[i]['nama']}\t\t{data_pasien[i]['jenis_kelamin']}\t\t{data_pasien[i]['usia']}\t{data_pasien[i]['alamat']}\t{data_pasien[i]['ruang']}\t{data_pasien[i]['penyakit']}")
        print("--------------------------------------------------------------------------------------------------------")

def read2() :
# Mencetak data
    print("NO PENDAFTARAN\tNAMA PASIEN\t\tJENIS KELAMIN\tUSIA\tALAMAT\t\tKAMAR\tPENYAKIT")
    print(f"{data_pasien['kode']}\t\t{data_pasien['nama']}\t\t{data_pasien['jenis_kelamin']}\t\t{data_pasien['usia']}\t{data_pasien['alamat']}\t{data_pasien['ruang']}\t{data_pasien[i]['penyakit']}")
    print("--------------------------------------------------------------------------------------------------------")


## CREATE
# Membuat daftar data pasien baru
def create() :
    print ('''\n====================================================
PENDAFTARAN PASIEN RAWAT INAP BARU RS BAHAGIA SELALU
====================================================''')
    print(f"Kode Pasien terakhir adalah {data_pasien[-1]['kode']}")
    print("Masukkan data pasien\n")
    # global data_pasien
    add_no = (input("Kode \t: ")).capitalize()
    add_nama= (input("Nama Pasien : ")).title()
    add_jk = (input("Jenis Kelamin : ")).capitalize()
    add_usia = (input("Usia \t: "))
    add_alamat = (input("Alamat \t: ")).title()
    add_ruang = (input("Ruang \t: ")).capitalize()
    add_penyakit = (input("Penyakit \t: ")).title()
    tabel_data = {'kode' : add_no,
                  'nama' : add_nama,
                  'jenis_kelamin' : add_jk,
                  'usia' : add_usia,
                  'alamat' : add_alamat,
                  'ruang' : add_ruang,
                  'penyakit' : add_penyakit}
    data_pasien.append(tabel_data)
    print("\nSelamat data berhasil ditambahkan ^_^")


## UPDATE
# Mengedit daftar pasien yang sudah ada
def update() :
    global data_pasien
    read1()
    a = int(input("\nPilih No pasien yang akan di edit : "))
    counter = 0
    for i in data_pasien[a-1]:
        counter += 1
        print(f"{counter}. {i.capitalize()} \t: {data_pasien[a-1][i]}")
    b = int(input("\nNomor mana yang mau di edit: "))
    if b == 1:
        data_pasien[a-1]['kode'] = input("\nSilahkan isi dengan kode pasien yang benar : ").upper()
    if b == 2:
        data_pasien[a-1]['nama'] = input("\nSilahkan isi dengan data nama pasien yang benar : ").title()
    if b == 3:
        data_pasien[a-1]['jenis_kelamin'] = input("\nSilahkan isi dengan data jenis kelamin pasien yang benar : ").capitalize()
    if b == 4:
        data_pasien[a-1]['usia'] = input("\nSilahkan isi dengan data usia pasien yang benar : ")
    if b == 5:
        data_pasien[a-1]['alamat'] = input("\nSilahkan isi dengan data alamat pasien yang benar : ").title()
    if b == 6:
        data_pasien[a-1]['ruang'] = input("\nSilahkan isi dengan data ruang yang benar : ").title()
    counter = 0
    print("\nSelamat Data Berhasi diperbarui ^_^\n")
    for i in data_pasien[a-1]:
        counter += 1
        print(f"{counter}. \t {i} : {data_pasien[a-1][i]}")


## DELETE
# Menghapus data pasien
def delete(i):
    global data_pasien
    del data_pasien[i-1]

# # SEARCH
def search_admin():
    global data_pasien
    while True:
        nm = input("\nMasukkan nama pasien: ").title()
        cari_nm = False
        for i in range(len(data_pasien)):
            if nm == data_pasien[i]['nama']:
                print("--------------------------------------------------------------------------------------------------------")
                print("NO\tNO PENDAFTARAN\tNAMA PASIEN\t\tJENIS KELAMIN\tUSIA\tALAMAT\t\tKAMAR\tPENYAKIT")
                print("--------------------------------------------------------------------------------------------------------")
                print(f"{i+1}\t{data_pasien[i]['kode']}\t\t{data_pasien[i]['nama']}\t\t{data_pasien[i]['jenis_kelamin']}\t\t{data_pasien[i]['usia']}\t{data_pasien[i]['alamat']}\t{data_pasien[i]['ruang']}\t{data_pasien[i]['penyakit']}")
                print("--------------------------------------------------------------------------------------------------------")
                cari_nm = True
                # back_read()
                print("\nKetik 1 untuk cari lagi\nKetik 0 untuk kembali ke menu")
                pilih = input("Silahkan pilih : ")
                if pilih == "1":
                    search_admin()
                if pilih == "0":
                    main_menu_admin()
        if cari_nm  == False:
            print(f"\nNama pasien {nm} tidak ditemukan !!! \nMungkin pasien sudah pulang atau coba lengkapi nama pasien yang dicari.")
            print("\nKetik 1 untuk cari lagi\nKetik 0 untuk kembali ke menu")
            pilih = input("Silahkan pilih : ")
            if pilih == "1":
                search_admin()
            if pilih == "0":
                main_menu_admin()

def search_dokter():
    global data_pasien
    while True:
        nm = input("\nMasukkan nama pasien: ").title()
        cari_nm = False
        for i in range(len(data_pasien)):
            if nm == data_pasien[i]['nama']:
                print("--------------------------------------------------------------------------------------------------------")
                print("NO\tNO PENDAFTARAN\tNAMA PASIEN\t\tJENIS KELAMIN\tUSIA\tALAMAT\t\tKAMAR\tPENYAKIT")
                print("--------------------------------------------------------------------------------------------------------")
                print(f"{i+1}\t{data_pasien[i]['kode']}\t\t{data_pasien[i]['nama']}\t\t{data_pasien[i]['jenis_kelamin']}\t\t{data_pasien[i]['usia']}\t{data_pasien[i]['alamat']}\t{data_pasien[i]['ruang']}\t{data_pasien[i]['penyakit']}")
                print("--------------------------------------------------------------------------------------------------------")
                cari_nm = True
                # back_read()
                print("\nKetik 1 untuk cari lagi\nKetik 0 untuk kembali ke menu")
                pilih = input("Silahkan pilih : ")
                if pilih == "1":
                    search_dokter()
                if pilih == "0":
                    main_menu_dokter()
        if cari_nm  == False:
            print(f"\nNama pasien {nm} tidak ditemukan !!!\nMungkin pasien sudah pulang atau coba lengkapi nama pasien yang dicari.")
            print("\nKetik 1 untuk cari lagi\nKetik 0 untuk kembali ke menu")
            pilih = input("Silahkan pilih : ")
            if pilih == "1":
                search_dokter()
            if pilih == "0":
                main_menu_dokter()

def search_pengunjung():
    global data_pasien
    while True:
        nm = input('Masukkan nama pasien: ').title()
        cari_nm = False
        for i in range(len(data_pasien)):
            if nm == data_pasien[i]['nama']:
                print("\n---------------------------------------------------------------")
                print("NAMA PASIEN\tJENIS KELAMIN\tUSIA\tALAMAT\t\tKAMAR")
                print("---------------------------------------------------------------")
                print(f"{data_pasien[i]['nama']}\t{data_pasien[i]['jenis_kelamin']}\t\t{data_pasien[i]['usia']}\t{data_pasien[i]['alamat']}\t{data_pasien[i]['ruang']}")
                print("---------------------------------------------------------------\n")
                cari_nm = True
                # back_read()
                print("Ketik 1 untuk cari lagi\nKetik 0 untuk kembali ke dasbor utama")
                pilih = input("Silahkan pilih : ")
                if pilih == "1":
                    search_dokter()
                if pilih == "0":
                    dasbor()
        if cari_nm  == False:
            print(f"Nama pasien {nm} tidak ditemukan.\nMungkin pasien sudah pulang atau coba lengkapi nama pasien yang dicari.")
            print("Ketik 1 untuk cari lagi\nKetik 0 untuk kembali ke dasbor utama")
            pilih = input("Silahkan pilih : ")
            if pilih == "1":
                search_dokter()
            if pilih == "0":
                dasbor()


## MAIN MENU
def main_menu_admin ():
# Menu utama untuk user admin
    global data_pasien
    print ('''\n=============================================================
SELAMAT DATANG ADMIN DI MENU UTAMA APLIKASI RS BAHAGIA SELALU
=============================================================''')
    print ("1. Melihat daftar pasien")
    print ("2. Pendaftaran pasien rawat inap")
    print ("3. Edit data pasien")
    print ("4. Hapus pasien rawat inap")
    print ("5. Cari nama pasien")
    print ("6. Keluar program")

    menu = input("\nMasukkan nomor yang ingin dijalankan : ")
    while True:
        if menu == "1":
            read_admin()
            # back_read()
        elif menu == "2":
            create()
            read_admin()
        elif menu == "3":
            update()
            read_admin()
        elif menu == "4":
            read1()
            i = int(input("Masukkan nomer pasien chekout : "))
            print(f"\nData pasien {data_pasien[i-1]['kode']} sudah dihapus dari daftar rawat inap !")
            delete(i)
            read_admin()
        elif menu == "5":
            search_admin()
            # back_read()
        elif menu == "6":
            print("\nTerima kasih, sampai jumpa kembali\n")
            bintang()
            dasbor()
        dasbor()

def main_menu_dokter ():
# Menu utama untuk user dokter
    global data_pasien
    print ('''\n==============================================================
SELAMAT DATANG DOKTER DI MENU UTAMA APLIKASI RS BAHAGIA SELALU
==============================================================''')
    print ("1. Melihat daftar pasien")
    print ("2. Cari nama pasien")
    print ("3. Keluar program")

    menu = input("\nMasukkan nomor yang ingin dijalankan : ")
    while True:
        if menu == "1":
            read_dokter()
            back_read_dokter()
        elif menu == "2":
            search_dokter()
        elif menu == "3":
            print("\nTerima kasih, sampai jumpa kembali\n")
            dasbor()
        # dasbor()


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
    3. Pengunjung''')
        usr = input("\nKetik angka sesuai user : ")
        if usr == "1":
            print('''\n===========================================
SELAMAT DATANG USER ADMIN RS BAHAGIA SELALU
===========================================''')
        # Login user admin
            while True :
                user = input("Masukkan username anda : ")
                pasw = input("Masukkan password anda : ")
                if user == "admin" and pasw == "12":
                    main_menu_admin()
                else :
                    print("\nUsername atau Password anda salah !!!")
                    pilih = input("Ketik 0 untuk kembali ke dasbor utama, ketik lainnya untuk login ulang : ")
                    if pilih == "0":
                        dasbor()
                    
        elif usr == "2":
            print('''\n============================================
SELAMAT DATANG USER DOKTER RS BAHAGIA SELALU
============================================''')
        # Login user dokter
            while True :
                user = input("Masukkan username anda : ")
                pasw = input("Masukkan password anda : ")
                if user == "dokter" and pasw == "12":
                    main_menu_dokter()
                else :
                    print("\nUsername atau Password anda salah !!!")
                    pilih = input("Ketik 0 untuk kembali ke dasbor utama, ketik lainnya untuk login ulang : ")
                    if pilih == "0":
                        dasbor()

        elif usr == "3":
            print('''===================================
SELAMAT DATANG DI RS BAHAGIA SELALU
===================================''')
            print("\nLaman ini untuk mencari nama pasien rawat inap RS Bahagia Selalu")
            search_pengunjung()
            # print("Mohon Maaf Aplikasi untuk user tersebut sedang dalam proses")
        else:
            print("\nSilahkan pilih user yang sudah ada")

bintang()
dasbor()
