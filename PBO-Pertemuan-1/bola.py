import math 

# Input jari-jari bola
jari_jari = float(input("Masukkan jari-jari bola: "))

# Menghitung luas permukaan bola
luas_permukaan = 4 * math.pi * jari_jari ** 2

# Menghitung volume bola
volume = (4/3) * math.pi * jari_jari ** 3

# Menampilkan hasil
print(f"Luas permukaan bola adalah: {luas_permukaan}")
print(f"Volume bola adalah:{volume}")