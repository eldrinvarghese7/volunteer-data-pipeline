import sqlite3

def get_connection():
    return sqlite3.connect("volunteer_data.db")

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    with open("db/schema.sql", "r") as f:
        schema = f.read()

    cursor.executescript(schema)
    conn.commit()
    conn.close()
