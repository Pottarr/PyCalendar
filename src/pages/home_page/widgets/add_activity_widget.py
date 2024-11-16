from customtkinter import *
from PIL import Image


alphabet_blue = "#abcdef"
python_blue_lighter = "#7bafe3"
very_light_gray = "#d3d3d3"


class AddActivityWidget(CTkFrame) :
    def __init__(self, master = None, parent_element = None, current_user = None, current_date = None, **kwargs,) :
        super().__init__(master, **kwargs, fg_color = python_blue_lighter)
        self.parent_element = parent_element
        self.current_user = current_user
        self.current_date = current_date
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 9)
        self.grid_rowconfigure(1, weight = 1)
        
        
        
        
        self.add_activity_frame = CTkFrame(self, fg_color = very_light_gray)
        self.add_activity_frame.grid(row = 0, column = 0, sticky = "nsew")
        
        
        # self.new_activity_name_label = CTkLabel(self.add_activity_frame, text = "Name")
        # self.new_activity_name_entry = CTkEntry(self.add_activity_frame, )
        
        
        
        
        
            
        self.footer_button_frame = CTkFrame(self, fg_color = python_blue_lighter)
        self.footer_button_frame.grid_columnconfigure(0, weight = 1)
        self.footer_button_frame.grid_rowconfigure(0, weight = 1)
        self.footer_button_frame.grid(row = 1, column = 0, sticky = "nsew")
        
        self.add_activity_button = CTkButton(self.footer_button_frame, fg_color = "green",
                                             hover_color = "green", text = "Save",
                                             command = self.save)
        self.add_activity_button.grid(row = 0, column = 0, sticky = "nsew")
        
    def save(self) :
        print("Save")
        
        self.destroy()
        self.parent_element.display_activity_log()
        