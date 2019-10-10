from source.dao.models.connection import DB


class PeopleDAO(DB):
    def __init__(self):
        self.conn = DB().connect().cursor()

    def select_people_by_cpf(self, cpf):
        sql = "SELECT nome, dt_nasc FROM people WHERE cpf={}".format(cpf)
        self.conn.execute(sql)
        result = self.conn.fetchone()
        return result


if __name__ == '__main__':
    PeopleDAO().select_people_by_cpf('45815372072')

