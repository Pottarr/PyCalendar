from abc import ABC, abstractmethod
from datetime import date
from typing import Optional

class Activity(ABC) :
    def __init__(self, name: str, description: str, date_of_activity: date) :
        self.name = name
        self.description = description
        self.date_of_activity = date_of_activity
    
    @abstractmethod
    def is_repeatable(self) -> bool :
        pass
    
    @abstractmethod
    def edit_activity(self) :
        pass
    
    def delete_activity(self) :
        pass
    
    

class OneTimeActivity(Activity) :
    def __init__(self, name: str, description: str, date_of_activity: date) :
        super().__init__(name, description, date_of_activity)
    
    def is_repeatable(self) -> bool :
        return False

class RepeatableActivity(Activity) :
    def __init__(self, name: str, description: str, date_of_activity: date, recurrence_type: str, start_date: date, end_date: Optional[date] = None) :
        super().__init__(name, description, date_of_activity)
        self.recurrence_type = recurrence_type  # e.g., "daily", "weekly", "annually"
        self.start_date = start_date
        self.end_date = end_date  # None if there's no end date
    
    def is_repeatable(self) -> bool:
        return True

    def is_within_date_range(self, current_date: date) -> bool:
        if self.end_date:
            return self.start_date <= current_date <= self.end_date
        return current_date >= self.start_date
