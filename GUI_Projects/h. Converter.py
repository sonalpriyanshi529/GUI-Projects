from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry('700x500')
win.title("Priyanshi")
combo_var = StringVar()

Label(text='Binary To All Number System Converter', font=('arial bold', 20)).grid(column=0, row=1, padx=50)

Label(text="").grid(column=0, row=2)
Label(text="Enter Binary Number:", font=('arial bold', 10)).grid(column=0, row=3, columnspan=2, sticky=W, padx=250)
Label(text="Decimal Number System :", font=('arial bold', 10)).grid(column=0, row=9, columnspan=2, sticky=W, padx=250)
Label(text="", bg="white", font=("Arial bold", 30), borderwidth=5, relief=GROOVE).grid(column=0, row=10, columnspan=2,ipadx=200)

Label(text="").grid(column=0, row=11)
Label(text="Hexadecimal Number System :", font=('arial bold', 10)).grid(column=0, row=12, columnspan=2, sticky=W,padx=250)
Label(text="", bg="white", font=("Arial bold", 30), borderwidth=5, relief=GROOVE).grid(column=0, row=13, columnspan=2,ipadx=200)

Label(text="").grid(column=0, row=14)
Label(text="Octal Number System :", font=('arial bold', 10)).grid(column=0, row=14, columnspan=2, sticky=W, padx=250)
Label(text="", bg="white", font=("Arial bold", 30), borderwidth=5, relief=GROOVE).grid(column=0, row=15, columnspan=2,ipadx=200)

bin_var = StringVar()
Entry(textvariable=bin_var, font=('arial bold', 20)).grid(column=0, row=4, columnspan=2)


def bin_dec():
        binary = bin_var.get()
        a = int(binary, 2)
        b = hex(a)
        b = b[2:]
        c = oct(a)
        c = c[2:]
        b = b.upper()
        decimal = Label(text=a, font=("Arial bold", 20), bg="white", borderwidth=1).grid(column=0, row=10, columnspan=2, ipadx=100)
        hexadecimal = Label(text=b, font=("Arial bold", 20), bg="white", borderwidth=1).grid(column=0, row=13, columnspan=2, ipadx=100)
        return decimal, hexadecimal, Label(text=c, font=("Arial bold", 20), bg="white", borderwidth=1).grid(column=0, row=15, columnspan=2, ipadx=100)


def dec_bin():
    gg = bin_var.get()
    d = bin(gg)

    a = d[2:]
    return Label(text=a, font=("Arial bold", 20)).grid(column=0, row=6)


Label(text="").grid(column=0, row=5)
Button(text='CONVERT', command=bin_dec, font=10,bg="deeppink",fg="white").grid(column=0, row=6, columnspan=2)
Label(text="").grid(column=0, row=7)

win.mainloop()
