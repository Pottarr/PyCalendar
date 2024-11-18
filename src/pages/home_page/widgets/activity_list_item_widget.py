from customtkinter import *
from PIL import Image


class ActivityListItemWidget(CTkFrame) :
    def __init__(self, master = None, parent_element = None, activity = None, file_obj = None, **kwargs) :
        super().__init__(master, **kwargs, fg_color = "white", border_color = "black", border_width = 1)
        self.parent_element = parent_element
        self.activity = activity
        self.file_obj = file_obj

        self.info_icon = CTkImage(light_image=Image.open("icons/info.png"))

        self.activity_label = CTkLabel(
            self, text = self.activity.name, text_color = "black")
        self.activity_label.grid(row = 0, column = 0, sticky = "nsew")

        self.info_button = CTkButton(self, fg_color = "white", hover_color = "white", text = "",
                                     image = self.info_icon, width = 30, height = 30,
                                     command = self.display_activity_info)
        self.info_button.grid(row = 0, column = 1, sticky = "nse")
        

    def display_activity_info(self) :
        print("from item")
        self.parent_element.display_activity_info(activity_from_item = self.activity, file_obj = self.file_obj)
