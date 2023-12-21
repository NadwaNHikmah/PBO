class Celsius:
    def __init__(self, suhu):
        self.suhu = suhu
    
    def get_celsius(self):
        val = self.suhu
        return val
    
    def get_fahrenheit(self):
        val = (9/5 * self.suhu) + 32
        return val
    
    def get_reamur(self):
        val = (4/5 * self.suhu)
        return val

    def get_kelvin(self):
        val = self.suhu + 273.15
        return val

suhu_celsius = input("Masukkan suhu dalam Celsius: ")
C = Celsius(float(suhu_celsius))
val = C.get_celsius()

F = C.get_fahrenheit()
R = C.get_reamur()
K = C.get_kelvin()

print(str(val) + " Celsius sama dengan:")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")