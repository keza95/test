import sqlite3

conn = sqlite3.connect('books.sqlite')
cursor = conn.cursor()
sql_query = """CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            language TEXT
            )
"""

cursor.execute(sql_query)