from abc import ABC

class Page(ABC) :
    def __init__(self) :
        pass
    
    def go_to_register(self) :
        """This method destroys the current page and generates the RegisterPage."""
        import pages.register_page as register_page
        self.page_frame.destroy()
        register_page.RegisterPage(self.root)
    
    def go_to_login(self) :
        """This method destroys the current page and generates the LoginPage."""
        import pages.login_page as login_page
        self.page_frame.destroy()
        login_page.LoginPage(self.root)
    
    def go_to_home(self, login_result) :
        """This method destroys the current page and generates the HomePage."""
        import pages.home_page as home_page
        self.page_frame.destroy()
        home_page.HomePage(self.root, login_result)
    
    def go_to_settings(self) :
        """This method destroys the current page and generates the SettingsPage."""
        import pages.settings_page as settings_page
        self.page_frame.destroy()
        settings_page.SettingsPage(self.root)
    