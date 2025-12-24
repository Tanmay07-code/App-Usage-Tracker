import time
import win32gui as wg
import json
from pathlib import Path
from datetime import date

last_app = None
last_time = time.time()
todays_date = date.today()

def get_file_path(day=None):
    current_dir = Path.cwd()
    data_dir = Path(current_dir/'tracking_data')
    Path.mkdir(data_dir,exist_ok=True)
    if day is None:
        day=todays_date
    data_filepath = Path(data_dir/f'usage_{day}.json')
    return data_filepath
    
def load_data(data_filepath):  
    if data_filepath.exists():
        with open(data_filepath,'r') as file:
            data = json.load(file)
        return data
    else:
        return {}

def get_active_window():
    handle = wg.GetForegroundWindow()
    title_text_list = wg.GetWindowText(handle).split('-')

    if len(title_text_list)>1:
        return f'{title_text_list[-1]} - {title_text_list[-2]}'
    elif len(title_text_list) == 1 and title_text_list != "":
        return f'{(title_text_list[0])}'
    else:
        return "Not Known"
    
def update_data(current_app,current_time,data_dict):
    global last_app,last_time

    if last_app == None:
        last_app = current_app
        last_time = current_time
        return data_dict

    elapsed_time = current_time - last_time
    data_dict[last_app] = data_dict.get(last_app,0)+elapsed_time
    last_time = current_time
    last_app = current_app
    return data_dict

def save_data(data_dict):
    data_filepath = get_file_path()
    with open(data_filepath,'w') as file:
        json.dump(data_dict,file,indent=4)

def start_tracker():
    starting_time = time.time()
    data_dict = load_data(get_file_path())
    try:
        while True:
            global last_app,todays_date,last_time
            current_time = time.time()
            app_name = get_active_window()
            data = update_data(app_name,current_time,data_dict)

            if (current_time - starting_time) >= 60:
                save_data(data)
                starting_time = current_time
                print("success")
            
            if todays_date != date.today():
                save_data(data)
                todays_date = date.today()
                data_dict = {}
                last_app = None
                last_time = current_time
            
            time.sleep(1)

    except KeyboardInterrupt:
        save_data(data_dict)
        print("\nTracking stopped — data saved safely.")
    
    except :
        print("Something went wrong. Make sure you have a Windows OS.")

        

if __name__=="__main__":
    start_tracker()

