import sqlite3

cnx = sqlite3.connect('dbparque.sqlite3')
cur = cnx.cursor()

cur.execute("SELECT * FROM ATRACOES;")
todos = cur.fetchall()
print(f'\nTodos: {todos}')
# print(type(todos))

