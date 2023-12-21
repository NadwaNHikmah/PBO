print("Konversi Suhu Kelvin")

def kelvin_to_celsius(suhu_kelvin):
    return float(suhu_kelvin) - 273

def kelvin_to_fahrenheit(suhu_kelvin):
    return (9/5 * (float(suhu_kelvin) - 273)) + 32

def kelvin_to_reamur(suhu_kelvin):
    return (4/5 * (float(suhu_kelvin) - 273))

# Entry
suhu_kelvin = input("Masukan suhu dalam Kelvin:")

# Rumus 
C = kelvin_to_celsius(suhu_kelvin)
F = kelvin_to_fahrenheit(suhu_kelvin)
R = kelvin_to_reamur(suhu_kelvin)

# Output
print(suhu_kelvin + " Kelvin sama dengan:")
print(str(C) + " Celsius")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")