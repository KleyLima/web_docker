from source.dao.models.connection import DB


class PeopleDAO(DB):
    def __init__(self):
        self.conn = DB().connect().cursor()

    def select_people_by_cpf(self, cpf):
        query = "SELECT nome, dt_nasc FROM people WHERE cpf={}".format(cpf)
        self.conn.execute(query)
        result = self.conn.fetchone()
        return result


if __name__ == '__main__':
    print(PeopleDAO().select_people_by_cpf('45815372072'))

