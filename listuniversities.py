import csv
from loading_json import load_json_file  

def list_states(data):
    states = sorted({record['university']['state'] for record in data})
    
    print("Available states:")
    for state in states:
        print(state)
    
    
    state_name = input("Enter the state name from the list above: ")
    return state_name

def list_and_save_universities_by_state(data):
    state_name = list_states(data)

    universities = [record['university']['name'] for record in data if record['university']['state'] == state_name]

    if universities:
        print(f"Universities in {state_name}:")
        for university in universities:
            print(university)

        # Save the universities to a CSV file
        csv_filename = f"universities_in_{state_name}.csv"
        with open(csv_filename, 'w', newline='') as csvfile:
            fieldnames = ['university_name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for university in universities:
                writer.writerow({'university_name': university})

        print(f"List of universities saved to {csv_filename}")
    else:
        print(f"No universities found in {state_name}.")

data = load_json_file('nainika_adoptions.json')

if data:
    list_and_save_universities_by_state(data)
