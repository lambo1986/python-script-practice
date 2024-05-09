import sqlite3

def query_database(database_file, query):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

database_file = 'example.db'
query = 'SELECT * FROM contacts'
query_database(database_file, query)
