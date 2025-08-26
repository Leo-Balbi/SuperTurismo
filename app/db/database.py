import sqlite3
import os

DB_FILE = "data/superturismo.db"

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temporada TEXT,
            fecha TEXT,
            equipo TEXT,
            piloto TEXT,
            pieza TEXT,
            precinto TEXT,
            motivo TEXT,
            situacion TEXT
        )
    """)
    conn.commit()
    conn.close()
