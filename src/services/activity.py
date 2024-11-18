from datetime import date
from typing import Optional

class Activity :
    def __init__(self, activity_dict) :
        self.id = activity_dict.get("id")
        self.name = activity_dict.get("name")
        self.description = activity_dict.get("description")
        self.date_of_activity = activity_dict.get("date_of_activity")
        self.day_of_week = activity_dict.get("day_of_week")

class NormalActivity(Activity) :
    def __init__(self, activity_dict) :
        super().__init__(activity_dict)
        
    

class RepeatableActivity(Activity) :
    def __init__(self, activity_dict) :
        super().__init__(activity_dict)
        self.activity_type = activity_dict.get("activity_type")  # "Daily", "Weekly", "Annually"