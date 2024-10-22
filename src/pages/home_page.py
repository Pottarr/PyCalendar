from customtkinter import *
import tkcalendar as tkcal
from PIL import Image
import tkinter as tk
# from tkcalendar import *
# import widgets.calendar as calendar

alphabet_blue = "#abcdef"
trueman_green = "#aae5a4"
cutie_pink = "#fcd1eb"

class HomePage:
    """This class generates the Home Page."""
    def __init__(self, root) :
        self.root = root
        
        self.page_frame = CTkFrame(self.root, fg_color = trueman_green, bg_color = trueman_green)
        self.page_frame.columnconfigure(0, weight = 1)
        self.page_frame.rowconfigure(0, weight = 1)
        self.page_frame.rowconfigure(1, weight = 16)
        self.page_frame.grid(row = 0, column = 0, sticky= "nsew")
        
        self.nav_bar_frame = CTkFrame(self.page_frame, fg_color = trueman_green, bg_color = trueman_green)
        self.nav_bar_frame.columnconfigure((0, 1, 2), weight = 1)
        self.nav_bar_frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.setting_icon_png = CTkImage(light_image = Image.open("icons\settings.png"), size = (30, 30)) 
        self.setting_icon = CTkButton(self.nav_bar_frame, image = self.setting_icon_png, command = self.go_to_settings())
        self.setting_icon.grid(row = 0, column = 0, sticky = "nsw")
        
        self.home_label = CTkLabel(self.nav_bar_frame, text = "HOME PAGE")
        # self.home_label.grid(row = 0, column = 0, columnspan = 9)
        self.home_label.grid(row = 0, column = 1, sticky = "ns")
        
        self.padding_frame = CTkFrame(self.page_frame, fg_color = trueman_green, bg_color = trueman_green)
        self.padding_frame.grid_columnconfigure(tuple(i for i in range(16)), weight = 1)
        self.padding_frame.grid_rowconfigure(tuple(i for i in range(9)), weight = 1)
        self.padding_frame.grid(row = 1, column = 0, sticky = "nsew", padx = 50, pady = 50)
        
        self.calendar_frame = CTkFrame(self.padding_frame, bg_color = alphabet_blue)
        # self.calendar_frame.grid_rowconfigure(0, weight = 1)
        # self.calendar_frame.grid_rowconfigure(1, weight = 1)
        # self.calendar_frame.grid(row = 1, column = 1, rowspan = 4, columnspan = 4, sticky = "nsew")
        self.calendar_frame.grid(row = 1, column = 0, rowspan = 6, columnspan = 5, sticky = "nsew")
        # self.calendar_frame.grid(row = 1, column = 1, rowspan = 3, columnspan = 3)
        
        self.calendar = tkcal.Calendar(self.calendar_frame, firstweekday = "sunday", showweeknumbers = False)
        # self.calendar.grid(row = 0, column = 0, sticky = "nsew")
        self.calendar.pack(fill = tk.BOTH, expand = True)
        
        self.activity_log_frame = CTkFrame(self.padding_frame, bg_color = alphabet_blue)
        # self.activity_log_frame.grid(row = 0, column = 5, rowspan = 7, columnspan = 6, sticky = "nsew")
        self.activity_log_frame.grid(row = 1, column = 10, rowspan = 16, columnspan = 7, sticky = "nsew")
        
        # self.edit_activity_frame = tk.Frame(self.page_frame, bg_color = cutie_pink)
        
    def go_to_settings(self) :
        import pages.setting_page as setting_page
        self.page_frame.destroy()
        setting_page.SettingPage(self.root)