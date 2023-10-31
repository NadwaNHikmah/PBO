import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

# create tkinter object
app = tk.Tk()

# atur ukuran window
app.geometry("450x450")

# tambahkan judul
app.title("Kalkulator Luas dan Keliling Kerucut")

# window
frame = Frame(app)
frame.pack(padx=20, pady=20)

app.mainloop()