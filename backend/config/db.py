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
    password=os.getenv("DB_PASSWORD"),
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

def login_user(username, password):
    conn = pool.get_connection()
    cursor = conn.cursor()

    try:
        # --- search user ---
        query = "SELECT password FROM players WHERE username = %s"
        cursor.execute(query, (username,))

        player = cursor.fetchone()

        if not player:
            return False, "Utilisateur ou mot de passe incorrect"

        stored_password = player[0]

        # --- check password hashed-
        if bcrypt.checkpw(
            password.encode(),
            stored_password.encode()
        ):
            return True, "Connexion réussie"
        else:
            return False, "Utilisateur ou mot de passe incorrect"

    finally:
        cursor.close()
        conn.close()

def save_score(username, score):
    conn = pool.get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT idPlayers FROM Players WHERE username = %s",
            (username,)
        )
        result = cursor.fetchone()

        if not result:
            return False

        player_id = result[0]

        cursor.execute(
            "SELECT score FROM Scores WHERE Players_idPlayers = %s",
            (player_id,)
        )
        existing = cursor.fetchone()

        if existing is None:
            cursor.execute(
                "INSERT INTO Scores (score, Players_idPlayers) VALUES (%s, %s)",
                (score, player_id)
            )
        else:
            if score > existing[0]:
                cursor.execute(
                    "UPDATE Scores SET score = %s WHERE Players_idPlayers = %s",
                    (score, player_id)
                )

        conn.commit()
        return True

    finally:
        cursor.close()
        conn.close()

#===================
# Ranking
#===================
def get_top_scores():

    conn = pool.get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT Players.username, Scores.score
            FROM Scores
            JOIN Players
            ON Scores.Players_idPlayers = Players.idPlayers
            ORDER BY Scores.score DESC
            LIMIT 10
        """)

        results = cursor.fetchall()

        scores = []

        for row in results:
            scores.append({
                "username": row[0],
                "score": row[1]
            })

        return scores

    finally:
        cursor.close()
        conn.close()