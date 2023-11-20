#404 (Not Found) and 500 (Internal Server Error) errors using error handlers

from flask import Flask, render_template

app = Flask(__name__)

# Dummy data for demonstration
books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2'},
    {'id': 3, 'title': 'Book 3', 'author': 'Author 3'},
]

# Route for handling 404 errors
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Route for handling 500 errors
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html', books=books)

# Route for getting a specific book
@app.route('/books/<int:book_id>')
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return render_template('book.html', book=book)
    else:
        # Raise a 404 error if the book is not found
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
