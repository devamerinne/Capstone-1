from time import sleep

data_pasien = [
    {'kode' : 'P001',
     'nama' : 'Andi Jaya Malarang',
     'no_ktp' : "105024170890001",
     'jenis_kelamin' : 'P',
     'usia' : 30,
     'alamat' : 'Jl. Jeruk',
     'ruang' : 'Mawar',
     'penyakit' : 'Jantung'},

     {'kode' : 'P002',
     'nama' : 'Bili Wongka',
     'no_ktp' : "332616060807019",
     'jenis_kelamin' : 'P',
     'usia' : 45,
     'alamat' : 'Jl. Semangka',
     'ruang' : 'Mawar',
     'penyakit' : 'Demam Berdarah'},

     {'kode' : 'P003',
     'nama' : 'Caca Maria',
     'no_ktp' : "357629990976540",
     'jenis_kelamin' : 'W',
     'usia' : 10,
     'alamat' : 'Jl. Apel',
     'ruang' : 'Melati',
     'penyakit' : 'Diabetes'}]



# HIASAN
def bintang():
    string = ""

    x = 3
    bar = x
    while bar >= 0:
        kol = bar
        while kol > 0:
            string = string + "   "
            kol = kol - 1	
        kiri = 1
        while kiri < (x - (bar-1)):
            string = string + " * "
            kiri = kiri + 1		
        kanan = 1
        while kanan < kiri -1:
            string = string + " * "
            kanan = kanan + 1	

        string = string + "\n"
        bar = bar - 1

    bar = 1	
    while bar <= x:
        kol = bar+1
        while kol > 1:
            string = string + "   "
            kol = kol - 1
        kiri = 0
        while kiri < (x - bar):
            string = string + " * "
            kiri = kiri + 1	
        kanan = kiri	
        while kanan > 1:
            string = string + " * "
            kanan = kanan - 1

        string = string + "\n"
        bar = bar + 1
    print (string)

# READ
def read_lengkap_admin ():
    a = input("\nPilih No pasien untuk melihat data lengkap : ")
    a = cek_program(a)
    print(f"\n-----Data Pasian kode {data_pasien[a-1]['kode']}-----\n")
    counter = 0
    for i in data_pasien[a-1]:
        counter += 1
        print(f"{counter}. {i.capitalize()} \t: {data_pasien[a-1][i]}")
    back_read_admin1()

def back_read_admin():
## Pernyataan untuk kembali ke menu utama laman admin
    utm = input("\nKetik 0 untuk kembali ke menu utama : ")
    while True:
        if utm == "0":
            main_menu_admin()
        else:
            read_admin()
            
def back_read_admin1():
    print('''\nKetik 1 untuk melihat rincian data pasien
Ketik 2 untuk melihat semua daftar pasien rawat inap
Ketik 0 untuk kembali ke menu utama''')
    bc = input ("\nPilih Program : ")
    while True:
        if bc == "1":
            read_lengkap_admin()
        elif bc == "2":
            read_admin()
        elif bc == "0":
            back_read_admin()
        else:
            print("\n\tYang anda ketik salah!")
            sleep(1)
            print("\tSilahkan pilih ulang")
            sleep(1)
            back_read_admin1()

def read_admin() :
## Mencetak semua data dengan pilihan kembali ke menu utama
    print ('''\n==========================================
DAFTAR PASIEN RAWAT INAP RS BAHAGIA SELALU
==========================================\n''')
    print("------------------------------------------------------------------------------------------------------------------")
    print("NO\tNO PENDAFTARAN\tNAMA PASIEN\tNO KTP\t\tJENIS KELAMIN\tUSIA\tALAMAT\t\tKAMAR\tPENYAKIT")
    print("------------------------------------------------------------------------------------------------------------------")
    global data_pasien
    for i in range(len(data_pasien)) :
        if len(data_pasien[i]['nama']) > 10:
            data_nama = data_pasien[i]['nama'][:10] + "..."
        else:
            data_nama = data_pasien[i]['nama']
        if len(data_pasien[i]['alamat']) > 10:
            data_alamat = data_pasien[i]['alamat'][:10]+"..."
        else:
            data_alamat = data_pasien[i]['alamat']
        data_ktp = data_pasien[i]['no_ktp'][:7]+"..."

        print(f"{i+1}\t{data_pasien[i]['kode']}\t\t{data_nama}\t{data_ktp}\t{data_pasien[i]['jenis_kelamin']}\t\t{data_pasien[i]['usia']}\t{data_alamat}\t{data_pasien[i]['ruang']}\t{data_pasien[i]['penyakit']}")
        print("------------------------------------------------------------------------------------------------------------------")
    back_read_admin1()

