import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luasalas():
    alas = float(txtalas.get())
    tinggi = float(txttinggi.get())
    luas = float(txtluas.get())
    tinggiprisma = float(txttinggiprisma.get())
    sisi1 = float(txtsisi1.get())
    sisi2 = float(txtsisi2.get())
    sisi3 = float(txtsisi3.get())
    
    luasalas = ( sisi1 + sisi2 + sisi3 ) * tinggiprisma
    
    txtluasalas.delete(0,END)
    txtluasalas.insert(END,luasalas)

def hitung_luassisi():
    alas = float(txtalas.get())
    tinggi = float(txttinggi.get())
    luas = float(txtluas.get())
    tinggiprisma = float(txttinggiprisma.get())
    sisi1 = float(txtsisi1.get())
    sisi2 = float(txtsisi2.get())
    sisi3 = float(txtsisi3.get())
    
    luassisi = ( sisi1 + sisi2 + sisi3 ) * tinggiprisma + alas * tinggi
    
    txtluassisi.delete(0,END)
    txtluassisi.insert(END,luassisi)
    
def hitung_volume():
    alas = float(txtalas.get())
    tinggi = float(txttinggi.get())
    luas = float(txtluas.get())
    tinggiprisma = float(txttinggiprisma.get())
    sisi1 = float(txtsisi1.get())
    sisi2 = float(txtsisi2.get())
    sisi3 = float(txtsisi3.get())
    
    volume = ( alas * tinggi ) / 2 * tinggiprisma
    
    txtvolume.delete(0, END)
    txtvolume.insert(END, volume)
    
def hitung():
    hitung_luasalas()
    hitung_luassisi()
    hitung_volume()
    
# Create tkinter object
app = tk.Tk()

#Tambahkan judul
app.title("Kalkulator Luas Alas, Luas Sisi dan Volume Prisma Segitiga")

#Windows
frame = Frame(app)
frame.pack(padx= 20, pady=20)

#Label Alas
alas = Label(frame, text="Alas:")
alas.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=1, column=0, sticky=W, padx=5, pady=5)

#Label Luas
luas = Label(frame, text="Luas:")
luas.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#Label Tinggi Prisma
tinggiprisma = Label(frame, text="Tinggi Prisma:")
tinggiprisma.grid(row=3, column=0, sticky=W, padx=5, pady=5)

#Label Sisi1
sisi1 = Label(frame, text="Sisi1:")
sisi1.grid(row=4, column=0, sticky=W, padx=5, pady=5)

#Label Sisi2
sisi2 = Label(frame, text="Sisi2:")
sisi2.grid(row=5, column=0, sticky=W, padx=5, pady=5)

#Label Sisi3
sisi3 = Label(frame, text="Sisi3:")
sisi3.grid(row=6, column=0, sticky=W, padx=5, pady=5)

#Textbox Alas
txtalas =Entry (frame)
txtalas.grid(row=0, column=1)

#Textbox Tinggi
txttinggi = Entry (frame)
txttinggi.grid(row=1, column=1)

#Textbox Luas
txtluas = Entry (frame)
txtluas.grid(row=2, column=1)

#Textbox Tinggi Prisma
txttinggiprisma = Entry (frame)
txttinggiprisma.grid(row=3, column=1)

#Textbox Sisi1
txtsisi1 = Entry (frame)
txtsisi1.grid(row=4, column=1)

#Textbox Sisi2
txtsisi2 = Entry (frame)
txtsisi2.grid(row=5, column=1)

#Textbox Sisi3
txtsisi3 = Entry (frame)
txtsisi3.grid(row=6, column=1)

#Button 
hitung_button = Button (frame, text="Hitung", command=hitung)
hitung_button.grid(row=7, column=1, sticky=W, padx=5, pady=5)

#Output Label Luas Alas
luasalas = Label(frame, text="Luas Alas:")
luasalas.grid(row=8, column=0, sticky=W, padx=5, pady=5)

#Output Label Luas Sisi
luassisi = Label(frame, text="Luas Sisi:")
luassisi.grid(row=9, column=0, sticky=W, padx=5, pady=5)

#Output Label Volume
volume = Label(frame, text="Volume:")
volume.grid(row=10, column=0, sticky=W, padx=5, pady=5)

#Output Textbox Luas Alas
txtluasalas = Entry (frame)
txtluasalas.grid(row=8, column=1, sticky=W, padx=5, pady=5)

#Output Textbox Luas Sisi
txtluassisi = Entry (frame)
txtluassisi.grid(row=9, column=1, sticky=W, padx=5, pady=5)

#Output Textbox Volume
txtvolume = Entry (frame)
txtvolume.grid(row=10, column=1, sticky=W, padx=5, pady=5)

nama = Label(frame, text='Nadzwa Nurul Hikmah')
nama.grid(row=11, column=0, sticky=W, padx=5, pady=5)

nama = Label(frame, text='220511099')
nama.grid(row=12, column=0, sticky=W, padx=6, pady=6)

app.mainloop()