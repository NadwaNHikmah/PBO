import tkinter as tk
from tkinter import Menu
from FrmPersegi import *
from FrmSegitiga import *
from FrmLingkaran import *
from FrmTabung import *
from FrmPrismaSegitiga import *
from FrmKubus import *
from FrmBalok import *
from FrmBola import *
from FrmKerucut import *
from FrmLimasSegitiga import *
from FrmLimasSegiEmpat import *

import tkinter as tk

def NadzwaNurulHikmah_220511099():
    saya = Entry.get() 

# Membuat jendela utama
root = tk.Tk()
root.title("Nadzwa Nurul Hikmah 220511099")

# Membuat label "Saya adalah:"
label_saya = tk.Label(root, text="Saya adalah:")
label_saya.pack(pady=10)

# Membuat tombol untuk menambahkan nama
tombol_tambah = tk.Button(root, text="Nadzwa Nurul Hikmah 220511099", command=NadzwaNurulHikmah_220511099)
tombol_tambah.pack(pady=10)

# Membuat label untuk menampilkan hasil
label_hasil = tk.Label(root, text="")
label_hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()


# root window
root = tk.Tk()
root.title('Menu Demo')
#root.attributes('-fullscreen', True)
root.geometry("900x400")
# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
app_menu = Menu(menubar)
data_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='File Open', command=root.destroy
)

file_menu.add_command(
    label='Exit', command=root.destroy
)

app_menu.add_command(
    label='App Persegi', command= lambda: new_window("Luas Persegi", FrmPersegi)
)
app_menu.add_command(
    label='App Segitiga', command= lambda: new_window("Luas Segitiga", FrmSegitiga)
)
app_menu.add_command(
    label='App Lingkaran', command= lambda: new_window("Luas Lingkaran", FrmLingkaran)
)
app_menu.add_command(
    label='App Tabung', command= lambda: new_window("Luas Tabung", FrmTabung)
)
app_menu.add_command(
    label='App PrismaSegitiga', command= lambda: new_window("Luas PrismaSegitiga", FrmSegitiga)
)
app_menu.add_command(
    label='App Kubus', command= lambda: new_window("Luas Kubus", FrmKubus)
)
app_menu.add_command(
    label='App Balok', command= lambda: new_window("Luas Balok", FrmBalok)
)
app_menu.add_command(
    label='App Bola', command= lambda: new_window("Luas Bola", FrmBola)
)
app_menu.add_command(
    label='App Kerucut', command= lambda: new_window("Luas Kerucut", FrmKerucut)
)
app_menu.add_command(
    label='App LimasSegitiga', command= lambda: new_window("Luas LimasSegitiga", FrmLimasSegitiga)
)
app_menu.add_command(
    label='App LimasSegiEmpat', command= lambda: new_window("Luas LimasSegiEmpat", FrmLimasSegiEmpat)
)

def new_window( number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)

# add the File menu to the menubar
menubar.add_cascade(
    label="File", menu=file_menu
)
menubar.add_cascade(
    label="App", menu=app_menu
)
    
root.mainloop()