def read_lengkap_dokter():
    a = int(input("\nPilih No pasien untuk melihat data lengkap : "))
    print(f"\n-----Data Pasian kode {data_pasien[a-1]['kode']}-----\n")
    counter = 0
    for i in data_pasien[a-1]:
        counter += 1
        print(f"{counter}. {i.capitalize()} \t: {data_pasien[a-1][i]}")
    back_read_dokter1()

def back_read_dokter():
## Pernyataan untuk kembali ke menu utama laman dokter
    utm = int(input("\nKetik 0 untuk kembali ke menu utama : "))
    while True:
        if utm == 0:
            main_menu_dokter()
        else:
            read_dokter()
        break

def back_read_dokter1():
    print('''\nKetik 1 untuk melihat rincian data pasien
Ketik 2 untuk melihat semua daftar pasien rawat inap
Ketik 0 untuk kembali ke menu utama''')
    bc = input ("\nPilih Program : ")
    while True:
        if bc == "1":
            read_lengkap_dokter()
        elif bc == "2":
            read_dokter()
        elif bc == "0":
            back_read_dokter()
        else:
            print("\n\tYang anda ketik salah!")
            sleep(1)
            print("\tSilahkan pilih ulang")
            sleep(1)
            back_read_dokter1()

def read_dokter() :
## Mencetak semua data dengan pilihan kembali ke menu utama
    print ('''\n==========================================
DAFTAR PASIEN RAWAT INAP RS BAHAGIA SELALU
==========================================\n''')
    print("------------------------------------------------------------------------------------------------------------------")
    print("NO\tNO PENDAFTARAN\tNAMA PASIEN\tNO KTP\t\tJENIS KELAMIN\tUSIA\tALAMAT\t\tKAMAR\tPENYAKIT")
    print("------------------------------------------------------------------------------------------------------------------")
    global data_pasien
    for i in range(len(data_pasien)) :
        if len(data_pasien[i]['nama']) > 10:
            data_nama = data_pasien[i]['nama'][:10] + "..."
        else:
            data_nama = data_pasien[i]['nama']
        if len(data_pasien[i]['alamat']) > 10:
            data_alamat = data_pasien[i]['alamat'][:10]+"..."
        else:
            data_alamat = data_pasien[i]['alamat']
        data_ktp = data_pasien[i]['no_ktp'][:7]+"..."

        print(f"{i+1}\t{data_pasien[i]['kode']}\t\t{data_nama}\t{data_ktp}\t{data_pasien[i]['jenis_kelamin']}\t\t{data_pasien[i]['usia']}\t{data_alamat}\t{data_pasien[i]['ruang']}\t{data_pasien[i]['penyakit']}")
        print("------------------------------------------------------------------------------------------------------------------")
    back_read_dokter1()

def read1() :
## Mencetak semua data saja
    print ('''\n==========================================
DAFTAR PASIEN RAWAT INAP RS BAHAGIA SELALU
==========================================\n''')
    print("------------------------------------------------------------------------------------------------------------------")
    print("NO\tNO PENDAFTARAN\tNAMA PASIEN\tNO KTP\t\tJENIS KELAMIN\tUSIA\tALAMAT\t\tKAMAR\tPENYAKIT")
    print("------------------------------------------------------------------------------------------------------------------")
    global data_pasien
    for i in range(len(data_pasien)) :
        if len(data_pasien[i]['nama']) > 10:
            data_nama = data_pasien[i]['nama'][:10] + "..."
        else:
            data_nama = data_pasien[i]['nama']
        if len(data_pasien[i]['alamat']) > 10:
            data_alamat = data_pasien[i]['alamat'][:10]+"..."
        else:
            data_alamat = data_pasien[i]['alamat']
        data_ktp = data_pasien[i]['no_ktp'][:7]+"..."

        print(f"{i+1}\t{data_pasien[i]['kode']}\t\t{data_nama}\t{data_ktp}\t{data_pasien[i]['jenis_kelamin']}\t\t{data_pasien[i]['usia']}\t{data_alamat}\t{data_pasien[i]['ruang']}\t{data_pasien[i]['penyakit']}")
        print("------------------------------------------------------------------------------------------------------------------")

