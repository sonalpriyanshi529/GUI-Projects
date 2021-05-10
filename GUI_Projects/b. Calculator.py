from tkinter import *

win = Tk()
win.resizable(0, 0)
win.title('Priyanshi Calculator')

Label(text='PRIYANSHI CALCULATOR', font=('arial bold', 30)).grid(column=0, row=0)
Label(text='Enter your equation', font=20, pady=20).grid(column=0, row=1)

Equation = StringVar()
Entry_box = Entry(textvariable=Equation, font=('lucida', 20))
Entry_box.grid(column=0, row=2)
Entry_box.focus()


def solve():
    try:
        a = eval(Equation.get())
        return Label(text=a, font=('arialbold', 20), bg='deeppink', fg='white').grid(column=0, row=4, sticky=EW)
    except Exception as e:
        return Label(text='ERROR', font=('arialbold', 20), bg='deeppink', fg='white').grid(column=0, row=4, sticky=EW)


Button(text='SOLVE', command=solve, bg='purple', fg='pink', font=100).grid(column=0, row=3, sticky=EW)

win.mainloop()
