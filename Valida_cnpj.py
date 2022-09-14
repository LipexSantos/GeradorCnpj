# E aqui é "por trás" de onde botamos o código para trabalhar, como se fosse uma "Central".

import re
from random import randint

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


# r é para tratar a '/' ou os caracteres especias
def removedor_caractere(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def valida(cnpj):
    cnpj = removedor_caractere(cnpj)

    try:
        if validador_numbers(cnpj):
            return False
    except:
        return False

    try:
        novo_cnpj = calc_digito(cnpj=cnpj, digito=1)
        novo_cnpj = calc_digito(cnpj=novo_cnpj, digito=2)
    except Exception as e:
        return False

    if novo_cnpj == cnpj:
        return True
    else:
        return False


def calc_digito(cnpj, digito):
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return None

    total = 0
    for index, regressivo in enumerate(regressivos):
        total += int(cnpj[index]) * regressivo

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0

    return f'{novo_cnpj}{digito}'


def validador_numbers(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if len(cnpj) != 14:
        print('\033[31mCNPJ está errado. por favor digite um CNPJ válido!\033[m')
    else:
        if sequencia == cnpj:
            return True
        else:
            return False


def gerador():
    blocos = [randint(0, 9) for _ in range(8)]
    quarto_bloco = [0, 0, 0, 1, 0, 0]
    inicio_cnpj = blocos + quarto_bloco

    result = ''.join(map(str, inicio_cnpj))
    novo_cnpj = calc_digito(cnpj=result, digito=1)
    novo_cnpj = calc_digito(cnpj=novo_cnpj, digito=2)

    return novo_cnpj

