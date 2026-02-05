import hashlib
from backend.database import cursor, conn

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup(username, password):
    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hash_password(password))
        )
        conn.commit()
        return True
    except Exception as e:
        print("Signup error:", e)
        return False

def login(username, password):
    cursor.execute(
        "SELECT id FROM users WHERE username=? AND password=?",
        (username, hash_password(password))
    )
    return cursor.fetchone()
