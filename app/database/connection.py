import sqlite3

def conectar():
    conexao = sqlite3.connect('app/database/database.db')
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

