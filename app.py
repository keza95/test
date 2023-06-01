from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)


@app.route('/home', methods=['GET'])
def main():
    return render_template('/html/index.html')


@app.route('/showbook', methods=['GET'])
def displayForm():
    return render_template('/html/forms.html')
# Comment

@app.route('/viewbooks', methods=['GET'])
def showAllBooks():
    conn = sqlite3.connect('books.sqlite')
    cursor = conn.cursor()

    sql_query_fetch_all_books = """SELECT * FROM books"""

    cursor.execute(sql_query_fetch_all_books)
    books = cursor.fetchall()  # Fetches all result from sql_query_fetch_all_books

    return render_template('/html/viewbooks.html', books_content=books)


@app.route('/addbook', methods=['POST'])
def addBook():
    conn = sqlite3.connect('books.sqlite')
    cursor = conn.cursor()

    # Data received is in a 'form' type
    received_data_object = request.form
    data_obj_to_save = dict(received_data_object)

    data_model = {
        'title': received_data_object['title'],
        'author': received_data_object['author'],
        'language': received_data_object['language']
    }

    sql_query = """INSERT INTO books(title, author, language) VALUES (?, ?, ?)"""
    cursor.execute(sql_query, (data_model['title'], data_model['author'], data_model['language']))
    conn.commit()

    return 'Book added successfully', 201


if __name__ == '__main__':
    app.run(debug=True)
