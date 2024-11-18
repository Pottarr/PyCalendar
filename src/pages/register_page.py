from pages.page import Page
from customtkinter import *
import services.auth_system as auth

alphabet_blue = "#abcdef"
python_yellow = "#ffe873"
python_blue = "#306998"
python_blue_lighter = "#7bafe3"
very_light_gray = "#d3d3d3"

class RegisterPage(Page) :
    """This class generates the Register Page."""
    def __init__(self, root) :
    
        # Page Frame 
        self.root = root
        self.page_frame = CTkFrame(self.root, fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.page_frame.grid_columnconfigure(0, weight = 1)
        self.page_frame.grid_rowconfigure(tuple([i for i in range(5)]), weight = 1)
        self.page_frame.pack(fill = "both", expand = True)

        # Register Frame
        self.register_frame = CTkFrame(self.page_frame, fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.register_frame.grid_columnconfigure(0, weight = 1)
        self.register_frame.grid_rowconfigure(0, weight = 1)
        self.register_frame.grid_rowconfigure(1, weight = 1)
        self.register_frame.grid(row = 2, column = 0)

        self.register_label = CTkLabel(self.register_frame, text="Register", font = ("Arial", 20),
                                       bg_color = alphabet_blue)
        self.register_label.grid(row = 0, column = 0, sticky = "s")
    
        self.entry_frame = CTkFrame(self.register_frame, fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.entry_frame.grid_columnconfigure(0, weight = 1)
        self.entry_frame.grid_columnconfigure(1, weight = 3)
        self.entry_frame.grid_rowconfigure((0, 1, 2, 3), weight = 1)
        self.entry_frame.grid(row = 1, column = 0, sticky = "n")
        
        self.username_label = CTkLabel(self.entry_frame, text = "Username: ", bg_color = alphabet_blue)
        self.username_label.grid(row = 0, column = 0)
    
        self.username_entry = CTkEntry(self.entry_frame, bg_color = alphabet_blue)
        self.username_entry.grid(row = 0, column = 1)
        
        self.password_label = CTkLabel(self.entry_frame, text = "Password: : ", bg_color = alphabet_blue)
        self.password_label.grid(row = 1, column = 0)
        
        self.password_entry = CTkEntry(self.entry_frame, show = "*", bg_color = alphabet_blue)
        self.password_entry.grid(row = 1, column = 1)
        
        self.confirm_password_label = CTkLabel(self.entry_frame, text = "Confirm Password: ",
                                               fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.confirm_password_label.grid(row = 2, column = 0)
        
        self.confirm_password_entry = CTkEntry(self.entry_frame, show = "*", bg_color = alphabet_blue)
        self.confirm_password_entry.grid(row = 2, column = 1)
        
        self.register_button = CTkButton(self.entry_frame, text="Register", text_color = "black",
                                         fg_color = "white", bg_color = alphabet_blue, command=self.register)
        self.register_button.grid(row = 4, column = 0, columnspan = 2)
        
        self.register_error = ""
        self.error_message = CTkLabel(self.entry_frame, text = self.register_error, text_color = "red",
                                      fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.error_message.grid(row = 5, column = 0, columnspan = 2, sticky = "n")
        
        self.go_to_login_button = CTkButton(self.page_frame, text = "Go to Login", text_color = "black",
                                            fg_color ="white", bg_color = alphabet_blue, command = self.go_to_login)
        self.go_to_login_button.grid(row = 3, column = 0, sticky = "n")
        
    def register(self) :
        username_value = self.username_entry.get()
        password_value = self.password_entry.get()
        confirm_password_value = self.confirm_password_entry.get()
        
        
        new_user = auth.register(username_value, password_value, confirm_password_value)
        can_register = list(new_user)[0]
        
        
        if can_register == True :
            new_user_data = list(new_user)[1]
            self.register_error = ""    
            self.go_to_login()
            
        else :
            self.register_error = list(new_user)[1]
            self.error_message.configure(text = self.register_error)