# CREATE
## Membuat daftar data pasien baru
def create() :
    print ('''\n====================================================
PENDAFTARAN PASIEN RAWAT INAP BARU RS BAHAGIA SELALU
====================================================''')
    print(f"Kode Pasien terakhir adalah {data_pasien[-1]['kode']}")
    print("Masukkan data pasien\n")
    
    cek_kode = True
    while cek_kode:
        add_no = (input("Kode \t: ")).capitalize()
        kode_list = []
        for i in data_pasien:
            kode_list.append(i['kode'])
        if add_no in kode_list:
            print("---Kode sudah ada---")
        else:
            break

    add_nama= (input("\nNama Pasien : ")).title()

    konfirm_jk = True
    while konfirm_jk:
        print("\nJenis Kelamin ketik 'P' untuk Pria, dan 'W' untuk Wanita")
        add_jk = (input("Jenis kelamin : "))
        if add_jk.capitalize() == 'P' or add_jk.upper() == 'W':
            konfirm_jk = False
        else :
            print("Jenis Kelamin tidak sesuai, HARAP ISI DENGAN")

    add_ktp = (input("\nNo KTP \t: "))
    add_usia = (input("\nUsia \t: "))
    add_alamat = (input("\nAlamat \t: ")).title()
    add_ruang = (input("\nRuang \t: ")).capitalize()
    add_penyakit = (input("\nPenyakit \t: ")).title()
    tabel_data = {'kode' : add_no,
                'nama' : add_nama,
                'no_ktp' : add_ktp,
                'jenis_kelamin' : add_jk,
                'usia' : add_usia,
                'alamat' : add_alamat,
                'ruang' : add_ruang,
                'penyakit' : add_penyakit}
    
    # print tabel data
    print("\nData Pasien adalah :" )
    counter = 0
    for i in tabel_data:
        counter += 1
        print(f"{counter}. {i.capitalize()} \t: {tabel_data[i]}")
            
    print("\n---Apakah anda yakin untuk menambahkan pasien?---")
    putusan1 = input("\nKetik [Y] untuk menambah data, ketik [N] untuk membatlkan : ").capitalize()
    if putusan1 == "Y":
        data_pasien.append(tabel_data)
        print("\n\tSELAMAT DATA ANDA BERHASIL DIPERBARUI ^_^ ")
        # read_admin()
    elif putusan1 == "N":
        print("\nData tidak jadi di edit !")
    else:
        notif()

# Notif data salah
def notif():
    print("\n\tYang anda ketik bukan 'Y' atau 'N' . . .")
    sleep(1)
    print("\tData anda belum tersimpan . . .")
    sleep(1)
    print("\tSilahkan ulangi di menu utama !\n")
    sleep(1)


