from customtkinter import *

class ActivityWidget :
    def __init__(self, root, activity_dict) :
        self.root = root
        self.activity_frame = CTkFrame(self.root)