from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
from celcius import Celcius

class FrmCelcius:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='Celsius:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Fahrenheit:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Reamur:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelvin:").grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.txtCelsius = Entry(mainFrame)
        self.txtCelsius.grid(row=0, column=1, padx=5, pady=5)

        self.txtFahrenheit = Entry(mainFrame)
        self.txtFahrenheit.grid(row=2, column=1, padx=5, pady=5)

        self.txtReamur = Entry(mainFrame)
        self.txtReamur.grid(row=3, column=1, padx=5, pady=5)

        self.txtKelvin = Entry(mainFrame)
        self.txtKelvin.grid(row=4, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)

    def onHitung(self):
        try:
            celsius_value = float(self.txtCelsius.get())
            C = Celcius(celsius_value)

            # Suhu dalam Fahrenheit
            F = C.get_fahrenheit()
            self.update_entry(self.txtFahrenheit, F)

            # Suhu dalam Reamur
            R = C.get_reamur()
            self.update_entry(self.txtReamur, R)

            # Suhu dalam Kelvin
            K = C.get_kelvin()
            self.update_entry(self.txtKelvin, K)
        except ValueError:
            print("Invalid input. Please enter a numeric value for Celsius.")

    def update_entry(self, entry, value):
        entry.delete(0, END)
        entry.insert(END, str(value))

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmCelcius(root, "Program Konversi Suhu Celsius")
    root.mainloop()