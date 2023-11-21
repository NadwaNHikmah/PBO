from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
import math

class FrmTabung:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Jari-jari:').grid(row=0, column=0,
                                                 sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:").grid(row=1, column=0,
                                              sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=3, column=0,
                                               sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Permukaan:").grid(row=4, column=0,
                                                      sticky=W, padx=5, pady=5)

        self.txtJariJari = Entry(mainFrame)
        self.txtJariJari.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggi = Entry(mainFrame)
        self.txtTinggi.grid(row=1, column=1, padx=5, pady=5)
        self.txtVolume = Entry(mainFrame)
        self.txtVolume.grid(row=3, column=1, padx=5, pady=5)
        self.txtLuasPermukaan = Entry(mainFrame)
        self.txtLuasPermukaan.grid(row=4, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung',
                                command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)

    def onHitung(self, event=None):
        try:
            jari_jari = float(self.txtJariJari.get())
            tinggi = float(self.txtTinggi.get())

            # Hitung volume tabung
            volume = math.pi * jari_jari**2 * tinggi
            self.txtVolume.delete(0, END)
            self.txtVolume.insert(END, str(volume))

            # Hitung luas permukaan tabung
            luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
            self.txtLuasPermukaan.delete(0, END)
            self.txtLuasPermukaan.insert(END, str(luas_permukaan))
        except ValueError:
            self.txtVolume.delete(0, END)
            self.txtVolume.insert(END, "Input harus angka")
            self.txtLuasPermukaan.delete(0, END)
            self.txtLuasPermukaan.insert(END, "Input harus angka")

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmTabung(root, "Program Volume dan Luas Tabung")
    root.mainloop()
