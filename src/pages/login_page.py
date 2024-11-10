from customtkinter import *
import services.auth_system as auth
from pages.page import Page

alphabet_blue = "#abcdef"
trueman_green = "#aae5a4"

        
class LoginPage(Page) :
    """This class generates the Login Page"""
    def __init__(self, root) :
        
        
        # Page Frame
        self.root = root
        self.page_frame = CTkFrame(self.root, fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.page_frame.grid_columnconfigure(0, weight = 1)
        self.page_frame.grid_rowconfigure(tuple([i for i in range(6)]), weight = 1)
        self.page_frame.grid(row = 0, column = 0, sticky = "nsew")

        self.title_label = CTkLabel(self.page_frame, text = "PyCalendar", font = ("Arial", 40), bg_color = alphabet_blue)
        self.title_label.grid(row = 0, column = 0, sticky = "s")
        
        # Login Frame
        self.login_frame = CTkFrame(self.page_frame, fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.login_frame.grid_columnconfigure(0, weight = 1)
        self.login_frame.grid_rowconfigure((0, 1), weight = 1)
        self.login_frame.grid(row = 2, column = 0, sticky = "nsew")

        
        self.login_label = CTkLabel(self.login_frame, text = "Login", font = ("Arial", 20), fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.login_label.grid(row = 0, column = 0, sticky = "s")
        
        self.entry_frame = CTkFrame(self.login_frame, fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.entry_frame.grid_columnconfigure(0, weight = 1)
        self.entry_frame.grid_columnconfigure(1, weight = 3)
        self.entry_frame.grid_rowconfigure((0, 1, 2, 3), weight = 1)
        self.entry_frame.grid(row = 1, column = 0, sticky = "n")

        self.username_label = CTkLabel(self.entry_frame, text = "Username: ", bg_color = alphabet_blue)
        self.username_label.grid(row = 0, column = 0)

        self.username_entry = CTkEntry(self.entry_frame, bg_color = alphabet_blue)
        self.username_entry.grid(row = 0, column = 1)
        
        self.password_label = CTkLabel(self.entry_frame, text = "Password: ", bg_color = alphabet_blue)
        self.password_label.grid(row = 1, column = 0)
        
        self.password_entry = CTkEntry(self.entry_frame, show = "*", bg_color = alphabet_blue)
        self.password_entry.grid(row = 1, column = 1)
        
        self.login_button = CTkButton(self.entry_frame, text = "Login", text_color = "black", fg_color = "white", bg_color = alphabet_blue, command = self.login)
        self.login_button.grid(row = 2, column = 0, columnspan = 2)
        
        self.login_error = ""
        self.error_message = CTkLabel(self.entry_frame, text = self.login_error, text_color = "red", fg_color = alphabet_blue, bg_color = alphabet_blue)
        self.error_message.grid(row = 3, column = 0, columnspan = 2, sticky = "n")
        
        #Go to Register Button 
        self.go_to_register_button = CTkButton(self.page_frame, text = "Go to Register", text_color = "black", fg_color = "white", bg_color = alphabet_blue, command = self.go_to_register)
        self.go_to_register_button.grid(row = 3, column = 0, sticky = "n")
        
    def login(self) :
        """This method executes when the login_button is pressed. It takes 2 values 
        from username_entry and password_entry from the LoginPage class and checks 
        whether the user is suitable for login or not. If suitable, the method 
        destroys the LoginPage and generates the HomePage, else, the method 
        throws back error for the error_message to generate."""
        username_value = self.username_entry.get()
        password_value = self.password_entry.get()
        
        can_login, login_result = auth.login(username_value, password_value)
        
        if can_login == True :
            
            import pages.home_page as home_page
            self.login_error = ""
            self.go_to_home(login_result)
            
        elif can_login == False :
            self.login_error = login_result
            self.error_message.configure(text = self.login_error)