import os
import services.user as user
import services.pickle_system as pkl

def change_password(current_user, new_password, file_obj) :
    
    file_name = f"{current_user.get_info().get("username")}.pickle"
    relative_path = "db/"
    file_path = os.path.join(relative_path, file_name)
    
    current_user.change_password(new_password)
    
    pkl.close_file(file_obj)
    pkl.write_file(file_path, current_user)
    pkl.close_file(file_obj)
    pkl.read_file(file_path)
    
def clear_history(current_user, file_obj) :
    
    file_name = f"{current_user.get_info().get("username")}.pickle"
    relative_path = "db/"
    file_path = os.path.join(relative_path, file_name)
    
    current_user.clear_history()
    
    pkl.close_file(file_obj)
    pkl.write_file(file_path, current_user)
    pkl.close_file(file_obj)
    pkl.read_file(file_path)