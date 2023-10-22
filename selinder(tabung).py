import math

# Menghitung volume tabung
def volume_tabung(jari_jari, tinggi):
    volume = math.pi * jari_jari**2 * tinggi
    return volume

# Menyediakan data dari soal
jari_jari_alas = 20 # cm
tinggi_tabung = 50 # cm

# Memanggil fungsi volume_tabung
hasil = volume_tabung(jari_jari_alas, tinggi_tabung)

# Menampilkan hasil
print(f"Volume tabung adalah {hasil} cm^3")
