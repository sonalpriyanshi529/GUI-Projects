from tkinter import *
from tkinter import ttk

win = Tk()

# windows size
win.geometry('240x200')
win.resizable(0, 0)

# creating label
Name_Label = Label(text='Name')
Name_Label.grid(column=0, row=0, sticky=W)

Age_Label = Label(text='Age')
Age_Label.grid(column=0, row=2, sticky=W)

Email_Label = Label(text='Email')
Email_Label.grid(column=0, row=3, sticky=W)

Language_label = Label(text='Choose your Language')
Language_label.grid(column=0, row=4, sticky=W)

Genger_Label = Label(text='Who are you ?')
Genger_Label.grid(column=0, row=5, sticky=W)

# entry box and a storing variable class( StringVar() ) to store all the entries.
Name_entry = StringVar()
first = Entry(width=16, textvariable=Name_entry)
first.grid(column=1, row=0)
first.focus()

# like Name_entry, Age_entry will also store the entries as a sting variable by writing in the entry
# 'textvariable=Age_entry'
Age_entry = StringVar()
Entry(width=16, textvariable=Age_entry).grid(column=1, row=2)

# like Name_entry and Age_entry Email_entry will also store the entries as a sting variable by writing in the entry
# 'textvariable=Email_entry'
Email_entry = StringVar()
Entry(width=16, textvariable=Email_entry).grid(column=1, row=3)

# Combobox
Combo_entry = StringVar()
v = ['GUJRATI', 'MARATHI', 'ENGLISH', 'HINDI',
     'OTHER']  # name any variable and then write what we want to show in our combobox.
combo = ttk.Combobox(values=v, width=13, textvariable=Combo_entry, state='readonly')
combo.grid(column=1, row=4)
combo.current(4)

# radiobutton
Genger_entry = StringVar()
ttk.Radiobutton(text='Male', value='Male', variable=Genger_entry).grid(column=1, row=5, sticky=W)
ttk.Radiobutton(text='Female', value='Female', variable=Genger_entry).grid(column=1, row=6, sticky=W)
ttk.Radiobutton(text='Other', value='Other', variable=Genger_entry).grid(column=1, row=7, sticky=W)

# CheckButton
Subscribe_Entry = IntVar()
ttk.Checkbutton(text='Do you want to Subscribe', variable=Subscribe_Entry).grid(columnspan=3, row=8, sticky=W)


# button (sign in)
def action():
    a = Name_entry.get()
    b = Age_entry.get()
    c = Email_entry.get()
    d = Combo_entry.get()
    e = Genger_entry.get()

    if Subscribe_Entry.get() == 0:
        subscribed = 'No'
    else:
        subscribed = 'Yes'

    with open('c.file.txt', 'a') as f:
        f.write(f'Username = {a}, Age = {b}, Email = {c}, Language = {d}, Gender = {e}, Submit = {subscribed}.\n')


Button(text='SUBMIT', command=action).grid(column=1, row=11, sticky=EW)

win.mainloop()
