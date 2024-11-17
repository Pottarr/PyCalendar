from customtkinter import *

alphabet_blue = "#abcdef"
python_yellow = "#ffe873"
python_blue = "#306998"
python_blue_lighter = "#7bafe3"

class SettingsPage :
    """This class generates the Home Page."""
    def __init__(self, root) :
        self.root = root
        
        self.page_frame = CTkFrame(self.root, fg_color = alphabet_blue)
        self.page_frame.grid_rowconfigure(0, weight = 1)
        self.page_frame.grid_rowconfigure(0, weight = 1)
        self.page_frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.padding_frame = CTkFrame(self.page_frame, fg_color = python_blue_lighter)
        self.padding_frame.grid_columnconfigure((0, 1), weight = 1)
        self.padding_frame.grid_rowconfigure((0, 1), weight = 1)
        self.padding_frame.grid(row = 0, column = 0, sticky = "nsew", padx = 400, pady = 150)
        
        
        