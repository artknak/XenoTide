from code.DbProxy import DbProxy


class ScoreManager:
    def __init__(self):
        self.score = 0
        self.db_proxy = DbProxy()

    def add(self):
        self.score += 1

    def save(self):
        self.db_proxy.insert_score(self.score)

    def get_best(self):
        return self.db_proxy.fetch_best_score()