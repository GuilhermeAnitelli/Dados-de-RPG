# Objetivo dessa aplicação é lançar dados

import random
from time import sleep

class SimuladorDadosRPG:
    def __init__(self):
        self.__dados = [4, 6, 8, 10, 12, 20, 100]

    def lanca_dado(self, tipo: int, quantidade_de_dados: int = 1):
        valor_maximo = tipo
        lancamentos = quantidade_de_dados
        resultados = []
        retorno = None
        if lancamentos > 1:
            for dado in range(lancamentos):
                resultado = random.randint(1, valor_maximo)
                print(f'\nO dado {dado+1} tem o valor de: {resultado}')
                resultados.append(resultado)
                retorno = resultados
        else:
            resultado = random.randint(1, valor_maximo)
            print(f'Resultado {resultado}')
            retorno = resultado

        return retorno

    def soma_resultado(self, lista):
        soma = 0
        for i in lista:
            soma = soma + int(i)
        return soma

    def execute(self):
        print('Executando...')
        print('Olá...')
        sleep(2)
        print('...')
        sleep(1)
        print('Seja bem-vindo/a ao meu simulador de dados de RPG!')
        sleep(1)
        print('Qual é o seu nome, jogador?')
        sleep(1)
        nome = input('Seu nome: ')
        sleep(1)
        print(f'Seja bem-vindo/a novamente, {nome}! É um prazer ter você aqui!')
        sleep(1)
        lancar = True
        while lancar == True:
            print('Quer lançar os dados? ')
            sleep(2)
            print('SIM (1)')
            print('NÃO (2)')
            try:
                resposta = int(input('Sua escolha: '))
                if resposta == 1:
                    print('Seu desejo é uma ordem!')
                    sleep(1)
                    print('Qual modelo quer lançar?')
                    sleep(2)
                    contador = 0
                    for dado in self.__dados:
                        print(f'D{dado} ({contador})')
                        contador += 1
                        sleep(1)
                    try:
                        tipo = int(input('Digite o tipo de dado: '))
                    except:
                        print('Não aceito! Digite um tipo de dado como 4, 6, 8, 10, 12, 20 ou 100.')
                    sleep(2)
                    print(f'Você vai lançar o D{ self.__dados[tipo] }')
                    sleep(1)

                    print('Quantos dados vai querer lançar?')
                    sleep(1)
                    try:
                        quant = int(input('A resposta tem que ser um número inteiro: '))
                    except:
                        print('Resposta invalida, tente novamente!')
                    resultado = self.lanca_dado(self.__dados[tipo], quant)
                    if type(resultado) == list:
                        resultado = self.soma_resultado(resultado)
                    print(f'Você lançou {quant} D{ self.__dados[tipo] } e obteve {resultado} como resultado.' )
                    sleep(5)

                elif resposta == 2:
                    lancar = False
                    print('Ok! Até a próxima!')

            except:
                print('Resposta invalida, tente novamente!')
if __name__ == '__main__':
    SimuladorDadosRPG().execute()




