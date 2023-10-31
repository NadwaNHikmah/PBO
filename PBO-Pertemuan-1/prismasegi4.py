# Menghitung volume prisma segitiga
def volume_prisma_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma):
    luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga
    volume = luas_segitiga * tinggi_prisma
    return volume

# Mengambil input dari pengguna
alas_segitiga = float(input("Masukkan panjang alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
tinggi_prisma = float(input("Masukkan tinggi prisma: "))

# Memanggil fungsi volume_prisma_segitiga
hasil = volume_prisma_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma)

# Menampilkan hasil
print(f"Volume prisma segitiga dengan alas {alas_segitiga}, tinggi segitiga {tinggi_segitiga}, dan tinggi prisma {tinggi_prisma} adalah {hasil}")
