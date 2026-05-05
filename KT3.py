import csv

# Задание 1
def get_books(filename):
    books = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            if not row or row[0] == 'isbn':
                continue
            
            isbn = row[0]
            title = row[1]
            author = row[2]
            quantity = int(row[3])
            price = float(row[4])
            
            books.append([isbn, title, author, quantity, price])
    
    return books

# Задание 2
def filtered_books(books, substring):
    filtered = []
    substring_lower = substring.lower()
    
    for book in books:
        if substring_lower in book[1].lower():
            combined_title_author = f"{book[1]}, {book[2]}"
            filtered.append([
                book[0],           
                combined_title_author, 
                book[3],         
                book[4]            
            ])
    
    return filtered

# Задание 3
def calculate_total_values(filtered_books):
    result = []
    for book in filtered_books:
        isbn = book[0]
        total_value = book[2] * book[3] 
        result.append((isbn, total_value))
    
    return result
