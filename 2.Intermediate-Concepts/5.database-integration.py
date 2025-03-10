import sqlite3

# Connecting to a Database
conn = sqlite3.connect("example.db")  # Creates or connects to a database
cursor = conn.cursor()

# Create table (only runs once, does not duplicate)
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )'''
)

# Inserting multiple rows correctly
users = [
    ("Youssouf", 27),
    ("Ibrahim", 16)
]

# If just one do the bottom
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))

cursor.executemany(
    "INSERT INTO users (name, age) VALUES (?, ?)",
    users
)

# Commit changes before fetching data
conn.commit()

# Fetching Data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Printing results
print("Users in database:")
for row in rows:
    print(row)  # Prints each row

# Closing the connection properly
conn.close()
