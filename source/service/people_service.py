# -*- coding: utf-8 -*-

from source.libs.validacpf_kleyton import ValidaCPF
from source.dao.people_dao import PeopleDAO
from source.dao.mapper.people_mapper import PeopleMapper

class PeopleService:
    def check_cpf(self, cpf):
        if ValidaCPF(cpf).valida_cpf():
            result = PeopleDAO().select_people_by_cpf(cpf=cpf)
            return PeopleMapper().map(result=result)

        else:
            resp = {"resp": "CPF Inválido para consulta."}
            return resp
