# Capstone-1
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


# Read
def read() :
    print ('''===============================
DAFTAR PASIEN RS BAHAGIA SELALU
===============================''')
    print("NO\tNO PENDAFTARAN\tNAMA PASIEN\t\tJENIS KELAMIN\tUSIA\tALAMAT\t\tKAMAR")
    global data_pasien
    for i in range(len(data_pasien)) :
        print(f"{i+1}\t{data_pasien[i]['kode']}\t\t{data_pasien[i]['nama']}\t\t{data_pasien[i]['jenis_kelamin']}\t\t{data_pasien[i]['usia']}\t{data_pasien[i]['alamat']}\t{data_pasien[i]['ruang']}")

# Create
def create() :
    print ('''=========================================
PENDAFTARAN PASIEN BARU RS BAHAGIA SELALU
=========================================''')
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

# update
def update() :
    global data_pasien
    read()
    a = int(input("Pilih No pasiena yang akan di edit : "))
    counter = 0
    for i in data_pasien[a-1]:
        counter += 1
        print(f"{counter}. \t {i} : {data_pasien[a-1][i]}")
    b = int(input(" Nomor mana yang mau di edit: "))
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

# delete
def delete(i):
    global data_pasien
    del data_pasien[i]
    print(f"Data pasien {data_pasien[i-1]['kode']} sudah dihapus dari daftar rawat inap !")


# search
def search(kode_cari) :
    for i in range(len(data_pasien)):
        if data_pasien[i]['kode'] == kode_cari:
            return i
    return -1 

# Main Menu
def main_menu ():
    global data_pasien
    print ('''=========================================================
SELAMAT DATANG PADA MENU UTAMA APLIKASI RS BAHAGIA SELALU
=========================================================''')
    print ("1. Melihat daftar pasien")
    print ("2. Pendaftaran pasien baru")
    print ("3. Edit data pasien")
    print ("4. Hapus pasien rawat inap")
    print ("5. Exit program")

    menu = input("Masukkan nomor yang ingin dijalankan : ")

    if menu == "1":
        read()
    elif menu == "2":
        create()
        read()
    elif menu == "3":
        update()
    elif menu == "4":
        read()
        i = int(input("Masukkan nomer pasiesn yang sudah chekout : "))
        delete(i-1)
        read()
    elif menu == "5":
        return print("Terima kasih, sampai jumpa kembali")
    main_menu()

main_menu()
