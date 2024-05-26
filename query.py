import sqlite3
from sqlite3 import Error


def create_connection(db_path):
    connection = None
    try:
        connection = sqlite3.connect(db_path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


if __name__ == "__main__":
    connection = create_connection("db.sqlite3")
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT auth_user.id, username, COUNT(links_link.id) as link_count
        FROM auth_user
        LEFT JOIN links_link ON links_link.user_id = auth_user.id
        GROUP BY auth_user.id
        ORDER BY link_count DESC
        LIMIT 10"""
    )

    rows = cursor.fetchall()

    for row in rows:
        print(f"id: {row[0]}, username: {row[1]}, link_count: {row[2]}")
