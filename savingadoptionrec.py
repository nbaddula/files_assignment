import csv
from loading_json import load_json_file  # Import the load_json_file function

# Function to save adoptions to CSV
def save_adoptions_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'university', 'book_title', 'quantity', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for record in data:
            university = record['university']['name']
            for adoption in record['adoptions']:
                writer.writerow({
                    'id': record['id'],
                    'university': university,
                    'book_title': adoption['book']['title'],
                    'quantity': adoption['quantity'],
                    'date': adoption['date']
                })


data = load_json_file('nainika_adoptions.json')

if data:
    # Save adoptions to CSV
    save_adoptions_to_csv(data, 'adoptions.csv')
