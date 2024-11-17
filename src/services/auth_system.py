import os
from typing import Tuple, Union, BinaryIO
import services.pickle_system as pkl
import services.user as user


def register(username:str , password: str, confirm_password: str) -> Tuple[bool, Union[user.User, str]]:
    if username == "" :
        return (False, "Error: Username is invalid.")
    else :
        file_name = username + ".pickle"
        relative_path = "db/"
        file_path = os.path.join(relative_path, file_name)
        if os.path.exists(file_path) == True :
            return (False, "Error: Username already exists.")
        else :
            if password == confirm_password :
                initial_user_data = {"username": username, "password": password, "activity_log": []}
                #Include later: "activity_log": [], "daily_activity": [], "weekly_activity": [], "monthly_activity": [], "yearly_activity": [], "event": []
                creating_user = user.User(initial_user_data)
                # creating_user.debug_print()
                pkl.write_file(file_path, creating_user)
                return (True, creating_user)
            else :
                return (False, "Error: Please check your password.")
        
def login(username: str, password: str) -> Tuple[bool, Union[Tuple[user.User, BinaryIO]]] :
    
    file_name = f"{username}.pickle"
    relative_path = "db/"
    file_path = os.path.join(relative_path, file_name)
    try :
        data, file_obj = pkl.read_file(file_path)
    except FileNotFoundError :
        return (False, "Error: Username not found.")
    correct_password = data.get("password")
    if correct_password == password :
        login_user_data = {"username": data.get("username"), "password": data.get("password"),
                           "activity_log": data.get("activity_log")}
        current_user = user.User(login_user_data)
        return (True, (current_user, file_obj))
    elif correct_password != password :
        return (False, "Error: Password is incorrect")
    
def logout(current_user: user.User, file_obj: BinaryIO) :
    try :
        pkl.close_file(file_obj)
    except Exception as e :
        print(f"Error: {e}")
    