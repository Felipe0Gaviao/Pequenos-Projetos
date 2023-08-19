from random import randint,choice
from itertools import cycle
from time import sleep

class JogoDoPorquinho:

    def __init__(self):
        self.OBJETIVO = 10
        self.REF = {'j':'Jogador','c':'Computador'}

        print('Bem vindo ao jogo do Porquinho')

        pessoas = self.str_int(input('Quantas pessoas vão jogar? '))
        self.jogadores = {f'j{i+1}':{'at':0,'md':0} for i in range(pessoas)}

        computadores = self.str_int(input('Quantos Computadores? '))
        self.jogadores.update({f'c{i+1}':{'at':0,'md':0} for i in range(computadores)} if computadores>0 else {})

        self.ciclo = cycle(self.jogadores)
        self.ciclo_val = next(self.ciclo)

        self.rodar()

    def str_int(self,texto:str) -> int:

        try:
            inteiro = int(texto)
        except ValueError:
            inteiro = self.str_int(input('Precisa ser um número'))
        
        return inteiro

    def rolar_dado(self):
        valor = randint(1,6)

        if valor == 1:
            print('Uma pena, caiu 1')
            sleep(.2)
            print('você perdeu os pontos da rodada atual')
            self.jogadores[self.ciclo_val]['md'] = self.jogadores[self.ciclo_val]['at']
            sleep(.2)
            print('passando para o próximo jogador...')
            self.ciclo_val = next(self.ciclo)
        else:
            self.jogadores[self.ciclo_val]['md'] += valor
            print(f'{self.REF[self.ciclo_val[0]]} {self.ciclo_val[1]} está com {self.jogadores[self.ciclo_val]["md"]} nesta rodada')

    def passar_rodada(self):
        print('Mantendo Pontos Atuais...')
        self.jogadores[self.ciclo_val]['at'] = self.jogadores[self.ciclo_val]['md']

        print(f'{self.REF[self.ciclo_val[0]]} {self.ciclo_val[1]} possui: {self.jogadores[self.ciclo_val]["at"]} {"ponto" if self.jogadores[self.ciclo_val]["at"] == 1 else "pontos"}')

        print('passando para o próximo jogador...')
        self.ciclo_val = next(self.ciclo)
    
    def rodar(self):
        while True:
            if self.jogadores[self.ciclo_val]['at'] >= self.OBJETIVO:
                print(f'{self.REF[self.ciclo_val[0]]} {self.ciclo_val[1]} Ganhou o Jogo')

                match input('Gostaria de continuar (s/n)? '):
                    case 's':
                        self.__init__()
                    case 'n':
                        break

            if self.ciclo_val[0] == 'j':

                print('Comandos: \
                    \nr | roll | rolar : rolar o dado \
                    \np | pass | passar : passar para o próximo.\n')

                print(f'OBJETIVO: o jogo acaba quando alguém conseguir {self.OBJETIVO} pontos\n')

                match input(f'Jogador {self.ciclo_val[1]}: '):
                    case i if i.lower() in ['r','roll','rolar']:
                        self.rolar_dado()
                    case i if i.lower() in ['p','pass','passar']:
                        self.passar_rodada()

            if self.ciclo_val[0] == 'c':
                sleep(1)
                choice([self.rolar_dado(),self.passar_rodada()])

if __name__ == '__main__':
    JogoDoPorquinho()

# def str_int(texto:str):
#     try:
#         texto = int(texto)
#     except ValueError:
#         texto = str_int(input('Tem que ser um número: '))
#     return texto

# print('Bem vindo ao jogo do Porquinho')

# OBJETIVO = 10
# REPR = {'j':'Jogador','c':'Computador'}

# pessoas = str_int(input('Quantas pessoas vão jogar? '))
# jogadores = {f'j{i+1}':{'at':0,'md':0} for i in range(pessoas)}

# computadores = str_int(input('Quantos Computadores? '))
# jogadores.update({f'c{i+1}':{'at':0,'md':0} for i in range(computadores)} if computadores>0 else {})

# ciclo = cycle(jogadores)
# ciclo_val = next(ciclo)

# def rolar_dado():
#     valor = randint(1,6)

#     global ciclo_val, ciclo
    
#     if valor == 1:
#         print('Uma pena, caiu 1')
#         sleep(.2)
#         print('você perdeu os pontos da rodada atual')
#         jogadores[ciclo_val]['md'] = jogadores[ciclo_val]['at']
#         sleep(.2)
#         print('passando para o próximo jogador...')
#         ciclo_val = next(ciclo)
#     else:
#         jogadores[ciclo_val]['md'] += valor
#         print(f'{REPR[ciclo_val[0]]} {ciclo_val[1]} está com {jogadores[ciclo_val]["md"]} nesta rodada')

# def passar_rodada():

#     global ciclo_val, ciclo

#     print('Mantendo Pontos Atuais...')
#     jogadores[ciclo_val]['at'] = jogadores[ciclo_val]['md']

#     print(f'{REPR[ciclo_val[0]]} {ciclo_val[1]} possui: {jogadores[ciclo_val]["at"]} {"ponto" if jogadores[ciclo_val]["at"] == 1 else "pontos"}')

#     print('passando para o próximo jogador...')
#     ciclo_val = next(ciclo)

# while True:
#     if ciclo_val[0] == 'j':

#         print('Comandos: \
#             \nr | roll | rolar : rolar o dado \
#             \np | pass | passar : passar para o próximo.\n')

#         print(f'OBJETIVO: o jogo acaba quando alguém conseguir {OBJETIVO} pontos\n')

#         match input(f'Jogador {ciclo_val[1]}: '):
#             case i if i.lower() in ['r','roll','rolar']:
#                 rolar_dado()
#             case i if i.lower() in ['p','pass','passar']:
#                 passar_rodada()
#     if ciclo_val[0] == 'c':
#         sleep(1)
#         choice([rolar_dado(),passar_rodada()])

#     if jogadores[ciclo_val]['at'] >= OBJETIVO:
#         print(f'{REPR[ciclo_val[0]]} {ciclo_val[1]} Ganhou o Jogo')
#         break