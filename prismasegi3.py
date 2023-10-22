# Input tinggi, panjang sisi alas, dan tinggi segitiga
tinggi_prisma = float(input("Masukkan tinggi prisma: "))
panjang_alas = float(input("Masukkan panjang sisi alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))

# Menghitung luas permukaan prisma segitiga
luas_permukaan = (2 * panjang_alas) + (panjang_alas * tinggi_prisma) + (3 * panjang_alas * tinggi_segitiga)

# Menghitung volume prisma segitiga
volume = (1/2) * panjang_alas * tinggi_segitiga * tinggi_prisma

# Menampilkan hasil
print(f"Luas permukaan prisma segitiga adalah: {luas_permukaan}")
print(f"Volume prisma segitiga adalah: {volume}")