# UPDATE
## Mengedit daftar pasien yang sudah ada
def update() :
    global data_pasien
    read1()
    a = input("\nPilih No pasien yang akan di edit : ")
    a = cek_program(a)
    counter = 0
    for i in data_pasien[a-1]:
        counter += 1
        print(f"{counter}. {i.capitalize()} \t: {data_pasien[a-1][i]}")
    b = int(input("\nNomor mana yang mau di edit: "))
    if b == 1:
        kode1 = input("\nSilahkan isi dengan kode pasien yang benar : ").upper()

        print("\nCoba cek kembali, apakah data sudah benar?")

        counter = 0
        for i in data_pasien[a-1]:
            counter += 1
            if i == 'kode':
                print(f"{counter}. {i.capitalize()} \t: {kode1}")
            else :
                print(f"{counter}. {i.capitalize()} \t: {data_pasien[a-1][i]}")
            
        print(f"\nApakah anda yankin mau mengedit {data_pasien[a-1]['kode']} menjadi {kode1}?")
        putusan = input("\nKetik [Y] untuk merubah data, ketik [N] untuk membatlkan : ").capitalize()
        if putusan == "Y":
            print("\n\tSELAMAT DATA ANDA BERHASIL DIPERBARUI ^_^ ")
            data_pasien[a-1]['kode'] = kode1
        elif putusan == "N":
            print("\nData tidak jadi di edit !")
        else:
            notif()

    if b == 2:
        nama1 = input("\nSilahkan isi dengan data nama pasien yang benar : ").title()

        print("\nCoba cek kembali, apakah data sudah benar?")
        
        counter = 0
        for i in data_pasien[a-1]:
            counter += 1
            if i == 'nama':
                print(f"{counter}. {i.capitalize()} \t: {nama1}")
            else :
                print(f"{counter}. {i.capitalize()} \t: {data_pasien[a-1][i]}")
            

        print(f"\nApakah anda yankin mau mengedit {data_pasien[a-1]['nama']} menjadi {nama1}?")
        putusan = input("\nKetik [Y] untuk merubah data, ketik [N] untuk membatlkan : ").capitalize()
        if putusan == "Y":
            print("\n\tSELAMAT DATA ANDA BERHASIL DIPERBARUI ^_^ ")
            data_pasien[a-1]['nama'] = nama1
        elif putusan == "N":
            print("\nData tidak jadi di edit !")
        else:
            notif()

    if b == 3:
        jenis_kelamin1 = input("\nSilahkan isi dengan data jenis kelamin pasien yang benar : ").capitalize()
        print("\nCoba cek kembali, apakah data sudah benar?")
        
        counter = 0
        for i in data_pasien[a-1]:
            counter += 1
            if i == 'jenis_kelamin':
                print(f"{counter}. {i.capitalize()} \t: {jenis_kelamin1}")
            else :
                print(f"{counter}. {i.capitalize()} \t: {data_pasien[a-1][i]}")
            

        print(f"\nApakah anda yankin mau mengedit {data_pasien[a-1]['jenis_kelamin']} menjadi {jenis_kelamin1}?")
        putusan = input("\nKetik [Y] untuk merubah data, ketik [N] untuk membatlkan : ").capitalize()
        if putusan == "Y":
            print("\n\tSELAMAT DATA ANDA BERHASIL DIPERBARUI ^_^ ")
            data_pasien[a-1]['jenis_kelamin'] = jenis_kelamin1
        elif putusan == "N":
            print("\nData tidak jadi di edit !")
        else:
            notif()

    if b == 4:
        usia1 = input("\nSilahkan isi dengan data usia pasien yang benar : ")
        print("\nCoba cek kembali, apakah data sudah benar?")
        
        counter = 0
        for i in data_pasien[a-1]:
            counter += 1
            if i == 'usia':
                print(f"{counter}. {i.capitalize()} \t: {usia1}")
            else :
                print(f"{counter}. {i.capitalize()} \t: {data_pasien[a-1][i]}")
            
        print(f"\nApakah anda yankin mau mengedit {data_pasien[a-1]['usia']} menjadi {usia1}?")
        putusan = input("\nKetik [Y] untuk merubah data, ketik [N] untuk membatlkan : ").capitalize()
        if putusan == "Y":
            print("\n\tSELAMAT DATA ANDA BERHASIL DIPERBARUI ^_^ ")
            data_pasien[a-1]['usia'] = usia1
        elif putusan == "N":
            print("\nData tidak jadi di edit !")


    if b == 5:
        alamat1 = input("\nSilahkan isi dengan data alamat pasien yang benar : ").title()

        print("\nCoba cek kembali, apakah data sudah benar?")
        
        counter = 0
        for i in data_pasien[a-1]:
            counter += 1
            if i == 'alamat':
                print(f"{counter}. {i.capitalize()} \t: {alamat1}")
            else :
                print(f"{counter}. {i.capitalize()} \t: {data_pasien[a-1][i]}")
            

        print(f"\nApakah anda yankin mau mengedit {data_pasien[a-1]['alamat']} menjadi {alamat1}?")
        putusan = input("\nKetik [Y] untuk merubah data, ketik [N] untuk membatlkan : ").capitalize()
        if putusan == "Y":
            print("\n\tSELAMAT DATA ANDA BERHASIL DIPERBARUI ^_^ ")
            data_pasien[a-1]['alamat'] = alamat1
        elif putusan == "N":
            print("\nData tidak jadi di edit !")
        else:
            notif()


    if b == 6:
        ruang1 = input("\nSilahkan isi dengan data ruang yang benar : ").title()
        print("\nCoba cek kembali, apakah data sudah benar?")
        
        counter = 0
        for i in data_pasien[a-1]:
            counter += 1
            if i == 'ruang':
                print(f"{counter}. {i.capitalize()} \t: {ruang1}")
            else :
                print(f"{counter}. {i.capitalize()} \t: {data_pasien[a-1][i]}")
            

        print(f"\nApakah anda yankin mau mengedit {data_pasien[a-1]['ruang']} menjadi {ruang1}?")
        putusan = input("\nKetik [Y] untuk merubah data, ketik [N] untuk membatlkan : ").capitalize()
        if putusan == "Y":
            print("\n\tSELAMAT DATA ANDA BERHASIL DIPERBARUI ^_^ ")
            data_pasien[a-1]['ruang'] = ruang1
        elif putusan == "N":
            print("\nData tidak jadi di edit !")
        else:
            notif()

