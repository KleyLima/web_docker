# -*- coding: utf-8 -*-

from source.libs.validacpf_kleyton import ValidaCPF
from source.dao.people_dao import PeopleDAO
from source.dao.mapper.people_mapper import PeopleMapper

class PeopleService:
    def check_cpf(self, cpf):
        #TODO: cpf valido, porém nao esta no banco
        if ValidaCPF(cpf).valida_cpf():
            result = PeopleDAO().select_people_by_cpf(cpf=ValidaCPF(cpf).retira_formatacao())
            if not result:
                return {"Erro": "CPF Válido porém não consta na base."}
            return PeopleMapper().map(result=result)

        else:
            #TODO: cpf invalido
            resp = {"Erro": "CPF Inválido para consulta."}
            return resp
