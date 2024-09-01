import json
from flask import Flask, jsonify, request, abort

app = Flask(__name__)


# Path to the JSON file
DATA_FILE = 'data.json'

# Load data from JSON file
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save data to JSON file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Sample data to simulate a database
#books = [
#    {"id": 1, "title": "1984", "author": "George Orwell"},
#    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
#]

# Initialize books list from the JSON file
books = load_data()

# Helper function to find a book by ID
def find_book(book_id):
    return next((book for book in books if book['id'] == book_id), None)

# Route to test the API
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Books API!"

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Route to get a book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = find_book(book_id)
    if book is None:
        abort(404)
    return jsonify(book)

@app.route('/books', methods=['POST'])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    
    new_id = books[-1]['id'] + 1 if books else 1
    new_book = {
        'id': new_id,
        'title': request.json['title'],
        'author': request.json.get('author', "")
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = find_book(book_id)
    if book is None:
        abort(404)
    if not request.json:
        abort(400)
    
    book['title'] = request.json.get('title', book['title'])
    book['author'] = request.json.get('author', book['author'])
    save_data(books)  # Save the updated list to file
    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = find_book(book_id)
    if book is None:
        abort(404)
    books.remove(book)
    save_data(books)  # Save the updated list to file
    return jsonify({'result': True})



if __name__ == "__main__":
    app.run(debug=True)
