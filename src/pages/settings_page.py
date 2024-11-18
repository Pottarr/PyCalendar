from customtkinter import *
from PIL import Image
from pages.page import Page
import services.pickle_system as pkl
import services.auth_system as auth
import services.user_configuration as user_con

alphabet_blue = "#abcdef"
python_yellow = "#ffe873"
python_blue = "#306998"
python_blue_lighter = "#7bafe3"
very_light_gray = "#d3d3d3"

class SettingsPage(Page) :
    """This class generates the Home Page."""
    def __init__(self, root, embed_data) :
        self.root = root
        self.current_user = embed_data[0]
        self.file_obj = embed_data[1]
        
        # Picture for buttons
        self.home_icon = CTkImage(light_image = Image.open("icons/home.png"), size = (40, 40))
        self.logout_icon = CTkImage(light_image = Image.open("icons/logout.png"), size = (40, 40))
        
        self.page_frame = CTkFrame(self.root, fg_color = alphabet_blue)
        self.page_frame.columnconfigure(0, weight = 1)
        # self.page_frame.rowconfigure((0,1), weight = 1)
        self.page_frame.rowconfigure(0, weight = 1)
        self.page_frame.rowconfigure(1, weight = 16)
        self.page_frame.pack(fill = "both", expand = True)
        
        self.nav_bar_frame = CTkFrame(self.page_frame, fg_color = alphabet_blue)
        self.nav_bar_frame.columnconfigure((0, 1, 2), weight = 1)
        self.nav_bar_frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.home_button = CTkButton(self.nav_bar_frame, fg_color = alphabet_blue, hover_color = alphabet_blue,
                                         text = "", image = self.home_icon, width = 40, height = 40,
                                         command = lambda : self.go_to_home(embed_data))
        self.home_button.grid(row = 0, column = 0, sticky = "nsw")
        
        self.settings_label = CTkLabel(self.nav_bar_frame, text = "SETTINGS PAGE", font = ("Arial", 30))
        self.settings_label.grid(row = 0, column = 1, sticky = "ns")
        
        self.logout_button = CTkButton(self.nav_bar_frame, fg_color = alphabet_blue, hover_color = alphabet_blue,
                                       text = "", image = self.logout_icon, width = 40, height = 40,
                                       command = self.logout)
        self.logout_button.grid(row = 0, column = 2, sticky = "nse")
        
        self.setting_body_frame = CTkFrame(self.page_frame, fg_color = alphabet_blue)
        self.setting_body_frame.grid_columnconfigure((0, 1, 2), weight = 1)
        self.setting_body_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
        self.setting_body_frame.grid(row = 1, column = 0, sticky = "ew", padx = 400, pady = 200)
        
        self.instruction_label = CTkLabel(self.setting_body_frame, text = "Blank Entry will cause NO Change")
        self.instruction_label.grid(row = 0, column = 0, columnspan = 3)
        
        self.edit_password_label = CTkLabel(self.setting_body_frame, text = "New Password:",
                                            text_color = "black")
        self.edit_password_label.grid(row = 1, column = 0, sticky = "e", pady = 5)
        
        
        self.edit_password_entry = CTkEntry(self.setting_body_frame, fg_color = "white",
                                            show = "*", bg_color = alphabet_blue)
        self.edit_password_entry.grid(row = 1, column = 1, columnspan = 2, sticky = "ew", pady = 5)
        
        
        self.confirm_edit_password_label = CTkLabel(self.setting_body_frame, text = "Confirmn New Password:",
                                            text_color = "black")
        self.confirm_edit_password_label.grid(row = 2, column = 0, sticky = "e", pady = 5)
        
        
        self.confirm_edit_password_entry = CTkEntry(self.setting_body_frame, fg_color = "white",
                                            show = "*", bg_color = alphabet_blue)
        self.confirm_edit_password_entry.grid(row = 2, column = 1, columnspan = 2, sticky = "ew", pady = 5)
        
        self.error_message_label = CTkLabel(self.setting_body_frame, text = "", text_color = "red")
        self.error_message_label.grid(row = 3, column = 0, columnspan = 3, pady = 5)
        
        self.save_button = CTkButton(self.setting_body_frame, text = "Save", text_color = "black",
                                    fg_color ="white", bg_color = alphabet_blue,
                                    command = self.save)
        self.save_button.grid(row = 4, column = 0, columnspan = 3, pady = 20)
        
        self.clear_history_button = CTkButton(self.setting_body_frame, text = "Clear History", text_color = "black",
                                    fg_color ="white", bg_color = alphabet_blue,
                                    command = self.clear_history)
        self.clear_history_button.grid(row = 5, column = 0, columnspan = 3, pady = 20)
        
     
    def logout(self) :
        auth.logout(self.current_user, self.file_obj)
        self.go_to_login()   
        
    def save(self) :
            
        if len(self.edit_password_entry.get()) == 0 :
            self.error_message_label.configure(text = "")
            new_password = self.current_user.get_info().get("password")
        else :
            if self.edit_password_entry.get() == self.confirm_edit_password_entry.get() :
                self.error_message_label.configure(text = "")
                new_password = self.edit_password_entry.get()
            else :
                self.error_message_label.configure(text = "Error: Password and Confirm Password do not match")
    
        user_con.change_password(self.current_user, new_password, self.file_obj)
    
    def clear_history(self) :
        user_con.clear_history(self.current_user, self.file_obj)