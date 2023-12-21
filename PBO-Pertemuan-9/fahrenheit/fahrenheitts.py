print("Konversi Suhu Fahrenheit")

def get_celsius(suhu_fahrenheit):
    return (float(suhu_fahrenheit) - 32) * 5/9

def get_reamur(suhu_fahrenheit):
    return (float(suhu_fahrenheit) - 32) * 4/9

def get_kelvin(suhu_fahrenheit):
    return (float(suhu_fahrenheit) - 32) * 5/9 + 273.15

# Entry
suhu_fahrenheit = input("Masukan suhu dalam Fahrenheit: ")

# rumus 
C = get_celsius(suhu_fahrenheit)
R = get_reamur(suhu_fahrenheit)
K = get_kelvin(suhu_fahrenheit)

# output
print(suhu_fahrenheit + " Fahrenheit sama dengan:")
print(str(C) + " Celsius")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")