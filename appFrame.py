import tkinter as tk
from tkinter import *
import pyperclip


class App:

    def __init__(self):
        # Main Frame Creation
        self.master = Tk()
        self.master.title("Delimiter Prototype")
        self.lstStr = '';

        # Labels & Placement
        self.columnarLbl = tk.Label(text="In: Column ")
        self.columnarLbl.grid(column=0, row=0)

        self.linearLbl = tk.Label(text="Out: CSV")
        self.linearLbl.grid(column=2, row=0)

        # Paste
        def leftpaste(event):
            self.colOne.insert(END, pyperclip.paste())

        # Clear
        def clear():
            self.colOne.delete('1.0', END)
            self.colTwo.delete('1.0', END)

        # Text Area Boxes
        self.colOne = tk.Text(self.master, height=25, width=40)
        self.colOne.bind("<Button-1>", leftpaste)
        self.colOne.grid(column=0, row=1)

        self.colTwo = tk.Text(self.master, height=25, width=40)
        self.colTwo.grid(column=2, row=1)

        # Convert function
        def convert():
            self.colTwo.delete('1.0', END)
            # Clear memory on each session
            self.lstStr = ''

            temp = self.colOne.get('1.0', END).split('\r\n')
            # temp = self.colOne.get('1.0', 'end-1c')
            print(temp)
            #print(len(temp))

            temp = list(filter(listChecker, temp))
            print('Post invalid item check')
            print(temp)

            for i in range(len(temp)):
                self.lstStr += temp[i] + ', '


            self.lstStr = self.lstStr.rstrip('\n')
            self.lstStr = self.lstStr.rstrip(' ,')

            self.colTwo.insert(END, self.lstStr)

        # Filter Function
        def listChecker(list):
            invalidItems = ['\n', '', ' ']

            if(list in invalidItems):
                return False
            else:
                return True

        # Buttons
        self.btnColumnar = Button(self.master, text="Columnar Data")
        self.btnColumnar.grid(column=0, row=2)

        self.btnClear = Button(self.master, text="Clear", command=clear)
        self.btnClear.grid(column=1, row=2)


        self.btnConvert = Button(self.master, text="Create CSV", command=convert)
        self.btnConvert.grid(column=2, row=2)

        self.chkOneClick = Checkbutton(self.master, text="Click Less")
        self.chkOneClick.grid(column=1, row=1)

        # Start yer Engines
        self.master.mainloop()


myApp = App()
