from abc import ABC, abstractmethod
from datetime import date
from typing import Optional

# We have Activity class to make it easier to edit the activity_dict
class Activity(ABC) :
    def __init__(self, name: str, description: str, date_of_activity: str, day_of_week: str) :
        self.name = name
        self.description = description
        self.date_of_activity = date_of_activity
        self.day_of_week = day_of_week
    
    # @abstractmethod
    # def is_repeatable(self) -> bool :
    #     pass
    
    @abstractmethod
    def edit_activity(self) :
        pass
    
    

class OneTimeActivity(Activity) :
    def __init__(self, name: str, description: str, date_of_activity: str) :
        super().__init__(name, description, date_of_activity)
        self.is_repeatable = False
        
    # def is_repeatable(self) -> bool :
    #     return False

class RepeatableActivity(Activity) :
    def __init__(self, name: str, description: str, date_of_activity: str, recurrence_type: str,
                 start_date: date, end_date: Optional[date] = None) :
        super().__init__(name, description, date_of_activity)
        self.recurrence_type = recurrence_type  # e.g., "daily", "weekly", "monthly", "annually"
        self.is_repeatable = True
        # self.start_date = start_date
        # self.end_date = end_date  # None if there's no end date
    
    # def is_repeatable(self) -> bool:
    #     return True

    # def is_within_date_range(self, current_date: date) -> bool:
    #     if self.end_date:
    #         return self.start_date <= current_date <= self.end_date
    #     return current_date >= self.start_date