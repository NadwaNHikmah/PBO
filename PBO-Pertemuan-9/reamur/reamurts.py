print("Konversi Suhu Reamur")

def reamur_to_celsius(reamur):
    celsius = 5/4 * float(reamur)
    return celsius

def reamur_to_fahrenheit(reamur):
    fahrenheit = (9/4 * float(reamur)) + 32
    return fahrenheit

def reamur_to_kelvin(reamur):
    kelvin = (5/4 * float(reamur)) + 273
    return kelvin

# Entry
suhu_reamur = input("Masukan suhu dalam Reamur: ")

# Rumus 
C = reamur_to_celsius(suhu_reamur)
F = reamur_to_fahrenheit(suhu_reamur)
K = reamur_to_kelvin(suhu_reamur)

# Output
print(suhu_reamur + " Reamur sama dengan:")
print(str(C) + " Celsius")
print(str(F) + " Fahrenheit")
print(str(K) + " Kelvin")