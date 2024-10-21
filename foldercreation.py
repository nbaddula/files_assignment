import json
import os


def prompt_for_folder_and_load_json():
    folder_name = input("Enter the folder name where the JSON file is located: ")
    file_name = 'nainika_adoptions.json'
    file_path = os.path.join(folder_name, file_name)
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        print(f"File loaded successfully from {folder_name}")
        return data
    except FileNotFoundError:
        print("File not found in the specified folder.")
    except json.JSONDecodeError:
        print("Error decoding JSON file.")