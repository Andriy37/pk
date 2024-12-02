#import sqlite3
#conn = sqlite3.connect("Artistc.db")
#cursor = conn.cursor()

#cursor.execute('SELECT * FROM artists')
#data = cursor.fetchall()
#print(len(data))

#cursor.execute('SELECT * FROM artists WHERE gender=="Female"')
#data = cursor.fetchall()
#print(len(data))

#cursor.execute('SELECT * FROM artists WHERE "Birth Year"<1900')
#data = cursor.fetchall()
#print(len(data))

from flask import Flask, url_for, redirect
import sqlite3

def index():
    pass 

app = Flask(__name__)
app.add_url_rule("/", "index", index)

if __name__ == "__main__":
    app.run()

