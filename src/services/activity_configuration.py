import os
import uuid
import services.pickle_system as pkl
import services.activity as act
import services.user as user

def create_activity(current_user, name, description, date_of_activity, day_of_week, activity_type, file_obj) :
    new_activity_dict = {}
    new_activity_dict["id"] = uuid.uuid4()
    new_activity_dict["name"] = name
    new_activity_dict["description"] = description
    new_activity_dict["date_of_activity"] = date_of_activity
    new_activity_dict["day_of_week"] = day_of_week

    if activity_type == "Normal" :
        activity_obj = act.NormalActivity(new_activity_dict)
    else :
        new_activity_dict["activity_type"] = activity_type
        activity_obj = act.RepeatableActivity(new_activity_dict)

    current_user.add_activity(activity_obj)
    
    file_name = f"{current_user.get_info().get("username")}.pickle"
    relative_path = "db/"
    file_path = os.path.join(relative_path, file_name)
    
    pkl.close_file(file_obj)
    pkl.write_file(file_path, current_user)
    pkl.close_file(file_obj)
    pkl.read_file(file_path)
    
    
        

def edit_activity() :
    pass

def delete_activity() :
    pass