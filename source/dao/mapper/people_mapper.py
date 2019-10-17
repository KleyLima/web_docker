# -*- coding:utf-8 -*-

from source.dao.models.people import People


class PeopleMapper:
    def map(self, result):
        return People(nome=result["nome"],
                      dt_nasc=str(result["dt_nasc"])).__dict__

    def dicter(self, result):
        return {"nome": result["nome"], "dt_nasc": result["dt_nasc"]}
