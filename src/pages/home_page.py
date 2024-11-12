from customtkinter import *
import tkcalendar as tkcal
from PIL import Image
import tkinter as tk
from pages.page import Page
import services.auth_system as auth
import time
# from tkcalendar import *
# import widgets.calendar as calendar

alphabet_blue = "#abcdef"
trueman_green= "#aae5a4"
cutie_pink = "#fcd1eb"
python_yellow = "#ffe873"
python_blue = "#306998"

class HomePage(Page) :
    """This class generates the Home Page."""
    def __init__(self, root, login_result) :
        self.root = root
        self.current_user = login_result[0]
        self.file_obj = login_result[1]
        
        self.settings_icon = CTkImage(light_image = Image.open("icons/settings.png"))
        self.logout_icon = CTkImage(light_image = Image.open("icons/logout.png"))
        # self.settings_icon = CTkImage(light_image = Image.open("icons/settings.png"))
        
                
        self.page_frame = CTkFrame(self.root, fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.page_frame.columnconfigure(0, weight = 1)
        self.page_frame.rowconfigure(0, weight = 1)
        self.page_frame.rowconfigure(1, weight = 16)
        self.page_frame.grid(row = 0, column = 0, sticky= "nsew")
        
        self.nav_bar_frame = CTkFrame(self.page_frame, fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.nav_bar_frame.columnconfigure((0, 1, 2), weight = 1)
        self.nav_bar_frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.settings_button = CTkButton(self.nav_bar_frame, fg_color = alphabet_blue, hover_color = alphabet_blue, text = "", image = self.settings_icon, width = 30, height = 30, command = self.go_to_settings)
        self.settings_button.grid(row = 0, column = 0, sticky = "nsw")
        
        self.home_label = CTkLabel(self.nav_bar_frame, text = "HOME PAGE", font = ("Arial", 30))
        # self.home_label.grid(row = 0, column = 0, columnspan = 9)
        self.home_label.grid(row = 0, column = 1, sticky = "ns")
        
        self.logout_button = CTkButton(self.nav_bar_frame, fg_color = alphabet_blue, hover_color = alphabet_blue,text = "", image = self.logout_icon, width = 30, height = 30, command = lambda : self.logout(self.current_user))
        self.logout_button.grid(row = 0, column = 2, sticky = "nse")
        
        self.padding_frame = CTkFrame(self.page_frame, fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.padding_frame.grid_columnconfigure(tuple(i for i in range(16)), weight = 1)
        self.padding_frame.grid_rowconfigure(tuple(i for i in range(9)), weight = 1)
        self.padding_frame.grid(row = 1, column = 0, sticky = "nsew", padx = 50, pady = 50)
        
        self.calendar_frame = CTkFrame(self.padding_frame, bg_color = alphabet_blue)
        # self.calendar_frame.grid_rowconfigure(0, weight = 1)
        # self.calendar_frame.grid_rowconfigure(1, weight = 1)
        # self.calendar_frame.grid(row = 1, column = 1, rowspan = 4, columnspan = 4, sticky = "nsew")
        self.calendar_frame.grid(row = 1, column = 0, rowspan = 6, columnspan = 5, sticky = "nsew")
        # self.calendar_frame.grid(row = 1, column = 1, rowspan = 3, columnspan = 3)
        
        self.calendar = tkcal.Calendar(self.calendar_frame, firstweekday = "sunday", showweeknumbers = False, background = python_blue, headersbackground = python_yellow, headersforeground = "#000000", selectbackground = python_blue)
        # self.calendar.grid(row = 0, column = 0, sticky = "nsew")
        self.calendar.pack(fill = tk.BOTH, expand = True)
        
        self.current_time_label = CTkLabel(self.padding_frame, text = time.strftime("%H:%M:%S"), font = ("Arial", 30))
        self.current_time_label.grid(row = 7, column = 0,columnspan = 5, sticky = "nsew")
        self.current_time_label.after(1000, self.update_current_time)
        
        self.activity_log_frame = CTkFrame(self.padding_frame, bg_color = alphabet_blue)
        # self.activity_log_frame.grid(row = 0, column = 5, rowspan = 7, columnspan = 6, sticky = "nsew")
        self.activity_log_frame.grid(row = 1, column = 10, rowspan = 16, columnspan = 7, sticky = "nsew")
        
    def update_current_time(self) :
        current_time = time.strftime("%H:%M:%S")
        self.current_time_label.configure(text = current_time)
        self.current_time_label.after(1000, self.update_current_time)
            
        
    def logout(self, current_user) :
        auth.logout(self.current_user, self.file_obj)
        self.go_to_login()