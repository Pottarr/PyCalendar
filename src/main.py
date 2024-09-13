import tkinter as tk
import pages.login_page as login_page
# import pages.register_page as register_page
# import pages.home_page as home_page

class Application :
    def __init__(self) :
        self.root = tk.Tk()
        self.root.title("PyCalendar")
        self.root.geometry("800x600")
        self.root.grid_rowconfigure(0, weight = 1)
        self.root.grid_columnconfigure(0, weight = 1)
        login_page.LoginPage(self.root)
        
        
    def run(self) :

        self.root.mainloop()

if __name__ == "__main__" :
    app = Application()
    app.run()