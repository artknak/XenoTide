import sqlite3

class DbProxy:
    def __init__(self, database_path='score.db'):
        self.database_path = database_path
        # Cria a tabela apenas uma vez
        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS score (points INTEGER)')

    def insert_score(self, points):
        # Salva um novo score de forma segura
        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO score (points) VALUES (?)', (points,))

    def fetch_best_score(self):
        # Retorna o maior score ou 0 se não houver nenhum
        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT MAX(points) FROM score')
            row = cursor.fetchone()

        return row[0] if row[0] is not None else 0