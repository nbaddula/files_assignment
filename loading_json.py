import json

def load_json_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        print("File loaded successfully.")
        return data
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON file.")

# Load and review the data
data = load_json_file('nainika_adoptions.json')
print(data[0]) 