# DELETE
## Menghapus data pasien
def delete():
    i = input("Masukkan nomer pasien chekout : ")
    i = cek_program(i)
    global data_pasien
    print("Apakah anda yakin mau menhghapus?")
    hps = input("Ketik [Y] untuk melanjutkan program, ketik [N] untuk membatalkan :").upper()
    if hps == "Y":
        print(f"\nData pasien {data_pasien[i-1]['kode']} sudah dihapus dari daftar rawat inap !")
        del data_pasien[i-1]
        read_admin()
    if hps == "N":
        read_admin()
    else:
        notif()
        main_menu_admin()

# SEARCH
## Mencari data pasien di akun admin
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

## Mencari data pasien di akun dokter
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

## Mencari data pasien untuk pengunjung rumah sakit
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
                print("Ketik 1 untuk cari lagi\nKetik 0 untuk kembali ke dasbor utama")
                pilih = input("Silahkan pilih : ")
                if pilih == "1":
                    search_dokter()
                if pilih == "0":
                    bintang()
                    dasbor()
        if cari_nm  == False:
            print(f"\nNama pasien {nm} tidak ditemukan.\nMungkin pasien sudah pulang atau coba lengkapi nama pasien yang dicari.")
            print("\nKetik 1 untuk cari lagi\nKetik 0 untuk kembali ke dasbor utama")
            pilih = input("Silahkan pilih : ")
            if pilih == "1":
                search_dokter()
            if pilih == "0":
                bintang()
                dasbor()

# MAIN MENU
def main_menu_admin ():
## Menu utama untuk user admin
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
        elif menu == "2":
            create()
            read_admin()
        elif menu == "3":
            update()
            read_admin()
        elif menu == "4":
            read1()
            delete()
        elif menu == "5":
            search_admin()
        elif menu == "6":
            print("\nTerima kasih, sampai jumpa kembali\n")
            bintang()
            dasbor()
        dasbor()

def main_menu_dokter ():
## Menu utama untuk user dokter
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
            bintang()
            dasbor()

# DASHBOARD
## Tampilan pertama kali buka aplikasi
def dasbor():
    print('''============================================
SELAMAT DATANG DI APLIKASI RS BAHAGIA SELALU
============================================''')
    while True:
        print('''Silahkan Pilih User
    1. Admin
    2. Dokter
    3. Pengunjung
    0. Exit Program''')
        usr = input("\nKetik angka sesuai user : ")
        if usr == "1":
            print('''\n===========================================
SELAMAT DATANG USER ADMIN RS BAHAGIA SELALU
===========================================''')
        # Login user admin
            while True :
                user = input("Masukkan username anda : ")
                pasw = input("Masukkan password anda : ")
                if user == "admin" and pasw == "1":
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
                if user == "dokter" and pasw == "2":
                    main_menu_dokter()
                else :
                    print("\nUsername atau Password anda salah !!!")
                    pilih = input("Ketik 0 untuk kembali ke dasbor utama, ketik lainnya untuk login ulang : ")
                    if pilih == "0":
                        dasbor()
        # Login untuk pengunjung
        elif usr == "3":
            print('''===================================
SELAMAT DATANG DI RS BAHAGIA SELALU
===================================''')
            print("\nLaman ini untuk mencari nama pasien rawat inap RS Bahagia Selalu")
            search_pengunjung()
        elif usr == "0":
            print("\nApakah yakin anda mau keluar dari program ini?")
            putusan = input("\nKetik [Y] untuk melanjutkan program, [N] untuk tetap di laman ini : ").capitalize()
            if putusan == "Y":
                exit()
            elif putusan == "N":
                dasbor()
            else:
                print("\nyang anda input salah, ketik ulang 0 untuk tetap keluar !!!")
                dasbor()
        else:
            print("\nSilahkan pilih user yang sudah ada")

def cek_program(program):
    while program.isnumeric() == False:
        print("\t-----Pilih sesuai opsi-----")
        program = input("Pilih sesuai opsi : ")
    program = int(program)
    while program > len(data_pasien):
        print (f"Masukkan input dari nomer 1 sampai {len(data_pasien)} saja")
        program = input("Pilih sesuai opsi : ")
        program = cek_program(program)
    return program

bintang()
dasbor()

