from tkinter import*

root = Tk()

def printName(event):
    print('My name is Ashish kumar saini.')


button_1 = Button(root, text='Name')
button_1.bind('<Button-1>', printName)
button_1.pack()




root.mainloop()