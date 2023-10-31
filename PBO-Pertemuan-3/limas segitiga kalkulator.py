import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luaspermukaan():
    alassegitiga = float(txtalassegitiga.get())
    tinggilimas = float(txttinggilimas.get())
    tinggisegitiga = float(txttinggisegitiga.get())
    
    luas = 4*(1/2*alassegitiga*tinggisegitiga)*tinggilimas
    
    txtluaspermukaan.delete(0,END)
    txtluaspermukaan.insert(END,luas)
    
def hitung_volume():
    alassegitiga = float(txtalassegitiga.get())
    tinggilimas = float(txttinggilimas.get())
    tinggisegitiga = float(txttinggisegitiga.get())
    
    Volume =  1/3*(1/2*alassegitiga*tinggisegitiga)*tinggilimas
    
    txtvolume.delete(0, END)
    txtvolume.insert(END, Volume)
    
def hitung():
    hitung_luaspermukaan()
    hitung_volume()
    
# Create tkinter object
app = tk.Tk()

#Tambahkan judul
app.title("Kalkulator Luas Permukaan dan Volume Limas Segitiga")

#Windows
frame = Frame(app)
frame.pack(padx= 20, pady=20)

#Label Alas Segitiga
alassegitiga = Label(frame, text="Alas Segitiga:")
alassegitiga.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#Label Tinggi Limas
tinggilimas = Label(frame, text="Tinggi Limas:")
tinggilimas.grid(row=1, column=0, sticky=W, padx=5, pady=5)

#Label Tinggi Segitiga
tinggisegitiga = Label(frame, text="Tinggi Segitiga:")
tinggisegitiga.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#Textbox Alas Segitiga
txtalassegitiga =Entry (frame)
txtalassegitiga.grid(row=0, column=1)

#Textbox Tinggi Limas
txttinggilimas = Entry (frame)
txttinggilimas.grid(row=1, column=1)

#Textbox Tinggi Segitiga
txttinggisegitiga = Entry (frame)
txttinggisegitiga.grid(row=2, column=1)

#Button 
hitung_button = Button (frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

#Output Label Luas Permukaan
luaspermukaan = Label(frame, text="Luas Permukaan:")
luaspermukaan.grid(row=4, column=0, sticky=W, padx=5, pady=5)

#Output Label Volume
volume = Label(frame, text="Volume:")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

#Output Textbox Luas Permukaan
txtluaspermukaan = Entry (frame)
txtluaspermukaan.grid(row=4, column=1, sticky=W, padx=5, pady=5)

#Output Textbox Volume
txtvolume = Entry (frame)
txtvolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

nama = Label(frame, text='Nadzwa Nurul Hikmah')
nama.grid(row=6, column=0, sticky=W, padx=6, pady=6)

nama = Label(frame, text='220511099')
nama.grid(row=7, column=0, sticky=W, padx=7, pady=7)

app.mainloop()