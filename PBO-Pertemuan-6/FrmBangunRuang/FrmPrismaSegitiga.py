from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
import math

class FrmPrismaSegitiga:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Alas segitiga:').grid(row=0, column=0,
                                                     sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi segitiga:").grid(row=1, column=0,
                                                       sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi prisma:").grid(row=2, column=0,
                                                     sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=4, column=0,
                                              sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Permukaan:").grid(row=5, column=0,
                                                      sticky=W, padx=5, pady=5)

        self.txtAlasSegitiga = Entry(mainFrame)
        self.txtAlasSegitiga.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggiSegitiga = Entry(mainFrame)
        self.txtTinggiSegitiga.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggiPrisma = Entry(mainFrame)
        self.txtTinggiPrisma.grid(row=2, column=1, padx=5, pady=5)
        self.txtVolume = Entry(mainFrame)
        self.txtVolume.grid(row=4, column=1, padx=5, pady=5)
        self.txtLuasPermukaan = Entry(mainFrame)
        self.txtLuasPermukaan.grid(row=5, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung',
                                command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)

    def onHitung(self, event=None):
        try:
            alas_segitiga = float(self.txtAlasSegitiga.get())
            tinggi_segitiga = float(self.txtTinggiSegitiga.get())
            tinggi_prisma = float(self.txtTinggiPrisma.get())

            # Hitung volume prisma segitiga
            volume = (1/2) * alas_segitiga * tinggi_segitiga * tinggi_prisma
            self.txtVolume.delete(0, END)
            self.txtVolume.insert(END, str(volume))

            # Hitung luas permukaan prisma segitiga
            luas_permukaan = (alas_segitiga * tinggi_prisma +
                              2 * alas_segitiga * math.sqrt((tinggi_segitiga ** 2) + ((alas_segitiga / 2) ** 2)))
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
    aplikasi = FrmPrismaSegitiga(root, "Program Volume dan Luas Prisma Segitiga")
    root.mainloop()
