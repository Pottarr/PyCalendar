from customtkinter import *
import tkcalendar as tkcal
from datetime import datetime
from PIL import Image
import tkinter as tk
from pages.page import Page
import services.auth_system as auth
import time
# from tkcalendar import *
# import widgets.calendar as calendar

alphabet_blue = "#abcdef"
# trueman_green= "#aae5a4"
# cutie_pink = "#fcd1eb"
python_yellow = "#ffe873"
python_blue = "#306998"
python_blue_lighter = "#7bafe3"

class HomePage(Page) :
    """This class generates the Home Page."""
    def __init__(self, root, login_result) :
        self.root = root
        self.current_user = login_result[0].get_info()
        self.file_obj = login_result[1]
        
        
        
        # Picture for buttons
        self.settings_icon = CTkImage(light_image = Image.open("icons/settings.png"))
        self.logout_icon = CTkImage(light_image = Image.open("icons/logout.png"))
        
        
           
        self.page_frame = CTkFrame(self.root, fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.page_frame.columnconfigure(0, weight = 1)
        # self.page_frame.rowconfigure((0,1), weight = 1)
        self.page_frame.rowconfigure(1, weight = 16)
        self.page_frame.grid(row = 0, column = 0, sticky= "nsew")
        
        
        
        self.nav_bar_frame = CTkFrame(self.page_frame, fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.nav_bar_frame.columnconfigure((0, 1, 2), weight = 1)
        self.nav_bar_frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.settings_button = CTkButton(self.nav_bar_frame, fg_color = alphabet_blue, hover_color = alphabet_blue,
                                         text = "", image = self.settings_icon, width = 30, height = 30,
                                         command = self.go_to_settings)
        self.settings_button.grid(row = 0, column = 0, sticky = "nsw")
        
        self.home_label = CTkLabel(self.nav_bar_frame, text = "HOME PAGE", font = ("Arial", 30))
        self.home_label.grid(row = 0, column = 1, sticky = "ns")
        
        self.logout_button = CTkButton(self.nav_bar_frame, fg_color = alphabet_blue, hover_color = alphabet_blue,
                                       text = "", image = self.logout_icon, width = 30, height = 30,
                                       command = lambda : self.logout(self.current_user))
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
        
        
        
        self.current_time_label = CTkLabel(self.padding_frame, text = time.strftime("%H:%M:%S"),
                                           font = ("Arial", 30))
        self.current_time_label.grid(row = 7, column = 0,columnspan = 5, sticky = "nsew")
        self.current_time_label.after(1000, self.update_current_time)
        
        
        
        self.current_user_label = CTkLabel(self.padding_frame,
                                           text = f"Current User: {self.current_user.get("username")}",
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
        


        self.activity_log_label = CTkLabel(self.activity_log_nav_bar_frame, text = self.current_date,
                                           font = ("Arial", 40))
        self.activity_log_label.grid(row = 0, column = 0, sticky = "nsew")
        
        
        
        self.display_activity_log()
        
        
        
    def update_current_time(self) :
        current_time = time.strftime("%H:%M:%S")
        self.current_time_label.configure(text = current_time)
        self.current_time_label.after(1000, self.update_current_time)
        
    def display_activity_log(self) :
        from pages.home_page.widgets.activity_log_list_widget import ActivityLogListWidget
        self.activity_log_list_widget = ActivityLogListWidget(self.activity_log_frame, self, self.current_user, self.current_date)
        self.activity_log_list_widget.grid(row = 1, column = 0, sticky = "nsew", padx = 20)
        
    def display_add_activity(self) :
        from pages.home_page.widgets.add_activity_widget import AddActivityWidget
        self.add_activity_widget = AddActivityWidget(self.activity_log_frame, self, self.current_user, self.current_date)
        self.add_activity_widget.grid(row = 1, column = 0, sticky = "nsew", padx = 20)
        
    def logout(self, current_user) :
        auth.logout(self.current_user, self.file_obj)
        self.go_to_login()