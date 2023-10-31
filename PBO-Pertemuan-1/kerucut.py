import math

# Minta input dari pengguna
jari_jari_alas = float(input("Masukkan jari-jari alas kerucut (cm): "))
tinggi_kerucut = float(input("Masukkan tinggi kerucut (cm): "))

# Menghitung volume kerucut
volume = (1/3) * math.pi * jari_jari_alas**2 * tinggi_kerucut

# Menampilkan hasil
print(f"Volume kerucut adalah {volume} cm^3")
