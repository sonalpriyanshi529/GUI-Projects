from tkinter import *

win = Tk()
win.geometry("650x250")

l1 = Label(text='Comparison', font=('Arial Bold', 50))
l1.grid(column=0, row=0, columnspan=10)

Label().grid(column=0, row=1)

var1 = IntVar()
num1 = Entry(width=3, font=('Arial Bold', 20), textvariable=var1)
num1.grid(column=0, row=2, sticky=W, padx=90)

Label(text="", font=('Arial Bold', 30)).grid(column=1, row=2, padx=10)

var2 = IntVar()
num2 = Entry(width=3, font=('Arial Bold', 20), textvariable=var2)
num2.grid(column=2, row=2, sticky=W, padx=80)

Label().grid(column=0, row=4)


def action():
    try:
        if var1.get() > var2.get():
            return Label(text=">", font=('Arial Bold', 30)).grid(column=1, row=2, padx=10)
        elif var1.get() < var2.get():
            return Label(text="<", font=('Arial Bold', 30)).grid(column=1, row=2, padx=10)
        elif var1.get() == var2.get():
            return Label(text="=", font=('Arial Bold', 30)).grid(column=1, row=2, padx=10)
    except Exception as e:
        return Label(text="Error", font=('Arial Bold', 10)).grid(column=1, row=2, padx=10)


Button(text="Solve", command=action).grid(column=1, row=5, ipadx=80)

win.mainloop()
