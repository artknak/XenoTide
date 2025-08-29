import sqlite3

class DbProxy:
    """Proxy to handle storing and fetching high scores from a SQLite database."""

    def __init__(self, database_path='score.db'):
        """
        Initialize database and ensure score table exists.

        :param database_path: Database name (default = score.db)
        """
        self.database_path = database_path

        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS score (points INTEGER)')

    def insert_score(self, points):
        """
        Insert a new score into the database.

        :param points: Points to be added.
        """
        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO score (points) VALUES (?)', (points,))

    def fetch_best_score(self):
        """Return the highest score store in the database, or 0 if none exists."""
        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT MAX(points) FROM score')
            row = cursor.fetchone()

        return row[0] if row[0] is not None else 0