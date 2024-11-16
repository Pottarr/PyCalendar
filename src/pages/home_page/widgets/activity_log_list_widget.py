from customtkinter import *

alphabet_blue = "#abcdef"

class ActivityLogListWidget(CTkScrollableFrame) :
    def __init__(self, master = None, current_user = None, current_date = None, **kwargs) :
        super().__init__(master, **kwargs)
        self.current_user = current_user
        self.current_date = current_date
        
        if len(current_user["activity_log"]) == 0 :
            self.no_activity_label = CTkLabel(self, text = "No Activity", font = ("Arial", 40))
            self.no_activity_label.pack(fill = "both", pady = 100)
        else :
            self.matched_activity = []
            