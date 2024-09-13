import tkinter as tk
# import pages.home_page as home_page
# import pages.register_page as register_page
import services.auth_system as auth

alphabet_blue = "#abcdef"
        
class LoginPage :
    def __init__(self, root) :
        
        
        # Page Frame
        self.root = root
        self.page_frame = tk.Frame(self.root, bg = alphabet_blue)
        self.page_frame.grid(row = 0, column = 0, sticky = "nsew")
        self.page_frame.grid_columnconfigure(0, weight = 1)
        self.page_frame.grid_rowconfigure(0, weight = 1)
        self.page_frame.grid_rowconfigure(1, weight = 1)
        # self.page_frame.grid_rowconfigure(2, weight = 1)
        # self.page_frame.grid_rowconfigure(3, weight = 1)
        # self.page_frame.grid_rowconfigure(4, weight = 1)

        # Login Frame
        self.login_frame = tk.Frame(self.page_frame, bg = alphabet_blue)
        self.page_frame.grid_rowconfigure(0, weight = 1)
        self.page_frame.grid_rowconfigure(1, weight = 1)
        self.page_frame.grid_rowconfigure(2, weight = 1)
        self.page_frame.grid_rowconfigure(3, weight = 1)
        self.page_frame.grid_rowconfigure(4, weight = 1)
        self.login_frame.grid(row = 0, column = 0)

        self.login_label = tk.Label(self.login_frame, text = "Login Page", bg = alphabet_blue)
        self.login_label.grid(row = 1, column = 0)

        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row = 2, column = 0)
        
        self.password_entry = tk.Entry(self.login_frame)
        self.password_entry.grid(row = 3, column = 0)
        
        self.login_button = tk.Button(self.login_frame, text = "Login", command = self.login)
        self.login_button.grid(row = 4, column = 0)

        #Go to Register Button 
        self.go_to_register_button = tk.Button(self.page_frame, text = "Go to Register", command = self.go_to_register)
        self.go_to_register_button.grid(row = 1, column = 0)
        
        
        
    def login(self) :
        username_value = self.username_entry.get()
        password_value = self.password_entry.get()
        
        current_user = auth.login(username_value, password_value)
        can_login = list(current_user)[0]
        current_user_data = list(current_user)[1]
        
        if can_login == True :
            import pages.home_page as home_page
            self.page_frame.destroy()
            home_page.HomePage(self.root)
        else :
            login_error = list(current_user)[1]
            # if err_count > 1 :
                # self.error_message.destroy()
                
            self.error_message = tk.Label(self.login_frame, text = login_error, bg = alphabet_blue, fg = "#ff0000")
            self.error_message.grid(row = 5, column = 0)
            print(login_error)
            
    def go_to_register(self) :
            import pages.register_page as register_page
            self.page_frame.destroy()
            register_page.RegisterPage(self.root)