import json
from tracker import get_file_path
from pathlib import Path

def get_data():
    current_dir = Path.cwd()
    data_dir = Path(current_dir/'tracking_data')
    if data_dir.exists():
        file_path= get_file_path()
        if file_path.exists():
            with open(file_path,'r') as data_file:
                try:
                    data = json.load(data_file)
                except json.JSONDecodeError:
                    return {}
            sorted_data = dict(sorted(data.items(),key=lambda x:x[1],reverse=True))
            return sorted_data
        else: 
            raise FileNotFoundError("Data does not exist.") 
    else:
        raise Exception("Something went wrong try again later.")

def get_top_five():
    data_loaded = get_data()
    return list(data_loaded.items())[:5]

def get_todays_data():
    data_loaded= get_data()
    return list(data_loaded.items())

def get_usage_on(some_date):
    file_path = get_file_path(some_date)
    if file_path.exists():
        with open(file_path,'r') as data_file:
            data_loaded= json.load(data_file)
        sorted_data = dict(sorted(data_loaded.items(),key=lambda x:x[1],reverse=True))
        return list(sorted_data.items())
    else: 
        raise FileNotFoundError("Data does not exist.")

if __name__=="__main__":
    print("Todays usage:")
    for app, sec in get_todays_data():
        print(f"{app}, {sec}s")