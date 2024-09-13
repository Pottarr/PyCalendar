import tkinter as tk
# from pages.login_page import login_page
# from services.auth_system import auth_system
# from services.auth_system import auth_system as auth
import services.auth_system as auth

alphabet_blue = "#abcdef"

class RegisterPage :
    def __init__(self, root) :
    
        # Page Frame 
        self.root = root
        self.page_frame = tk.Frame(self.root, bg = alphabet_blue)
        self.page_frame.grid(row = 0, column = 0, sticky = "nsew")
        self.page_frame.grid_columnconfigure(0, weight = 1)
        self.page_frame.grid_rowconfigure(0, weight = 1)
        self.page_frame.grid_rowconfigure(1, weight = 1)
        # self.page_frame.grid_rowconfigure(1, weight = 1)
        # self.page_frame.grid_rowconfigure(2, weight = 1)
        # self.page_frame.grid_rowconfigure(3, weight = 1)
        # self.page_frame.grid_rowconfigure(4, weight = 1)

        # Register Frame
        self.register_frame = tk.Frame(self.page_frame, bg = alphabet_blue)
        self.register_frame.grid_columnconfigure(0, weight = 1)
        self.register_frame.grid_rowconfigure(0, weight = 1)
        self.register_frame.grid_rowconfigure(1, weight = 1)
        self.register_frame.grid_rowconfigure(2, weight = 1)
        self.register_frame.grid_rowconfigure(3, weight = 1)
        self.register_frame.grid_rowconfigure(4, weight = 1)
        self.register_frame.grid_rowconfigure(5, weight = 1)
        self.register_frame.grid(row = 0, column = 0)

        self.label = tk.Label(self.register_frame, text="Register Page")
        self.label.grid(row = 0, column = 0)
        
        self.username_entry = tk.Entry(self.register_frame)
        self.username_entry.grid(row = 1, column = 0)
        
        self.password_entry = tk.Entry(self.register_frame)
        self.password_entry.grid(row = 2, column = 0)
        
        self.confirm_password_entry = tk.Entry(self.register_frame)
        self.confirm_password_entry.grid(row = 3, column = 0)
        
        self.login_button = tk.Button(self.register_frame, text="Register", command=self.register)
        self.login_button.grid(row = 4, column = 0)
        
        self.go_to_login_button = tk.Button(self.page_frame, text = "Go to Login", command = self.go_to_login)
        self.go_to_login_button.grid(row = 1, column = 0)
        
        # self.error_message = tk.Label(self.register_frame, text = register_error, bg = alphabet_blue, fg = "#ff0000")
        # self.error_message.pack()
    def register(self) :

        # self.page_frame.destroy()
        # self.register_frame(self.page_frame)        
    
        username_value = self.username_entry.get()
        password_value = self.password_entry.get()
        confirm_password_value = self.confirm_password_entry.get()
        
        
        new_user = auth.register(username_value, password_value, confirm_password_value)
        can_register = list(new_user)[0]
        
        
        if can_register == True :
            new_user_data = list(new_user)[1]
            import pages.login_page as login_page
            self.page_frame.destroy()
            login_page.LoginPage(self.root)
        else :
            register_error = list(new_user)[1]
            # if err_count > 1 :
                # self.error_message.destroy()
                
            self.error_message = tk.Label(self.register_frame, text = register_error, bg = alphabet_blue, fg = "#ff0000")
            self.error_message.grid(row = 5, column = 0)
            # err_count += 1
            
            # return err_count
            
    def go_to_login(self) :
        import pages.login_page as login_page
        self.page_frame.destroy()
        login_page.LoginPage(self.root)