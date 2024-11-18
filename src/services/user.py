class User :
    def __init__(self, user_dict) :
        self.__username = user_dict.get("username")
        self.__password = user_dict.get("password")
        self.__activity_log = user_dict.get("activity_log")
        
    def get_info(self) :
        return {"username": self.__username, "password": self.__password, "activity_log": self.__activity_log}
    
    def edit_user(self, new_username, new_password) :
        self.__username = new_username
        self.__password = new_password
        
    def add_activity(self, activity_obj) :
        self.__activity_log.append(activity_obj)
    
    def delete_activity(self, activity) :
        self.__activity_log.remove(activity)
    
    def change_password(self, new_password) :
        self.__password = new_password
        
    def clear_history(self) :
        self.__activity_log.clear()