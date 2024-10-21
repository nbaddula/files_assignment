import csv
from loading_json import load_json_file  # Import the load_json_file function

# Function to save books to CSV
def save_books_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['book_id', 'isbn10', 'isbn13', 'title', 'category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for record in data:
            for adoption in record['adoptions']:
                book = adoption['book']
                writer.writerow({
                    'book_id': book['id'],
                    'isbn10': book['isbn10'],
                    'isbn13': book['isbn13'],
                    'title': book['title'],
                    'category': book['category']
                })

data = load_json_file('nainika_adoptions.json')

# Save books to CSV
if data:
    save_books_to_csv(data, 'books.csv')
