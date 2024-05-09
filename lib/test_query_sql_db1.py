import sqlite3

def test_query_database():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    query = 'SELECT * FROM contacts'
    cursor.execute(query)
    rows = cursor.fetchall()

    assert len(rows) == 3
    assert rows[0] == (1, 'John Doe', 'john.doe@example.com', '555-1234')
    assert rows[1] == (2, 'Jane Smith', 'jane.smith@example.com', '555-5678')
    assert rows[2] == (3, 'Nathan Lambertson', 'lambertones@gmail.com', '435-6889')

    conn.close()

test_query_database()
