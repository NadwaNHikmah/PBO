import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W
import math


def hitung_luas():
    jari_jari = float(txtjari_jari.get())
    Tinggi = float(txtTinggi.get())

    luas = (2 * math.pi * jari_jari) * jari_jari + Tinggi

    txtLuas.delete(0, END)
    txtLuas.insert(END,luas)

def hitung_volume():
    jari_jari = float(txtjari_jari.get())
    Tinggi = float(txtTinggi.get())

    Volume = math.pi * jari_jari * 2 * Tinggi

    txtVolume.delete(0,END)
    txtVolume.insert(END, Volume)

def hitung():
    hitung_luas()
    hitung_volume()

app = tk.Tk()

app.title ("Kalkulator Mencari Luas dan Volume Tabung")

frame = Frame (app)
frame.pack(padx=20, pady=20)

#panjang
jari_jari = Label (frame, text="Jari-jari:")
jari_jari.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#tinggi
Tinggi = Label (frame, text="Tinggi:")
Tinggi.grid(row=1, column=0, sticky=W, padx=5, pady=5)

#textbox panjang
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=0, column=1)

#textbox tinggi
txtTinggi = Entry(frame)
txtTinggi.grid(row=1,column=1 )
# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)


volume = Label (frame, text="Volume: ")
volume.grid(row=4, column=0, stick=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtVolume = Entry (frame)
txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

nama = Label(frame, text='Nadzwa Nurul Hikmah')
nama.grid(row=5, column=0, sticky=W, padx=5, pady=5)

nama = Label(frame, text='220511099')
nama.grid(row=6, column=0, sticky=W, padx=6, pady=6)

app.mainloop()