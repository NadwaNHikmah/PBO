import tkinter as tk
from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
import math

class FrmKerucut:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # Pasang Label
        Label(mainFrame, text='Jari-jari Alas:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=4, column=0, sticky=W, padx=5, pady=5)

        # Pasang textbox
        self.txtJariJariAlas = Entry(mainFrame)
        self.txtJariJariAlas.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggi = Entry(mainFrame)
        self.txtTinggi.grid(row=1, column=1, padx=5, pady=5)
        self.txtVolume = Entry(mainFrame)
        self.txtVolume.grid(row=3, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5)

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)

    # Fungsi "onHitung" berfungsi untuk menghitung volume dan luas kerucut
    def onHitung(self, event=None):
        jari_jari_alas = float(self.txtJariJariAlas.get())
        tinggi = float(self.txtTinggi.get())

        volume = (1/3) * math.pi * (jari_jari_alas ** 2) * tinggi
        luas = math.pi * jari_jari_alas * (jari_jari_alas + math.sqrt(jari_jari_alas**2 + tinggi**2))

        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, str(volume))
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))

    def onKeluar(self, event=None):
        # Memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmKerucut(root, "Program Volume dan Luas Kerucut")
    root.mainloop()
