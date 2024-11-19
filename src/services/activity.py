from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional

class Activity(ABC) :
    def __init__(self, activity_dict) :
        self.id = activity_dict.get("id")
        self.name = activity_dict.get("name")
        self.description = activity_dict.get("description")
        self.date_of_activity = activity_dict.get("date_of_activity")
        self.day_of_week = activity_dict.get("day_of_week")

    @abstractmethod
    def debug_print(self) :
        pass

class NormalActivity(Activity) :
    def __init__(self, activity_dict) :
        super().__init__(activity_dict)
        
    def debug_print(self) :
        print(f"===================== Debug =====================")
        print(f"Title: {self.name}")
        print(f"Type: Normal")
        print(f"Date of activity: {self.day_of_week} {self.date_of_activity}")
        print(f"Description: {self.description}")
        print(f"=================================================")
        
    

class RepeatableActivity(Activity) :
    def __init__(self, activity_dict) :
        super().__init__(activity_dict)
        self.activity_type = activity_dict.get("activity_type")  # "Daily", "Weekly", "Annually"
        
    def debug_print(self) :
        reccurence = ""
        if self.activity_type == "Daily" :
            reccurence = "Every day"
        elif self.activity_type == "Weekly" :
            reccurence == f"Every {self.day_of_week}"
        elif self.activity_type == "Annually" :
            reccurence = f"Every {datetime.strptime(self.date_of_activity, "%d/%m/%Y").strftime("%d/%m")}"
        print(f"===================== Debug =====================")
        print(f"Title: {self.name}")
        print(f"Type: {self.activity_type}")
        print(f"Reccurence: {reccurence}")
        print(f"Description: {self.description}")
        print(f"=================================================")