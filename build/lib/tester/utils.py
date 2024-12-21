from os import path

def get_curr_dir(file_obj: str):
    return path.dirname(file_obj)    

def add_path(path1: str, *args: str):
    result: str = path1
    for arg in args:
        result = path.join(result, arg)
    return result
