from tkinter import *
from tkinter import ttk

win = Tk()

f1 = Frame(win)
f1.grid(column=0, row=0)

l1 = Label(f1, text='Enter First Number', font=('arial bold', 20), fg='blue')
l1.grid(column=0, row=0, sticky=W, padx=10)

var1 = StringVar()
a = Entry(f1, font=('arial bold', 20), textvariable=var1)
a.grid(column=0, row=1, padx=10)

l2 = Label(f1, text='', font=('arial bold', 30))
l2.grid(column=0, row=2)

l3 = Label(f1, text='Enter Second Number', font=('arial bold', 20), fg='blue')
l3.grid(column=0, row=3, sticky=W, padx=10)

var2 = StringVar()
c = Entry(f1, font=('arial bold', 20), textvariable=var2)
c.grid(column=0, row=4, sticky=W, padx=10)

Label(f1, text='', font=('arial bold', 30)).grid(column=1, row=0)

f2 = Frame(win)
f2.grid(column=4, row=0, padx=50)

all_var = StringVar()
r1 = ttk.Radiobutton(f2, text='addition', variable=all_var, value='add')
r1.grid(column=1, row=0, sticky=W)

r1 = ttk.Radiobutton(f2, text='subtract', variable=all_var, value='sub')
r1.grid(column=1, row=2, sticky=W)

r1 = ttk.Radiobutton(f2, text='multiply', variable=all_var, value='mul')
r1.grid(column=1, row=3, sticky=W)

r1 = ttk.Radiobutton(f2, text='divide', variable=all_var, value='div')
r1.grid(column=1, row=4, sticky=W)


def action():
    if all_var.get() == 'add':
        q = var1.get()
        w = var2.get()
        dd = int(q) + int(w)
        return Label(text=dd, font=('Cambria', 30), bg='deeppink', fg='white', padx=100).grid(column=0, row=6)

    elif all_var.get() == 'sub':
        q = var1.get()
        w = var2.get()
        dd = int(q) - int(w)
        return Label(text=dd, font=('Cambria', 30), bg='deeppink', fg='white', padx=100).grid(column=0, row=6)

    elif all_var.get() == 'mul':
        q = var1.get()
        w = var2.get()
        dd = int(q) * int(w)
        return Label(text=dd, font=('Cambria', 30), bg='deeppink', fg='white', padx=100).grid(column=0, row=6)

    elif all_var.get() == 'div':
        q = var1.get()
        w = var2.get()
        dd = int(q) / int(w)
        return Label(text=dd, font=('Cambria', 30), bg='deeppink', fg='white', padx=100).grid(column=0, row=6)


Button(f1, text='Solve', padx=50, command=action).grid(column=0, row=5, pady=20)
win.mainloop()
