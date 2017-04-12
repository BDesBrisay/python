# CIS 117 Python Programming - Lab 9
# Bryce DesBrisay
import tkinter

class myGUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.text = tkinter.Label(master = self.root, text = 'Bryce DesBrisay')
        self.text.pack()
        self.root.mainloop()

my_GUI = myGUI()


#
# File output:
# 
# White window with my name displayed.
#
