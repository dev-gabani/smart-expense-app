import sqlite3

def create_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # User table with authentication fields
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password_hash TEXT,
        income REAL DEFAULT 0.0
    )
    """)
    
    # Incomes tied to user
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incomes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        source TEXT,
        amount REAL,
        date TEXT,
        FOREIGN KEY(user_id) REFERENCES user(id)
    )
    """)
    
    # Expenses tied to user
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        category TEXT,
        amount REAL,
        date TEXT,
        FOREIGN KEY(user_id) REFERENCES user(id)
    )
    """)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_expenses ON expenses(user_id);")
    
    # Categories tied to user
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        name TEXT,
        percentage REAL,
        FOREIGN KEY(user_id) REFERENCES user(id)
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
    print("Database created successfully!")