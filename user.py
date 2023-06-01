
import sqlite3
class User:
    def __init__(self, username, firstname, lastname):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    def to_db(self):
        pass

    @classmethod
    def from_db(cls, username):
        connection = sqlite3.connect("tweb.db") # Muss vorher angelegt werden.
        cursor = connection.cursor()
        sql = f"SELECT name FROM personen WHERE name = {username}"
        cursor.execute(sql)
        row = cursor.fetchone()
        connection.close()
        return User(row[0],row[1],row[2])

user = User.from_db("name")
