# This is a little challenge I wanted to work on to learn something about Automation in Python and SQL

## Using Python 3.12.2

### Install Pytest:
```
pip install pytest
```

### Run Pytest:
```
Pytest
```

### Run Parse Text File:
```
python3 lib/parse_text_file.py
```
##### Result:
```
TXT Plain Text File Format:

A plain text file that contains unformatted text. It is popular due to wide range of compatibility.



W.B. Yeats

A Prayer For My Daughter.... etc etc
```

### Run Parse CSV File:
```
python3 lib/parse_csv_file.py
```
##### Result:
```
John Doe john.doe@example.com 555-1234
Jane Smith jane.smith@example.com 555-5678
Alice Johnson alice.johnson@example.com 555-9876
Bob Brown bob.brown@example.com 555-5432
Eve Williams eve.williams@example.com 555-8765
```

### Run Query SQLite DB:
```
python3 lib/query_sql_db1.py
```
##### Result:
```
(1, 'John Doe', 'john.doe@example.com', '555-1234')
(2, 'Jane Smith', 'jane.smith@example.com', '555-5678')
(3, 'Nathan Lambertson', 'lambertones@gmail.com', '435-6889')
```

# Make sure SQLite is installed on your system:
[SQLite website](https://www.sqlite.org/)
