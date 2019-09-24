from tkinter import *
root = Tk()

def printName(event):
    print('My name is Ashish kumar saini.')

label_1 = Label(root, text = "Id")
label_2 = Label(root, text = 'Password')
entry_1 = Entry(root)
entry_2 = Entry(root) 

label_1.grid(row=0, sticky=E)
label_2.grid(row=1,sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text='Keep me logged in')
c.grid(columnspan=2)

# button_1 = Button(root, text='Name')
# button_1.bind('<Button-1>', printName)
# button_1.grid(row=3)

root.mainloop()