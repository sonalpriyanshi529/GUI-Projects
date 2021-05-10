from tkinter import *
win=Tk()
win.title('Priyanshi Calculator')
win.geometry('228x486')
win.resizable(0,0)

#Entry Box
Entry_box=Entry(width=8,font=('Arial bold',30),borderwidth=15)
Entry_box.grid(columnspan=100,row=0)


#Functions of number buttons
def seven():
    a=Entry_box.get()
    Entry_box.delete(0,END)
    Entry_box.insert(0,a+'7')

def eight():

    b=Entry_box.get()
    Entry_box.delete(0,END)
    Entry_box.insert(0,b+'8')
    
def nine():
    a=Entry_box.get()
    Entry_box.delete(0,END)
    Entry_box.insert(0,a+'9')

def four():
    b=Entry_box.get()
    Entry_box.delete(0,END)
    Entry_box.insert(0,b+'4')
    
def five():
    a=Entry_box.get()
    Entry_box.delete(0,END)
    Entry_box.insert(0,a+'5')

def six():
    b=Entry_box.get()
    Entry_box.delete(0,END)
    Entry_box.insert(0,b+'6')
    
def one():
    a=Entry_box.get()
    Entry_box.delete(0,END)
    Entry_box.insert(0,a+'1')

def two():
    b=Entry_box.get()
    Entry_box.delete(0,END)
    Entry_box.insert(0,b+'2')

def three():
    b=Entry_box.get()
    Entry_box.delete(0,END)
    Entry_box.insert(0,b+'3')

def zero():
    b=Entry_box.get()
    Entry_box.delete(0,END)
    Entry_box.insert(0,b+'0')


#Function of operator Buttons
def AC():
    Entry_box.delete(0,END)
    
def mul():
    b=Entry_box.get()
    Entry_box.delete(0,END)
    Entry_box.insert(0,b+'*')

def add():
    b=Entry_box.get()
    Entry_box.delete(0,END)
    Entry_box.insert(0,b+'+')

def sub():
    b=Entry_box.get()
    Entry_box.delete(0,END)
    Entry_box.insert(0,b+'-')

def B():
    b=Entry_box.get()
    a=len(b)
    a=a-1
    Entry_box.delete(a,END)

def div():
    b=Entry_box.get()
    Entry_box.delete(0,END)
    Entry_box.insert(0,b+'/')

def ans():
    
    try:
        b=eval(Entry_box.get())
        Entry_box.delete(0,END)
        return Entry_box.insert(0,b)
    except:
        Entry_box.delete(0,END)
        return Entry_box.insert(0,'ERROR')
        

#All the buttons
Button(text='AC',command=AC,font=('Arial bold',19),pady=15).grid(column=0,row=1,sticky=W)
Button(text='←',command=B,font=('Arial bold',30),padx=22).grid(column=1,row=1,sticky=W,columnspan=2)
Button(text='÷',command=div,font=('Arial bold',27),pady=5).grid(column=3,row=1,sticky=W)

Button(text='7',command=seven,font=('Arial bold',30)).grid(column=0,row=2,sticky=W)
Button(text='8',command=eight,font=('Arial bold',30)).grid(column=1,row=2,sticky=W)
Button(text='9',command=nine,font=('Arial bold',30)).grid(column=2,row=2,sticky=W)
Button(text='*',command=mul,font=('Arial bold',30)).grid(column=3,row=2,sticky=W)

Button(text='4',command=four,font=('Arial bold',30)).grid(column=0,row=3,sticky=W)
Button(text='5',command=five,font=('Arial bold',30)).grid(column=1,row=3,sticky=W)
Button(text='6',command=six,font=('Arial bold',30)).grid(column=2,row=3,sticky=W)
Button(text='+',command=add,font=('Arial bold',26),pady=6).grid(column=3,row=3,sticky=W)

Button(text='1',command=one,font=('Arial bold',30)).grid(column=0,row=4,sticky=W)
Button(text='2',command=two,font=('Arial bold',30)).grid(column=1,row=4,sticky=W)
Button(text='3',command=three,font=('Arial bold',30)).grid(column=2,row=4,sticky=W)
Button(text='-',command=sub,font=('Arial bold',30),padx=3).grid(column=3,row=4,sticky=W)

Button(text='0',command=zero,font=('Arial bold',30)).grid(column=0,row=5,sticky=W)
Button(text='=',command=ans,font=('Arial bold',30),padx=57,bg='pink').grid(column=1,row=5,sticky=W,columnspan=10)

win.mainloop()