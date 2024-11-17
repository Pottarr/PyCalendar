from customtkinter import *

very_light_gray = "#d3d3d3"

class ActivityInfoWidget(CTkFrame) :
    def __init__(self, master = None, parent_element = None, activity = None, **kwargs) :
        super().__init__(master, **kwargs, fg_color = very_light_gray)
        self.activity = activity
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)
        self.grid_rowconfigure((0, 1, 2, 3), weight = 1)
        
        
        self.no_activity_selected_label = CTkLabel(self, text = "No Activity Selected", text_color = "black", font = ("Arial", 20))
        if self.activity == None :
            self.no_activity_selected_label.pack(fill = "both", expand = True)
        else :
            self.display_activity_info()
            
    def display_activity_info(self) :
        self.no_activity_selected_label.destroy()
        
        self.name_tile_label = CTkLabel(self, text = "Name")
        self.name_tile_label.grid(row = 0, column = 0, sticky = "nse")
        
        self.name_frame = CTkFrame(self, fg_color = "white")
        self.name_frame.grid(row = 0, column = 1, sticky = "nsew", padx = 2)
        
        self.name_label = CTkLabel(self.name_frame, text = self.activity.name)
        self.name_label.pack(fill = "both")