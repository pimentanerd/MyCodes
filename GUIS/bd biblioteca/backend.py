import sqlite3
import time
from tkinter import *

def connect():
	conn=sqlite3.connect("livro.db")
	cur=conn.cursor()
	cur.execute("""
	CREATE TABLE livro(
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		titulo VARCHAR(50) NOT NULL,
		autor VARCHAR(50) NOT NULL,
		ano INTEGER NOT NULL,
		devolucao INTEGER NOT NULL
	);
	""")
	conn.commit()
	conn.close()

def search(titulo="", autor="", ano=""):
	conn=sqlite3.connect("livro.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM livro WHERE titulo=? OR autor=? OR ano=?", (titulo, autor, ano,))
	rows=cur.fetchall()
	conn.close()
	return rows

def delete(id):
	conn=sqlite3.connect("livro.db")
	cur=conn.cursor()
	cur.execute("DELETE from livro WHERE id=?, (id,)")
	rows=cur.fetchall()
	conn.close()
	return rows

def update(id, titulo, autor, ano,):
	conn=sqlite3.connect("livro.db")
	cur=conn.cursor()
	cur.execute("UPDATE livro and set keyword SET title=?, autor=?, ano=? WHERE id=?", (titulo, autor, ano))
	conn.commit()
	rows=cur.fetchall()
	conn.close()

