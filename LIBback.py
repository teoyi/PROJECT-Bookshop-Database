import sqlite3
import os.path

class Database():
    # Create a db to house the inputted data
    def __init__(self, db):
        self.connect = sqlite3.connect(db)
        self.cursor = connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS lib (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)")
        self.connect.commit()

    # Execute a command to add a row entry that contains all 4 var
    def add_entry(self, Title, Author, Year, ISBN):
        self.cursor.execute("INSERT INTO lib VALUES (NULL,?,?,?,?)", (Title, Author, Year, ISBN))
        self.connect.commit()

    # Execute a command to delete a book based on the ISBN
    # Since ISBN is a unique value that is tied to the book
    def delete_entry(self, id):
        self.cursor.execute("DELETE FROM lib WHERE id = ?", (id,))
        self.connect.commit()

    # Execute command to search for a specific part
    def search_entry(self, Title = "", Author = "", Year = "", ISBN = ""):
        self.cursor.execute("SELECT * FROM lib WHERE Title = ? OR Author = ? or YEAR = ? or ISBN = ?", (Title, Author, Year, ISBN))
        rows = self.cursor.fetchall()
        return rows

    # Execute command to update a book based on ISBN
    def update_entry(self, id, Title, Author, Year, ISBN):
        self.cursor.execute("UPDATE lib SET Title = ?, Author = ?, Year = ?, ISBN = ? WHERE id = ? ", (Title, Author, Year, ISBN, id))
        self.connect.commit()

    # Execute command to get values from db
    def view_all(self):
        self.cursor.execute("SELECT * FROM lib")
        rows = self.cursor.fetchall()
        return rows

    def __del__(self):
        self.connect.close()
        
#create_table()
# add_entry()
# delete_entry()
# search_entry()
# update_entry()
# view_all()
