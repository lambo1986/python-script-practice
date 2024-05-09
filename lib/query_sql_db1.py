import sqlite3

def query_database(database_file, query):
    if not query.strip().startswith('SELECT'):
        raise ValueError("Invalid query. Only SELECT queries are allowed.")
    
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
