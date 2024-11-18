from customtkinter import *
import tkcalendar as tkcal
from datetime import *
from PIL import Image
import tkinter as tk
from pages.page import Page
import services.auth_system as auth
import time

alphabet_blue = "#abcdef"
python_yellow = "#ffe873"
python_blue = "#306998"
python_blue_lighter = "#7bafe3"
very_light_gray = "#d3d3d3"

class HomePage(Page) :
    """This class generates the Home Page."""
    def __init__(self, root, embed_data) :
        self.root = root
        self.current_user = embed_data[0]
        self.file_obj = embed_data[1]
        
        
        
        # Picture for buttons
        self.settings_icon = CTkImage(light_image = Image.open("icons/settings.png"), size = (40, 40))
        self.logout_icon = CTkImage(light_image = Image.open("icons/logout.png"), size = (40, 40))
        
        
           
        self.page_frame = CTkFrame(self.root, fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.page_frame.columnconfigure(0, weight = 1)
        # self.page_frame.rowconfigure((0,1), weight = 1)
        self.page_frame.rowconfigure(0, weight = 1)
        self.page_frame.rowconfigure(1, weight = 16)
        self.page_frame.pack(fill = "both", expand = True)
        
        
        
        self.nav_bar_frame = CTkFrame(self.page_frame, fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.nav_bar_frame.columnconfigure((0, 1, 2), weight = 1)
        self.nav_bar_frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.settings_button = CTkButton(self.nav_bar_frame, fg_color = alphabet_blue, hover_color = alphabet_blue,
                                         text = "", image = self.settings_icon, width = 40, height = 40,
                                         command = lambda : self.go_to_settings(embed_data))
        self.settings_button.grid(row = 0, column = 0, sticky = "nsw")
        
        self.home_label = CTkLabel(self.nav_bar_frame, text = "HOME PAGE", font = ("Arial", 30))
        self.home_label.grid(row = 0, column = 1, sticky = "ns")
        
        self.logout_button = CTkButton(self.nav_bar_frame, fg_color = alphabet_blue, hover_color = alphabet_blue,
                                       text = "", image = self.logout_icon, width = 40, height = 40,
                                       command = self.logout)
        self.logout_button.grid(row = 0, column = 2, sticky = "nse")
        
        self.padding_frame = CTkFrame(self.page_frame, fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.padding_frame.grid_columnconfigure(tuple(i for i in range(16)), weight = 1)
        self.padding_frame.grid_rowconfigure(tuple(i for i in range(9)), weight = 1)
        self.padding_frame.grid(row = 1, column = 0, sticky = "nsew", padx = 50, pady = 50)
        
        
        
        self.calendar_frame = CTkFrame(self.padding_frame)
        self.calendar_frame.grid(row = 1, column = 0, rowspan = 6, columnspan = 5, sticky = "nsew")
        
        
        
        self.calendar = tkcal.Calendar(self.calendar_frame, firstweekday = "sunday", showweeknumbers = False,
                                       background = python_blue, headersbackground = python_yellow,
                                       headersforeground = "#000000", selectbackground = python_blue,
                                       date_pattern = "dd/mm/yyyy")
        self.calendar.pack(fill = tk.BOTH, expand = True)
        
        self.calendar.bind("<<CalendarSelected>>", self.date_detection)
        self.calendar.bind("<<DateEntrySelected>>", self.date_detection)

        
        self.current_time_label = CTkLabel(self.padding_frame, text = time.strftime("%H:%M:%S"),
                                           font = ("Arial", 30))
        self.current_time_label.grid(row = 7, column = 0,columnspan = 5, sticky = "nsew")
        self.current_time_label.after(1000, self.update_current_time)
        
        
        
        self.current_user_label = CTkLabel(self.padding_frame,
                                           text = f"Current User: {self.current_user.get_info().get("username")}",
                                           font = ("Arial", 30))
        self.current_user_label.grid(row = 8, column = 0, columnspan = 5, sticky = "nsew")
        
        
            
        self.activity_log_frame = CTkFrame(self.padding_frame, fg_color = python_blue_lighter)
        self.activity_log_frame.grid_columnconfigure(0, weight = 1)
        self.activity_log_frame.grid_rowconfigure(0, weight = 1)
        self.activity_log_frame.grid_rowconfigure(1, weight = 10)
        self.activity_log_frame.grid(row = 1, column = 6, rowspan = 16, columnspan = 10, sticky = "nsew")
        
        
        
        self.activity_log_nav_bar_frame = CTkFrame(self.activity_log_frame, fg_color = python_blue_lighter)
        self.activity_log_nav_bar_frame.grid_rowconfigure(0, weight = 1)
        self.activity_log_nav_bar_frame.grid_columnconfigure(0, weight = 1)
        self.activity_log_nav_bar_frame.grid(row = 0, column = 0, sticky = "nsew")
        
        
        
        
        # The self.current_date is down here because we need to initialize the Calendar first.
        self.current_date = self.calendar.get_date()
        current_date_obj = datetime.strptime(self.current_date, "%d/%m/%Y").date()
        self.current_day_of_week = current_date_obj.strftime("%A")
        


        self.activity_log_label = CTkLabel(self.activity_log_nav_bar_frame, text = self.current_date,
                                           font = ("Arial", 40))
        self.activity_log_label.grid(row = 0, column = 0, sticky = "nsew")
        
        self.display_activity_log(caller = "not none")
        
        
        
    def update_current_time(self) :
        current_time = time.strftime("%H:%M:%S")
        self.current_time_label.configure(text = current_time)
        self.current_time_label.after(1000, self.update_current_time)
        
    def display_activity_log(self, caller = None) :
        if caller == "not none" :            
            from pages.home_page.widgets.activity_log_list_widget import ActivityLogListWidget
            self.activity_log_list_widget = ActivityLogListWidget(self.activity_log_frame, self, self.current_user, self.current_date, self.current_day_of_week, self.file_obj)
            self.activity_log_list_widget.grid(row = 1, column = 0, sticky = "nsew", padx = 20)
        else :
            self.activity_log_list_widget.destroy()
            
            from pages.home_page.widgets.activity_log_list_widget import ActivityLogListWidget
            self.activity_log_list_widget = ActivityLogListWidget(self.activity_log_frame, self, self.current_user, self.current_date, self.current_day_of_week, self.file_obj)
            self.activity_log_list_widget.grid(row = 1, column = 0, sticky = "nsew", padx = 20)
        
    def display_add_activity(self) :
        from pages.home_page.widgets.add_activity_widget import AddActivityWidget
        self.add_activity_widget = AddActivityWidget(self.activity_log_frame, self, self.current_user, self.current_date, self.file_obj)
        self.add_activity_widget.grid(row = 1, column = 0, sticky = "nsew", padx = 20)
        
    def logout(self) :
        auth.logout(self.current_user, self.file_obj)
        self.go_to_login()
    
    def date_detection(self, event) :
        self.current_date = self.calendar.get_date()
        current_date_obj = datetime.strptime(self.current_date, "%d/%m/%Y").date()
        self.current_day_of_week = current_date_obj.strftime("%A")
        self.activity_log_label.configure(text = self.calendar.get_date())
        self.activity_log_list_widget.destroy()
        self.display_activity_log()
    
    def backward_current_date(self) :
        self.current_date_obj = datetime.strptime(self.current_date, "%d/%m/%Y").date()
        self.current_date_obj -= timedelta(days = 1)
        self.calendar.selection_set(self.current_date_obj)
        self.current_date = self.current_date_obj.strftime("%d/%m/%Y")
        self.activity_log_label.configure(text = self.current_date)
        self.activity_log_list_widget.destroy()
        self.display_activity_log()
        
    def forward_current_date(self) :
        self.current_date_obj = datetime.strptime(self.current_date, "%d/%m/%Y").date()
        self.current_date_obj += timedelta(days = 1)
        self.calendar.selection_set(self.current_date_obj)
        self.current_date = self.current_date_obj.strftime("%d/%m/%Y")
        self.activity_log_label.configure(text = self.current_date)
        self.activity_log_list_widget.destroy()
        self.display_activity_log()
        
    