from tkinter import *
import services.auth_system as auth

alphabet_blue = "#abcdef"
trueman_green = "#aae5a4"

class RegisterPage :
    def __init__(self, root) :
    
        # Page Frame 
        self.root = root
        self.page_frame = Frame(self.root, bg = alphabet_blue)
        self.page_frame.grid_columnconfigure(0, weight = 1)
        self.page_frame.grid_rowconfigure(tuple([i for i in range(5)]), weight = 1)
        self.page_frame.grid(row = 0, column = 0, sticky = "nsew")

        # Register Frame
        self.register_frame = Frame(self.page_frame, bg = alphabet_blue)
        self.register_frame.grid_columnconfigure(0, weight = 1)
        self.register_frame.grid_rowconfigure(0, weight = 1)
        self.register_frame.grid_rowconfigure(1, weight = 1)
        self.register_frame.grid(row = 2, column = 0)

        self.register_label = Label(self.register_frame, text="Register", font = ("Arial", 20), bg = alphabet_blue)
        self.register_label.grid(row = 0, column = 0, sticky = "s")
    
        self.entry_frame = Frame(self.register_frame, bg = alphabet_blue)
        self.entry_frame.grid_columnconfigure(0, weight = 1)
        self.entry_frame.grid_columnconfigure(1, weight = 3)
        self.entry_frame.grid_rowconfigure((0, 1, 2, 3), weight = 1)
        self.entry_frame.grid(row = 1, column = 0, sticky = "n")
        
        self.username_label = Label(self.entry_frame, text = "Username: ", bg = alphabet_blue)
        self.username_label.grid(row = 0, column = 0)
    
        self.username_entry = Entry(self.entry_frame)
        self.username_entry.grid(row = 0, column = 1)
        
        self.password_label = Label(self.entry_frame, text = "Password: : ", bg = alphabet_blue)
        self.password_label.grid(row = 1, column = 0)
        
        self.password_entry = Entry(self.entry_frame, show = "*")
        self.password_entry.grid(row = 1, column = 1)
        
        self.confirm_password_label = Label(self.entry_frame, text = "Confirm Password: ", bg = alphabet_blue)
        self.confirm_password_label.grid(row = 2, column = 0)
        
        self.confirm_password_entry = Entry(self.entry_frame, show = "*")
        self.confirm_password_entry.grid(row = 2, column = 1)
        
        self.register_button = Button(self.entry_frame, text="Register", command=self.register)
        self.register_button.grid(row = 4, column = 0, columnspan = 2)
        
        self.register_error = ""
        self.error_message = Label(self.entry_frame, text = self.register_error, bg = alphabet_blue, fg = "#ff0000")
        self.error_message.grid(row = 5, column = 0, columnspan = 2, sticky = "n")
        
        self.go_to_login_button = Button(self.page_frame, text = "Go to Login", command = self.go_to_login)
        self.go_to_login_button.grid(row = 3, column = 0, sticky = "n")
        
    def register(self) :
    
        username_value = self.username_entry.get()
        password_value = self.password_entry.get()
        confirm_password_value = self.confirm_password_entry.get()
        
        
        new_user = auth.register(username_value, password_value, confirm_password_value)
        can_register = list(new_user)[0]
        
        
        if can_register == True :
            new_user_data = list(new_user)[1]
            import pages.login_page as login_page
            self.register_error = ""
            self.page_frame.destroy()
            login_page.LoginPage(self.root)
        else :
            self.register_error = list(new_user)[1]

            self.error_message["text"] = self.register_error

            
    def go_to_login(self) :
        import pages.login_page as login_page
        self.page_frame.destroy()
        login_page.LoginPage(self.root)