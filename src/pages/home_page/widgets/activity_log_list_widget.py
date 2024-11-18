from customtkinter import *
from PIL import Image
from datetime import *
import services.activity as act
from pages.home_page.widgets.activity_list_item_widget import ActivityListItemWidget
from pages.home_page.widgets.activity_info_widget import ActivityInfoWidget

alphabet_blue = "#abcdef"
python_yellow = "#ffe873"
python_blue = "#306998"
python_blue_lighter = "#7bafe3"
very_light_gray = "#d3d3d3"

class ActivityLogListWidget(CTkFrame) :
    def __init__(self, master = None, parent_element = None, current_user = None, current_date = None,
                 current_day_of_week = None, file_obj = None, **kwargs) :
        super().__init__(master, **kwargs, fg_color = python_blue_lighter)
        print("ActivityLogListWidget was loaded")
        self.parent_element = parent_element
        self.current_user = current_user
        self.current_date = current_date
        self.current_day_of_week = current_day_of_week
        self.file_obj = file_obj
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 9)
        self.grid_rowconfigure(1, weight = 1)
        
        self.prev_icon = CTkImage(light_image = Image.open("icons/previous.png"), size = (40, 40))
        self.add_icon = CTkImage(light_image = Image.open("icons/add.png"), size = (40,40))
        self.next_icon = CTkImage(light_image = Image.open("icons/next.png"), size = (40, 40))
        
        self.activity_multi_info_frame = CTkFrame(self, fg_color = python_blue_lighter)
        self.activity_multi_info_frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.activity_log_scrollable_frame = CTkScrollableFrame(self.activity_multi_info_frame,
                                                                fg_color = very_light_gray)
        self.activity_log_scrollable_frame.pack(fill = "both", expand = True, side = "left", padx = 5)
        
        if len(current_user.get_info().get("activity_log")) == 0 :
            self.no_activity_label = CTkLabel(self.activity_log_scrollable_frame, text = "No Activity",
                                              font = ("Arial", 40))
            self.no_activity_label.pack(fill = "both", expand = True, pady = 125)
        else :
            self.matched_activity = []
            all_activity = self.current_user.get_info().get("activity_log")
            for activity in all_activity :
                # Filter by normal
                if isinstance(activity, act.NormalActivity) :
                    if activity.date_of_activity == self.current_date :
                        self.matched_activity.append(activity)
                elif isinstance(activity, act.RepeatableActivity) :
                    # Filter by Daily
                    if activity.activity_type == "Daily" :
                        self.matched_activity.append(activity)
                    # Filter by Weekly
                    elif activity.activity_type == "Weekly" :
                        if self.current_day_of_week == activity.day_of_week :
                            self.matched_activity.append(activity)
                    # Filter by Annnualy
                    elif activity.activity_type == "Annually" :
                        current_date_obj = datetime.strptime(self.current_date, "%d/%m/%Y")
                        activity_date_obj = datetime.strptime(activity.date_of_activity, "%d/%m/%Y")
                        print(current_date_obj)
                        print(activity_date_obj)
                        if current_date_obj == activity_date_obj :
                            self.matched_activity.append(activity)
                            
            self.all_activity_frame = []
            for activity in self.matched_activity :
                activity_frame = ActivityListItemWidget(self.activity_log_scrollable_frame, self, activity,
                                                        self.file_obj)
                activity_frame.grid_columnconfigure(0, weight = 1)
                activity_frame.grid_rowconfigure(0, weight = 1)
                
                self.all_activity_frame.append(activity_frame)
            
            for activity_frame in self.all_activity_frame :
                activity_frame.pack(fill = "x", pady = 5)
                
        self.activity_info_frame = CTkFrame(self.activity_multi_info_frame, fg_color = very_light_gray)
        self.activity_info_frame.grid_columnconfigure(0, weight = 1)
        self.activity_info_frame.grid_rowconfigure(0, weight = 1)
        self.activity_info_frame.pack(fill = "both", expand = True, side = "right", padx = 5)
        
        self.display_activity_info()
                        
        self.footer_button_frame = CTkFrame(self, fg_color = python_blue_lighter)
        self.footer_button_frame.grid_columnconfigure((0, 1, 2), weight = 1)
        self.footer_button_frame.grid_rowconfigure(0, weight = 1)
        self.footer_button_frame.grid(row = 1, column = 0, columnspan = 2, sticky = "nsew", pady = 5)
        
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
        
    def display_activity_info(self, activity_from_item = None, file_obj = None) :
        print("from log")
        self.activity_info_widget = ActivityInfoWidget(self.activity_info_frame, parent_element = self,
                                                       current_user = self.current_user,
                                                       activity = activity_from_item, file_obj = self.file_obj)
        self.activity_info_widget.grid(row = 0, column = 0, sticky = "nsew")
            
    def previous_day(self) :
        self.parent_element.backward_current_date()
        
    def add_activity(self) :
        print("Add Activity")
        self.destroy()
        self.parent_element.display_add_activity()

    def next_day(self) :
        self.parent_element.forward_current_date()