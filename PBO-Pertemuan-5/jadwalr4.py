# Program untuk membuat dan membaca file jadwal kuliah R4/D

def tambah_jadwal():
    # Menerima input jadwal baru
    hari = input("Masukkan hari: ")
    jam = input("Masukkan jam: ")
    mata_kuliah = input("Masukkan mata kuliah: ")

    # Menyimpan jadwal ke dalam file
    with open("jadwal_kuliah.txt", "a") as file:
        file.write(f"{hari}, {jam}, {mata_kuliah}\n")

    print("Jadwal berhasil ditambahkan.")

def lihat_jadwal():
    # Membaca dan menampilkan jadwal dari file
    try:
        with open("jadwal_kuliah.txt", "r") as file:
            jadwal = file.readlines()

        if not jadwal:
            print("Jadwal kosong.")
        else:
            print("Jadwal Kuliah:")
            for jadwal_item in jadwal:
                print(jadwal_item.strip())

    except FileNotFoundError:
        print("File jadwal_kuliah.txt tidak ditemukan. Jadwal kosong.")

# Menu utama
while True:
    print("\nMenu:")
    print("1. Tambah Jadwal")
    print("2. Lihat Jadwal")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        tambah_jadwal()
    elif pilihan == "2":
        lihat_jadwal()
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
