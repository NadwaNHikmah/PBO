import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W
import math

def hitung_luas():
    tinggi  = float(txttinggi.get())
    jari_jari = float(txtjari_jari.get())

    L = math.pi * jari_jari * (jari_jari + math.sqrt(jari_jari * 2 + tinggi * 2))

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    tinggi = float(txttinggi.get())
    jari_jari = float(txtjari_jari.get())

    volume = (1/3) * math.pi * jari_jari * tinggi * 2

    txtvolume.delete(0,END)
    txtvolume.insert(END,volume)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Kerucut")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

# Label Tinggi
tinggi = Label(frame, text="Tinggi:") 
tinggi.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#Label jari2
jari_jari= Label(frame, text="jari_jari:")
jari_jari.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=0, column=1,sticky=W, padx=5, pady=5)

#text box jari-jari
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=1, column=1,sticky=W, padx=5, pady=5 )

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label (frame, text="Volume: ")
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtvolume = Entry (frame)
txtvolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

nama = Label(frame, text='Nadzwa Nurul Hikmah')
nama.grid(row=5, column=0, sticky=W, padx=5, pady=5)

nama = Label(frame, text='220511099')
nama.grid(row=6, column=0, sticky=W, padx=6, pady=6)

app.mainloop()