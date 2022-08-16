import sqlite3
class Database():

    def __init__(self, bd):
        self.conn = sqlite3.connect(bd)
        self.c = self.conn.cursor()

    def del_info(self, id):
        with self.conn:
            self.c.execute("""DELETE FROM facts  WHERE id_name = ? """,(id, ))
    def add_user(self, array):
        with self.conn:
            self.c.execute("""INSERT INTO users VALUES (NULL, ?, ?);""", array)
    def add_fact(self, array):
        with self.conn:
            self.c.execute("""INSERT INTO facts VALUES (NULL, ?, ?, ?);""", array)

    def get_users(self, id_tg):
        with self.conn:
            self.c.execute("""SELECT  id FROM users WHERE id_tg = ?""" ,(id_tg, ))
            result = self.c.fetchall()
            return  result

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
            self.c.execute("""SELECT text, type, users.name FROM facts JOIN users ON users.id = facts.id_name WHERE facts.id_name = ?""",(id_tg, ))
            result1 = self.c.fetchall()

            return result1

# db = Database("mysqlite.db")
# # db.del_info(1065143120db
#
#
#
# r = db.get_users(5525)
# print(r[0][0])
# if not len(r)==0:
#     pass
# else:
#     db.add_user((5525, "oleg"))
#
# id_user =  db.get_users()
# db.add_fact((id_user, "text", "math"))
#
#
#
# result = db.show_all(id_user)
# print(result)









