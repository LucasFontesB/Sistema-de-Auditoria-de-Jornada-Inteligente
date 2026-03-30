import sqlite3

DB_PATH = "data/banco_horas.db"

def conectar():
    return sqlite3.connect(DB_PATH)


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS banco_horas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            funcionario TEXT,
            mes INTEGER,
            ano INTEGER,
            saldo_minutos INTEGER,
            UNIQUE(funcionario, mes, ano)
        )
    """)

    conn.commit()
    conn.close()