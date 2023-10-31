# Minta input dari pengguna
panjang_sisi_alas = float(input("Masukkan panjang sisi alas segitiga (cm): "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga (cm): "))
tinggi_limas = float(input("Masukkan tinggi limas (cm): "))

# Menghitung luas alas segitiga
luas_alas = 0.5 * panjang_sisi_alas * tinggi_segitiga

# Menghitung volume limas segitiga
volume = (1/3) * luas_alas * tinggi_limas

# Menampilkan hasil
print(f"Volume limas segitiga adalah {volume} cm^3")
