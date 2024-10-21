import csv
from loading_json import load_json_file  # Import the load_json_file function

# Function to save messages to CSV
def save_messages_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['adoption_id', 'message_id', 'date', 'category', 'content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for record in data:
            for message in record['messages']:
                writer.writerow({
                    'adoption_id': record['id'],
                    'message_id': message['id'],
                    'date': message['date'],
                    'category': message['category'],
                    'content': message['content']
                })

data = load_json_file('nainika_adoptions.json')

# Save messages to CSV
if data:
    save_messages_to_csv(data, 'messages.csv')
