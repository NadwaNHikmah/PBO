class Kelvin:
    def __init__(self, suhu):
        self.suhu = suhu
    
    def get_kelvin(self):
        val = self.suhu
        return val
    
    def get_celsius(self):
        val = float(self.suhu) - 273
        return val
    
    def get_fahrenheit(self):
        val = (9/5 * (float(self.suhu) - 273)) + 32
        return val
    
    def get_reamur(self):
        val = (4/5 * (float(self.suhu) - 273))
        return val

# Entry
suhu_kelvin = input("Masukan suhu dalam Kelvin: ")
K = Kelvin(float(suhu_kelvin))
val = K.get_kelvin()

C = K.get_celsius()
F = K.get_fahrenheit()
R = K.get_reamur()

# Output
print(suhu_kelvin + " Kelvin sama dengan:")
print(str(C) + " Celsius")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")