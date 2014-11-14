import sqlite3

conn = sqlite3.connect('cadastro.db')
conn.cursor()
conn.execute('''CREATE TABLE inscricoes (name, email, escola, serie)''')