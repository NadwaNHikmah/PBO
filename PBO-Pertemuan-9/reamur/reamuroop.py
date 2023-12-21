class Reamur:
    def __init__(self, suhu):
        self.suhu = suhu
    
    def get_reamur(self):
        val = self.suhu
        return val
    
    def get_celsius(self):
        val = 5/4 * float(self.suhu)
        return val
    
    def get_fahrenheit(self):
        val = (9/4 * float(self.suhu)) + 32
        return val

    def get_kelvin(self):
        val = (5/4 * float(self.suhu)) + 273
        return val

suhu_reamur = input("Masukan suhu dalam Reamur: ")
R = Reamur(float(suhu_reamur))
val = R.get_reamur()

C = R.get_celsius()
F = R.get_fahrenheit()
K = R.get_kelvin()

print(str(val) + " Reamur sama dengan:")
print(str(C) + " Celsius")
print(str(F) + " Fahrenheit")
print(str(K) + " Kelvin")