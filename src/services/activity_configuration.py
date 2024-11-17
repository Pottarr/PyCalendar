import os
import services.pickle_system as pkl
import services.user as user

def create_activity(current_user, name, description, date_of_activity, day_of_week, is_repeatable, activity_type, file_obj) :
    new_activity_dict = {}
    new_activity_dict["name"] = name
    new_activity_dict["description"] = description
    new_activity_dict["date_of_activity"] = date_of_activity
    new_activity_dict["day_of_week"] = day_of_week
    new_activity_dict["activity_type"] = activity_type

    current_user["activity_log"].append(new_activity_dict)
    print()
    print()
    print("Current user:")
    print(current_user)
    print()
    print()
    
    current_user_obj = user.User(current_user)

    file_name = f"{current_user.get("username")}.pickle"
    relative_path = "db/"
    file_path = os.path.join(relative_path, file_name)
    
    pkl.close_file(file_obj)
    pkl.write_file(file_path, current_user_obj)
    pkl.close_file(file_obj)
    pkl.read_file(file_path)
    
    
        

def edit_activity() :
    pass

def delete_activity() :
    pass