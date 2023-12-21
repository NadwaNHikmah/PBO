print("Konversi Suhu Fahrenheit")

# Entry
suhu_fahrenheit = input("Masukan suhu dalam Fahrenheit: ")

# rumus
C = (float(suhu_fahrenheit) - 32) * 5/9
R = (float(suhu_fahrenheit) - 32) * 4/9
K = (float(suhu_fahrenheit) - 32) * 5/9 + 273.15

# output
print(suhu_fahrenheit + " Fahrenheit sama dengan: ")
print(str(C) + " Celsius")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")