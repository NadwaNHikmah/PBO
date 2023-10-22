# Menghitung volume limas segitiga
def volume_limas_segitiga(alas_segitiga, tinggi_segitiga, tinggi_limas):
    luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga
    volume = (1/3) * luas_segitiga * tinggi_limas
    return volume

# Mengambil input dari pengguna
alas_segitiga = float(input("Masukkan panjang alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
tinggi_limas = float(input("Masukkan tinggi limas: "))

# Memanggil fungsi volume_limas_segitiga
hasil = volume_limas_segitiga(alas_segitiga, tinggi_segitiga, tinggi_limas)

# Menampilkan hasil
print(f"Volume limas segitiga dengan alas {alas_segitiga}, tinggi segitiga {tinggi_segitiga}, dan tinggi limas {tinggi_limas} adalah {hasil}")
