import tkinter as tk
from tkinter import *
import pyperclip


class App:

    def __init__(self):
        # Main Frame Creation
        self.master = Tk()
        self.master.title("Delimiter Prototype")
        self.csv = []
        self.lstStr = '';

        # Labels & Placement
        self.columnarLbl = tk.Label(text="In: Column ")
        self.columnarLbl.grid(column=0, row=0)

        self.linearLbl = tk.Label(text="Out: CSV")
        self.linearLbl.grid(column=1, row=0)

        # Paste
        def leftpaste(event):
            self.colOne.insert(END, pyperclip.paste())

        # Clear
        def clear():
            self.colOne.delete('1.0', END)

        # Text Area Boxes
        self.colOne = tk.Text(self.master, height=25, width=40)
        self.colOne.bind("<Button-1>", leftpaste)
        self.colOne.grid(column=0, row=1)

        self.colTwo = tk.Text(self.master, height=25, width=40)
        self.colTwo.grid(column=1, row=1)

        # Convert function
        def convert():
            self.colTwo.delete('1.0', END)
            self.lstStr = ''
            temp = self.colOne.get('1.0', END).split('\r\n')
            # temp = self.colOne.get('1.0', 'end-1c')
            print(temp)
            print(len(temp))
            length = len(temp) - 1

            for i in range(length):
                self.lstStr += temp[i] + ', '

            self.lstStr = self.lstStr.lstrip(', ')

            self.lstStr = self.lstStr.strip()

            self.colTwo.insert(END, self.lstStr.rstrip(', '))
            print(self.lstStr)


        # Buttons
        self.btnClear = Button(self.master, text="Clear", command=clear)
        self.btnClear.grid(column=0, row=2)


        self.btnConvert = Button(self.master, text="Convert", command=convert)
        self.btnConvert.grid(column=1, row=2)

        self.master.mainloop()


myApp = App()
