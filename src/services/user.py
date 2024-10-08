class User :
    def __init__(self, user_dict) :
        self.__username = user_dict.get("username")
        self.__password = user_dict.get("password")
        self.__activity_log = user_dict.get("activity_log")
        
    def get_info(self) :
        return {"username": self.__username, "password": self.__password, "activity_log": self.__activity_log}
        
    # def add_activity(self) :
    #     pass 
    
    # def edit_activitty(self) :
    #     pass
    
    # def delete_activity(self) :
    #     pass
    
    def change_username(self, new_username) :
        self.__username = new_username
    
    def change_password(self, new_password) :
        self.__password = new_password
    
    def debug_print(self) :
        print(self.__username)
        print(self.__password)
    