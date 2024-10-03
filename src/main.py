from customtkinter import *
import pages.login_page as login_page
# import pages.register_page as register_page
# import pages.home_page as home_page

class Application:
    """This class is the main class for the application."""
    def __init__(self):
        set_appearance_mode("light")
        # set_default_color_theme("blue")
        self.root = CTk()
        self.root.title("PyCalendar")
        self.root.geometry("1280x720")
        self.root.grid_rowconfigure(0, weight = 1)
        self.root.grid_columnconfigure(0, weight = 1)
        login_page.LoginPage(self.root)

    def run(self):
        """This method runs and starts up GUI application."""
        self.root.mainloop()


if __name__ == "__main__":
    app = Application()
    app.run()

