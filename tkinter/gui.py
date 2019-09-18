#importing all the submodule from the tkinter module
from tkinter import *

root = Tk() #creats a blank window named as 'root'
topFrame = Frame(root) #creating a invisible fram on the window (root)
topFrame.pack() #creats a frame on the window and fitting anywhere on the window(root)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM) #this frame is at bottom side of the window
button1 = Button(topFrame, text="Ashish", fg="blue")
button2 = Button(topFrame, text="Praveen", fg="green")
button3 = Button(bottomFrame, text="Jugnu", fg="red")
button4 = Button(bottomFrame, text="Rachit", fg="black")
button1.pack(side=LEFT)
button2.pack(side=LEFT) 
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


theLable = Label(root, text="Ashish kumar saini") #'Label' is used to showing any text on the window and takes two parameter, created window (root) and text which is shown
theLable.pack() #'pack' is used to show the label anywhere on the window where it can fit
root.mainloop() #'mainloop' is used for popup that window(root) 

