# -*- coding: utf-8 -*-


class People:
    """
    Classe que representa a tabela People do banco de dados, carregando seus atributos.
    """
    @classmethod
    def __init__(cls, id_people="", nome="", cpf="", dt_nasc=""):
        cls.id_people = id_people
        cls.nome = nome
        cls.cpf = cpf
        cls.dt_nasc = dt_nasc
