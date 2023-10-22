# Minta input dari pengguna
panjang = float(input("Masukkan panjang balok (cm): "))
lebar = float(input("Masukkan lebar balok (cm): "))
tinggi = float(input("Masukkan tinggi balok (cm): "))

# Menghitung volume balok
volume = panjang * lebar * tinggi

# Menampilkan hasil
print(f"Volume balok adalah {volume} cm^3")
