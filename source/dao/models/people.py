# -*- coding: utf-8 -*-

import json


class People:
    """
    Classe que representa a tabela People do banco de dados, carregando seus atributos.
    """
    def __init__(self, id_people="", nome="", cpf="", dt_nasc: str = ""):
        self.id_people = id_people
        self.nome = nome
        self.cpf = cpf
        self.dt_nasc = dt_nasc
