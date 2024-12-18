import pickle

def write_file(file_path, data) :
    with open(file_path, "wb") as f :
        print("File Opened: Write")
        pickle.dump(data, f)
        
def read_file(file_path) :
    with open(file_path, "rb") as f :
        print("File Opened: Read")
        data = pickle.load(f)
        return (data, f)
    
def close_file(file_obj) :
    file_obj.close()
    print("File Closed...")