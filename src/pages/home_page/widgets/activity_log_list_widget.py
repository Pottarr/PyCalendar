from customtkinter import *
from PIL import Image
from datetime import *

alphabet_blue = "#abcdef"
python_blue_lighter = "#7bafe3"
very_light_gray = "#d3d3d3"


class ActivityLogListWidget(CTkFrame) :
    def __init__(self, master = None, parent_element = None, current_user = None, current_date = None, **kwargs,) :
        super().__init__(master, **kwargs, fg_color = python_blue_lighter)
        self.parent_element = parent_element
        self.current_user = current_user
        self.current_date = current_date
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 9)
        self.grid_rowconfigure(1, weight = 1)
        
        self.prev_icon = CTkImage(light_image = Image.open("icons/previous.png"), size = (40, 40))
        self.add_icon = CTkImage(light_image = Image.open("icons/add.png"), size = (40,40))
        self.next_icon = CTkImage(light_image = Image.open("icons/next.png"), size = (40, 40))
        
        
        
        
        self.activity_log_scrollable_frame = CTkScrollableFrame(self, fg_color = very_light_gray)
        self.activity_log_scrollable_frame.grid(row = 0, column = 0, sticky = "nsew")
        
        if len(current_user.get_info().get("activity_log")) == 0 :
            self.no_activity_label = CTkLabel(self.activity_log_scrollable_frame, text = "No Activity", font = ("Arial", 40))
            self.no_activity_label.pack(fill = "both", pady = 200)
        else :
            self.matched_activity = []
            all_activity = self.current_user.get_info().get("activity_log")
            print(all_activity)
            
                        
        self.footer_button_frame = CTkFrame(self, fg_color = python_blue_lighter)
        self.footer_button_frame.grid_columnconfigure((0, 1, 2), weight = 1)
        self.footer_button_frame.grid_rowconfigure(0, weight = 1)
        self.footer_button_frame.grid(row = 1, column = 0, sticky = "nsew")
        
        self.previous_day_button = CTkButton(self.footer_button_frame, fg_color = python_blue_lighter,
                                             hover_color = python_blue_lighter, text = "",
                                             image = self.prev_icon, width = 30, height = 30,
                                             command = self.previous_day)
        self.previous_day_button.grid(row = 0, column = 0, sticky = "nse")
        
        self.add_activity_button = CTkButton(self.footer_button_frame, fg_color = python_blue_lighter,
                                             hover_color = python_blue_lighter, text = "",
                                             image = self.add_icon, width = 30, height = 30,
                                             command = self.add_activity)
        self.add_activity_button.grid(row = 0, column = 1, sticky = "nsew")
        
        self.next_day_button = CTkButton(self.footer_button_frame, fg_color = python_blue_lighter,
                                             hover_color = python_blue_lighter, text = "",
                                             image = self.next_icon, width = 30, height = 30,
                                             command = self.next_day)
        self.next_day_button.grid(row = 0, column = 2, sticky = "nsw")
        
    def previous_day(self) :
        self.parent_element.backward_current_date()
        
    def add_activity(self) :
        print("Add Activity")
        self.destroy()
        self.parent_element.display_add_activity()

    def next_day(self) :
        self.parent_element.forward_current_date()