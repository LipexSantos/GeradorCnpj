import Valida_cnpj
import os

# Aqui é onde botamos o código para trabalhar e gerenciamos alguns erros.

while True:
    try:
        opcao = int(input('[1] - Validar CNPJ\n'
                          '[2] - Gerar CNPJ Válido\n'
                          'Digite sua Opção: '))

        if opcao == 1:
            CNPJ = input('Seu Cnpj: ')
            if Valida_cnpj.valida(CNPJ):
                print(f'{CNPJ} é Válido', os.linesep)
                break
            else:
                print(f'{CNPJ} é Inválido', os.linesep)
        elif opcao == 2:
            CNPJ = Valida_cnpj.gerador()
            if Valida_cnpj.valida(CNPJ):
                print(f'Gerado: {CNPJ[:2]}.{CNPJ[2:5]}.{CNPJ[5:8]}/{CNPJ[8:12]}-{CNPJ[12:14]}', os.linesep)
                break
            else:
                print('\033[31mInválido\033[m', os.linesep)
        elif opcao != 1 and 2:
            print('\033[31mDigite uma das Opções por favor!\033[m', os.linesep)
            continue
    except ValueError:
        print('\033[31mError! Tente Novamente.\033[m', os.linesep)

