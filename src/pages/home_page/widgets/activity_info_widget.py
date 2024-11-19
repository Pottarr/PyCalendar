from customtkinter import *
from PIL import Image
from datetime import *
import services.activity as act
import services.activity_configuration as act_con

alphabet_blue = "#abcdef"
python_yellow = "#ffe873"
python_blue = "#306998"
python_blue_lighter = "#7bafe3"
very_light_gray = "#d3d3d3"

class ActivityInfoWidget(CTkFrame) :
    def __init__(self, master = None, parent_element = None, current_user = None, activity = None, file_obj = None, **kwargs) :
        super().__init__(master, **kwargs, fg_color = very_light_gray)
        self.parent_element = parent_element
        self.current_user = current_user
        self.activity = activity
        self.file_obj = file_obj
        self.grid_columnconfigure((0, 1, 2, 3), weight = 1)
        self.grid_rowconfigure((0, 1, 2, 3), weight = 1)
        
        self.delete_icon = CTkImage(light_image = Image.open("icons/delete.png"), size = (20, 20))
        
        
        self.display_activity_info()
            
    def display_activity_info(self) :
        if self.activity != None :
            self.activity.debug_print()
            
        children = self.winfo_children()
        for anything in children :
            anything.destroy()
        
        if self.activity == None :
            
            self.no_activity_selected_label = CTkLabel(self, text = "No Activity Selected", text_color = "black", font = ("Arial", 20))
            self.no_activity_selected_label.grid(row = 0, column = 0, rowspan = 4, columnspan = 4, sticky = "nsew")
        else :        
            
            self.name_tile_label = CTkLabel(self, text = "Title:")
            self.name_tile_label.grid(row = 0, column = 0, sticky = "ew")
            
            self.name_frame = CTkFrame(self, fg_color = "white")
            self.name_frame.grid(row = 0, column = 1, sticky = "ew", padx = 2)
            
            self.name_label = CTkLabel(self.name_frame, text = self.activity.name)
            self.name_label.pack(fill = "both", expand = True)
            
            self.type_title_label = CTkLabel(self, text = "Type:")
            self.type_title_label.grid(row = 0, column = 2, sticky = "ew")
            
            self.type_frame = CTkFrame(self, fg_color = "white")
            self.type_frame.grid(row = 0, column = 3, sticky = "ew", padx = 2)
            self.type_label = CTkLabel(self.type_frame, text = "")
            self.type_label.pack(fill = "both", expand = True)
            
            if isinstance(self.activity, act.NormalActivity) :
                self.type_label.configure(text = "Normal")
            elif isinstance(self.activity, act.RepeatableActivity) :
                self.type_label.configure(text = self.activity.activity_type)
            
            self.description_title = CTkLabel(self, text = "Description:")
            self.description_title.grid(row = 1, column = 0, sticky = "sw", padx = 10)
            
            self.description_frame = CTkScrollableFrame(self, fg_color = "white")
            self.description_frame.grid(row = 2, column = 0, columnspan = 4, sticky = "nsew")
            
            self.description_label = CTkLabel(self.description_frame, text = self.activity.description)
            self.description_label.pack(fill = "both", side = "left")
            

            self.date_title_label = CTkLabel(self, text = "")
            self.date_title_label.grid(row = 1, column = 2, sticky = "ew")
            self.date_frame = CTkFrame(self, fg_color = "white")
            self.date_frame.grid(row = 1, column = 3, sticky = "ew")
            self.date_label = CTkLabel(self.date_frame, text = "")
            self.date_label.pack(fill = "both", expand = True)
            if isinstance(self.activity, act.NormalActivity) :
                self.date_title_label.configure(text = "Date:")
                self.date_label.configure(text = self.activity.date_of_activity)
            elif isinstance(self.activity, act.RepeatableActivity) :
                if self.activity.activity_type == "Daily" :
                    self.date_title_label.configure(text = "Date:")
                    self.date_label.configure(text = "Every day")
                else :
                    self.date_title_label.configure(text = "Occur on:")
                    if self.activity.activity_type == "Weekly" :
                        self.date_label.configure(text = f"Every {self.activity.day_of_week}")
                    elif self.activity.activity_type == "Annually" :
                        activity_date_without_yr = datetime.strptime(self.activity.date_of_activity, "%d/%m/%Y").strftime("%d/%m")
                        self.date_label.configure(text = f"Every {activity_date_without_yr}")
                        
            self.delete_button = CTkButton(self, fg_color = very_light_gray,
                                                    hover_color = very_light_gray, text = "",
                                                    image = self.delete_icon, width = 20, height = 20,
                                                    command = self.delete_activity)
            
            self.delete_button.grid(row = 3, column = 3, sticky = "nse")
        
    def delete_activity(self) :
        act_con.delete_activity(self.current_user, self.activity, self.file_obj)
        self.destroy()
        self.parent_element.display_activity_info()
        self.parent_element.parent_element.display_activity_log()