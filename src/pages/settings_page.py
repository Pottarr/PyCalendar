from customtkinter import *

cutie_pink = "#fcd1eb"

class SettingsPage :
    """This class generates the Home Page."""
    def __init__(self, root) :
        self.root = root
        
        self.page_frame = CTkFrame(self.root, fg_color = cutie_pink, bg_color = cutie_pink)
        self.page_frame.grid(row = 0, column = 0, sticky = "nsew")