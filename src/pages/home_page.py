import tkinter as tk
# import widgets.calendar as calendar

alphabet_blue = "#abcdef"

class HomePage:
    def __init__(self, root):
        self.root = root
        
        self.page_frame = tk.Frame(self.root, bg = alphabet_blue)
        self.page_frame.grid_columnconfigure(0, weight = 1)
        self.page_frame.grid_rowconfigure(0, weight = 1)
        self.page_frame.grid_rowconfigure(1, weight = 1)
        self.page_frame.grid(row = 0, column = 0, sticky= "nsew")
        
        self.home_label = tk.Label(self.page_frame, text = "HOME PAGE",bg = alphabet_blue)
        self.home_label.grid(row = 0, column = 0)