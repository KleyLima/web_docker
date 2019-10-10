from source.dao.models.connection import DB


class Teste(DB):
    def __init__(self):
        self.conn = DB().connect().cursor()

    def query(self):
        sql = "SELECT nome FROM people WHERE id_people={}".format(1)
        self.conn.execute(sql)
        result = self.conn.fetchone()
        print(result['nome'])


if __name__ == '__main__':
    Teste().query()
