import sqlite3
from app.db.database import DB_FILE

def insert_registro(temporada, fecha, equipo, piloto, pieza, precinto, motivo, situacion):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO registros 
        (temporada, fecha, equipo, piloto, pieza, precinto, motivo, situacion)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (temporada, fecha, equipo, piloto, pieza, precinto, motivo, situacion))
    conn.commit()
    conn.close()
