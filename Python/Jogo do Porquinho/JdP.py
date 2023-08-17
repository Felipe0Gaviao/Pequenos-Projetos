from random import randint,choice
from itertools import cycle
from time import sleep

def str_int(texto:str):
    try:
        texto = int(texto)
    except ValueError:
        texto = str_int(input('Tem que ser um número: '))
    return texto

print('Bem vindo ao jogo do Porquinho')

OBJETIVO = 10
REPR = {'j':'Jogador','c':'Computador'}

pessoas = str_int(input('Quantas pessoas vão jogar? '))
jogadores = {f'j{i+1}':{'at':0,'md':0} for i in range(pessoas)}

computadores = str_int(input('Quantos Computadores? '))
jogadores.update({f'c{i+1}':{'at':0,'md':0} for i in range(computadores)} if computadores>0 else {})

ciclo = cycle(jogadores)
ciclo_val = next(ciclo)

def rolar_dado():
    valor = randint(1,6)

    global ciclo_val, ciclo
    
    if valor == 1:
        print('Uma pena, caiu 1')
        sleep(.2)
        print('você perdeu os pontos da rodada atual')
        jogadores[ciclo_val]['md'] = jogadores[ciclo_val]['at']
        sleep(.2)
        print('passando para o próximo jogador...')
        ciclo_val = next(ciclo)
    else:
        jogadores[ciclo_val]['md'] += valor
        print(f'{REPR[ciclo_val[0]]} {ciclo_val[1]} está com {jogadores[ciclo_val]["md"]} nesta rodada')

def passar_rodada():

    global ciclo_val, ciclo

    print('Mantendo Pontos Atuais...')
    jogadores[ciclo_val]['at'] = jogadores[ciclo_val]['md']

    print(f'{REPR[ciclo_val[0]]} {ciclo_val[1]} possui: {jogadores[ciclo_val]["at"]} {"ponto" if jogadores[ciclo_val]["at"] == 1 else "pontos"}')

    print('passando para o próximo jogador...')
    ciclo_val = next(ciclo)

while True:
    if ciclo_val[0] == 'j':

        print('Comandos: \
            \nr | roll | rolar : rolar o dado \
            \np | pass | passar : passar para o próximo.\n')

        print(f'OBJETIVO: o jogo acaba quando alguém conseguir {OBJETIVO} pontos\n')

        match input(f'Jogador {ciclo_val[1]}: '):
            case i if i.lower() in ['r','roll','rolar']:
                rolar_dado()
            case i if i.lower() in ['p','pass','passar']:
                passar_rodada()
    if ciclo_val[0] == 'c':
        sleep(1)
        choice([rolar_dado(),passar_rodada()])

    if jogadores[ciclo_val]['at'] >= OBJETIVO:
        print(f'{REPR[ciclo_val[0]]} {ciclo_val[1]} Ganhou o Jogo')
        break