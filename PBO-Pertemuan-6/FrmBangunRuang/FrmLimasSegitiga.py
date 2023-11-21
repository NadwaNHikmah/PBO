import tkinter as tk
from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
import math

class FrmLimasSegitiga:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # Pasang Label
        Label(mainFrame, text='Panjang Alas:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi Alas:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi Limas:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=5, column=0, sticky=W, padx=5, pady=5)

        # Pasang textbox
        self.txtPanjangAlas = Entry(mainFrame)
        self.txtPanjangAlas.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggiAlas = Entry(mainFrame)
        self.txtTinggiAlas.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggiLimas = Entry(mainFrame)
        self.txtTinggiLimas.grid(row=2, column=1, padx=5, pady=5)
        self.txtVolume = Entry(mainFrame)
        self.txtVolume.grid(row=4, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=5, column=1, padx=5, pady=5)

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)

    # Fungsi "onHitung" berfungsi untuk menghitung volume dan luas limas segitiga
    def onHitung(self, event=None):
        panjang_alas = float(self.txtPanjangAlas.get())
        tinggi_alas = float(self.txtTinggiAlas.get())
        tinggi_limas = float(self.txtTinggiLimas.get())

        volume = (1/3) * panjang_alas * tinggi_alas * tinggi_limas
        luas = (panjang_alas * tinggi_alas / 2) + (panjang_alas * math.sqrt((tinggi_limas ** 2) + (tinggi_alas ** 2))) + (tinggi_alas * math.sqrt((panjang_alas / 2) ** 2 + tinggi_limas ** 2))

        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, str(volume))
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))

    def onKeluar(self, event=None):
        # Memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmLimasSegitiga(root, "Program Volume dan Luas Limas Segitiga")
    root.mainloop()
