from flask import Flask
from flask import render_template, redirect,request,session
import sqlite3
pizza=5
title= "Testing Ground"
app = Flask(__name__)

@app.route("/")
def hello_world():
    return redirect("/add_user")


class User:
    def __init__(self, vorname, nachname, klasse):
        self.vorname = vorname
        self.nachname = nachname
        self.klasse = klasse
        
    def to_db(self):
        connection = sqlite3.connect("tweb.db")
        cursor = connection.cursor()
        sql = f"INSERT INTO personen (vorname, nachname, klasse) VALUES ('{self.vorname}', '{self.nachname}', '{self.klasse}')"
        cursor.execute(sql)
        connection.commit()
        connection.close()
                
    @classmethod
    def from_db(cls, vorname):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        sql = f'SELECT vorname, nachname, klasse FROM personen WHERE vorname = "{vorname}"'
        cursor.execute(sql)
        row = cursor.fetchone()        
        connection.close()
        return cls(row[0], row[1], row[2])




@app.route("/add_user", methods=["GET", "POST"])
def user_form():
    if request.method == "GET":
        return '''<form method="POST">
                      <div><label>Vorname: <input type="text" name="vorname"></label></div>
                      <div><label>Nachname: <input type="text" name="nachname"></label></div>
                      <div><label>Klasse: <input type="text" name="klasse"></label></div>
                      <input type="submit" value="Submit">
                  </form>'''
    else:
        vorname = request.form.get("vorname")
        nachname = request.form.get("nachname")
        klasse = request.form.get("klasse")
        user = User(vorname, nachname, klasse)
        user.to_db()
        return f"User {vorname} was created"
