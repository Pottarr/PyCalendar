import pickle

def write_file(file_path, data) :
    with open(file_path, "wb") as f :
        pickle.dump(data, f)
        
def read_file(file_path) :
    # print("FIle Path inside pickle read")
    # print(file_path)
    with open(file_path, "rb") as f :
        data = pickle.load(f)
        # print(data)
        # print(type(data))
        return (data, f)
    
def close_file(file_obj) :
    file_obj.close()
    print("File Closed...")