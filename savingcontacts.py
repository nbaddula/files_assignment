import csv
from loading_json import load_json_file  # Import the load_json_file function

# Function to save contacts to CSV
def save_contacts_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['adoption_id', 'contact_order', 'firstname', 'lastname', 'gender']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for record in data:
            for contact in record['contacts']:
                writer.writerow({
                    'adoption_id': record['id'],
                    'contact_order': contact['order'],
                    'firstname': contact['firstname'],
                    'lastname': contact['lastname'],
                    'gender': contact['gender']
                })

data = load_json_file('nainika_adoptions.json')

# Save contacts to CSV
if data:
    save_contacts_to_csv(data, 'contacts.csv')
