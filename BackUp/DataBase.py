import sqlite3
class Database():

    def __init__(self, bd):
        self.conn = sqlite3.connect(bd)
        self.c = self.conn.cursor()

    def del_info(self, id):
        with self.conn:
            self.c.execute("""DELETE FROM num_fact  WHERE id_tg = ? """,(id, ))
    def add_info(self, array):
        with self.conn:
            self.c.execute("""INSERT INTO num_fact VALUES (NULL, ?, ?, ?, ?);""", array)

    def add_table(self):
        with self.conn:
            self.c.execute("""CREATE TABLE IF NOT EXISTS num_fact (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_tg INTEGER,
                    name TEXT,
                    text_num TEXT,
                    type_num TEXT)""")
    def show_all(self,id_tg):
        with self.conn:
            a = []
            self.c.execute("""SELECT  text_num, type_num FROM num_fact WHERE id_tg = ?""" ,(id_tg, ))
            result1 = self.c.fetchall()

            return result1

db = Database("mysqlite.db")
db.del_info(1065143120)