from loading_json import load_json_file  # Import the load_json_file function

# Function to list book categories and save books by category
def list_and_save_books_by_category(data):
    categories = set()
    for record in data:
        for adoption in record['adoptions']:
            categories.add(adoption['book']['category'])
    
    print("Available categories:")
    for category in categories:
        print(category)
    
    chosen_category = input("Enter a category: ")
    books_in_category = [adoption['book']['title'] for record in data for adoption in record['adoptions'] if adoption['book']['category'] == chosen_category]
    
    if books_in_category:
        with open(f"{chosen_category}_books.txt", 'w') as file:
            for book in books_in_category:
                file.write(book + '\n')
        print(f"Books in the {chosen_category} category saved to {chosen_category}_books.txt")
    else:
        print(f"No books found in the {chosen_category} category.")

data = load_json_file('nainika_adoptions.json')

# Save books by category
if data:
    list_and_save_books_by_category(data)
