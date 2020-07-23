import sqlite3

# Create a db to house the inputted data
def create_table():
    connect = sqlite3.connect("lib.db")
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS lib (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)")
    connect.commit()
    connect.close()

# Execute a command to add a row entry that contains all 4 var
def add_entry(Title, Author, Year, ISBN):
    connect = sqlite3.connect("lib.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO lib VALUES (NULL,?,?,?,?)", (Title, Author, Year, ISBN))
    connect.commit()
    connect.close()

# Execute a command to delete a book based on the ISBN
# Since ISBN is a unique value that is tied to the book
def delete_entry(id):
    connect = sqlite3.connect("lib.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM lib WHERE id = ?", (id,))
    connect.commit()
    connect.close()

# Execute command to search for a specific part
def search_entry(Title = "", Author = "", Year = "", ISBN = ""):
    connect = sqlite3.connect("lib.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM lib WHERE Title = ? OR Author = ? or YEAR = ? or ISBN = ?", (Title, Author, Year, ISBN))
    rows = cursor.fetchall()
    connect.close()
    return rows

# Execute command to update a book based on ISBN
def update_entry(id, Title, Author, Year, ISBN):
    connect = sqlite3.connect("lib.db")
    cursor = conect.cursor()
    cursor.execute("UPDATE lib SET Title = ?, Author = ?, Year = ?, ISBN = ? WHERE id = ? ", (Title, Author, Year, ISBN, id))
    connect.commit()
    connect.close()

# Execute command to get values from db
def view_all():
    connect = sqlite3.connect("lib.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM lib")
    rows = cursor.fetchall()
    connect.close()
    return rows


# create_table()
# add_entry()
# delete_entry()
# search_entry()
# update_entry()
# view_all()
