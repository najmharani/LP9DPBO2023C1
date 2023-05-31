from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image

hunians = []
hunians.append(Apartemen( "Nelly Joy", 3, 3, 2,"tunai"))
hunians.append(Rumah("Sekar MK", 5, 2, 400, "cicilan"))
hunians.append(Indekos("Bp. Romi", "Cahya", "tunai", True))
hunians.append(Rumah("Satria", 1, 4, 200, "kredit"))

root = Tk()
root.title("Latihan Praktikum DPBO Python")

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w")

    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)

    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)

def home():
    top = Toplevel()
    top.title("Home")
    frame = LabelFrame(top, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(top, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_exit = Button(opts, text="Exit", command=top.destroy)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

frame = Label(root, text="Selamat Datang Di Database Hunian", padx=10, pady=10)
frame.pack(padx=10, pady=10)

landing_img = ImageTk.PhotoImage(Image.open("img/landing.png"))
landing_label = Label(image=landing_img)
landing_label.pack()

b_home = Button(root, text="Home", command=home)
b_home.pack(padx=10, pady=10)

root.mainloop()
