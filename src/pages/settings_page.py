from customtkinter import *

alphabet_blue = "#abcdef"

class SettingsPage :
    """This class generates the Home Page."""
    def __init__(self, root) :
        self.root = root
        
        self.page_frame = CTkFrame(self.root, fg_color = cutie_pink, bg_color = alphabet_blue)
        self.page_frame.grid(row = 0, column = 0, sticky = "nsew")