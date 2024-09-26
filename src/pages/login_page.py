from tkinter import *
import services.auth_system as auth

alphabet_blue = "#abcdef"
trueman_green = "#aae5a4"

        
class LoginPage :
    def __init__(self, root) :
        
        
        # Page Frame
        self.root = root
        self.page_frame = Frame(self.root, bg = alphabet_blue)
        self.page_frame.grid_columnconfigure(0, weight = 1)
        self.page_frame.grid_rowconfigure(tuple([i for i in range(6)]), weight = 1)
        self.page_frame.grid(row = 0, column = 0, sticky = "nsew")

        self.title_label = Label(self.page_frame, text = "PyCalendar", font = ("Arial", 40), bg = alphabet_blue)
        self.title_label.grid(row = 0, column = 0, sticky = "s")
        
        # Login Frame
        self.login_frame = Frame(self.page_frame, bg = alphabet_blue)
        self.login_frame.grid_columnconfigure(0, weight = 1)
        self.login_frame.grid_rowconfigure((0, 1), weight = 1)
        self.login_frame.grid(row = 2, column = 0, sticky = "nsew")

        
        self.login_label = Label(self.login_frame, text = "Login", font = ("Arial", 20),  bg = alphabet_blue)
        self.login_label.grid(row = 0, column = 0, sticky = "s")
        
        self.entry_frame = Frame(self.login_frame, bg = alphabet_blue)
        self.entry_frame.grid_columnconfigure(0, weight = 1)
        self.entry_frame.grid_columnconfigure(1, weight = 3)
        self.entry_frame.grid_rowconfigure((0, 1, 2, 3), weight = 1)
        self.entry_frame.grid(row = 1, column = 0, sticky = "n")

        self.username_label = Label(self.entry_frame, text = "Username: ", bg = alphabet_blue)
        self.username_label.grid(row = 0, column = 0)

        self.username_entry = Entry(self.entry_frame)
        self.username_entry.grid(row = 0, column = 1)
        
        self.password_label = Label(self.entry_frame, text = "Password: ", bg = alphabet_blue)
        self.password_label.grid(row = 1, column = 0)
        
        self.password_entry = Entry(self.entry_frame, show = "*")
        self.password_entry.grid(row = 1, column = 1)
        
        self.login_button = Button(self.entry_frame, text = "Login", command = self.login)
        self.login_button.grid(row = 2, column = 0, columnspan = 2)
        
        self.login_error = ""
        self.error_message = Label(self.entry_frame, text = self.login_error, bg = alphabet_blue, fg = "#ff0000")
        self.error_message.grid(row = 3, column = 0, columnspan = 2, sticky = "n")
        
        #Go to Register Button 
        self.go_to_register_button = Button(self.page_frame, text = "Go to Register", command = self.go_to_register)
        self.go_to_register_button.grid(row = 3, column = 0, sticky = "n")
        
    def login(self) :
        username_value = self.username_entry.get()
        password_value = self.password_entry.get()
        
        current_user = auth.login(username_value, password_value)
        can_login = list(current_user)[0]
        current_user_data = list(current_user)[1]
        
        if can_login == True :
            import pages.home_page as home_page
            self.login_error = ""
            self.page_frame.destroy()
            home_page.HomePage(self.root)
        elif can_login == False :
            self.login_error = list(current_user)[1]
            self.error_message["text"] = self.login_error
            
    def go_to_register(self) :
            import pages.register_page as register_page
            self.page_frame.destroy()
            register_page.RegisterPage(self.root)