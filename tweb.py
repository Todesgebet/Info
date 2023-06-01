import sqlite3
conn = sqlite3.connect('tweb.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS personen (id INTEGER PRIMARY KEY, vorname TEXT, nachname TEXT,klasse TEXT)")
cursor.execute("INSERT INTO personen (vorname, nachname,klasse) VALUES (?, ?, ?)",("Florian","Meyer","Q2"))
cursor.execute("SELECT * FROM personen")
rows = cursor.fetchall()
for row in rows:
     print(row)

conn.commit()
conn.close()