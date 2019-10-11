# coding: utf-8

from sys import argv
from functools import reduce
from re import sub
from random import randrange  as rd


class ValidaCPF:
    def __init__(self, num_cpf=''):
        self.num_cpf = num_cpf

    def valida_cpf(self):
        self.num_cpf = self.retira_formatacao()
        cpf = [int(num) for num in self.num_cpf.zfill(11)]
        if len(set(cpf)) != 1:
            first_check = int(
                (10 * reduce(lambda a, b: a + b, [x * y for x, y in zip(cpf[:9], range(10, 1, -1))])) % 11)
            if first_check == cpf[9]:
                sec_check = int(
                    10 * reduce(lambda a, b: a + b, [x * y for x, y in zip(cpf[:10], range(11, 1, -1))])) % 11
                if sec_check == cpf[10]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def retira_formatacao(self):
        cpf = sub('\D', '', str(self.num_cpf))
        return cpf

    @classmethod
    def gera_cpf(cls):
        cls.num_cpf = rd(111111111, 999999999)
        ls_cpf = [int(num) for num in str(cls.num_cpf)]
        first = int((10 * reduce(lambda a, b: a + b, [x * y for x, y in zip(ls_cpf[:9], range(10, 1, -1))])) % 11)
        first = 0 if first == 10 else first
        ls_cpf.append(first)
        second = int(10 * reduce(lambda a, b: a + b, [x * y for x, y in zip(ls_cpf[:10], range(11, 1, -1))])) % 11
        cls.num_cpf = str(cls.num_cpf) + str(first) + str(second)
        if ValidaCPF(cls.num_cpf).valida_cpf():
            return cls.num_cpf
        else:
            return ValidaCPF().gera_cpf()


if __name__ == '__main__':
    # print("CPF: {}".format(ValidaCPF(argv[1]).retira_formatacao()))
    # ValidaCPF(argv[1]).valida_cpf()
    print(ValidaCPF('45815372-072').valida_cpf())

