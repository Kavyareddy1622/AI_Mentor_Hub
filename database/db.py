import sqlite3

DATABASE = "database/student.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        task TEXT,

        completed INTEGER
    )
    """)

    conn.commit()

    conn.close()