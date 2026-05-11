import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import pooling
import bcrypt

load_dotenv()

pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME"),
    port=os.getenv("DB_PORT")
)



#===================
# Register
#===================
def register_user(username, password):
    conn = pool.get_connection()
    cursor = conn.cursor()
    try:
        # --- Check if user already exists ---
        query = "SELECT * FROM players WHERE username = %s"
        cursor.execute(query, (username,))

        existing_user = cursor.fetchone()

        if existing_user:
            return False, "Utilisateur déjà existant"

        # --- Hash password ---
        hashed_password = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )

        # --- Insert user ---
        query = """
        INSERT INTO players (username, password)
        VALUES (%s, %s)
        """

        cursor.execute(query, (
            username,
            hashed_password.decode()
        ))

        conn.commit()

        return True, "Compte créé"
    finally:
        cursor.close()
        conn.close()
