 # set nilai panjang dan lebar 
panjang = 25
lebar = 4

def HitungLuas(pj, lb):
    # rumus
    L = pj * lb

    # tampilkan hasilnya
    print("Luas :",L)

def HitungKeliling(pj, lb):
   # rumus
   K = (2 * pj)+(2 * lb)

   # tampilkan hasilnya
   print("Keliling :",K)

# Gunakan fungsi untuk menghitung
print("Panjang:", panjang)
print("Lebar:", lebar)
HitungLuas(panjang, lebar)
HitungKeliling(panjang, lebar)