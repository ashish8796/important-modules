from tkinter import *

class AshishButtons:


    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.printButton = Button(frame, text='button', command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text='Quit', command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print('Wow, this actually worked!')


root = Tk()
a = AshishButtons(root)
root.mainloop()