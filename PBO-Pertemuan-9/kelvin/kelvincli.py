print("Konversi Suhu Kelvin")

# Entry
suhu_kelvin = input("Masukan suhu dalam Kelvin: ")

# Rumus
C = float(suhu_kelvin) - 273
F = (9/5 * (float(suhu_kelvin) - 273)) + 32
R = (4/5 * (float(suhu_kelvin) - 273))

# Output
print(suhu_kelvin + " Kelvin sama dengan:")
print(str(C) + " Celsius")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")