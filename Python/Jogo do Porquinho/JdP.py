from random import randint,choice
from itertools import cycle
from time import sleep

def roll():
    return randint(1,6)

def limpar_input(texto:str):
    try:
        texto = int(texto)
        return texto
    except ValueError:
        texto = limpar_input(input('Tem que ser um número: '))
        return texto

print('Bem vindo ao jogo do Porquinho')

OBJETIVO = 10

pessoas = limpar_input(input('Quantas pessoas vão jogar? '))
jogadores = {f'j{i+1}':0 for i in range(pessoas)}
computadores = limpar_input(input('Quantos Computadores? '))
jogadores.update({f'c{i+1}':0 for i in range(computadores)} if computadores>0 else {})

ciclo = cycle(jogadores)
ciclo_val = next(ciclo)

sup_arr = []

while True:
    if ciclo_val[0] == 'p':
        print('Comandos: \
            \nr | roll | rolar : rolar o dado \
            \np | pass | passar : passar para o próximo.')
        
        print(f'OBJETIVO: o jogo acaba quando alguém conseguir {OBJETIVO} pontos')

        match input(f'Jogador {ciclo_val[1]}: '):
            case c if c.lower() in ['r','roll','rolar']:

                sup_arr.append(roll())
                print(f'rolou: {sup_arr[-1]}')

                if 1 in sup_arr:
                    sup_arr = []
                    print('Passando para o próximo jogador')

                    ciclo_val = next(ciclo)
                    continue
                
            case c if c.lower() in ['p','pass','passar']:
                sum = 0
                for i in sup_arr:
                    sum+=i

                jogadores[ciclo_val] += sum

                print(f'Jogador {ciclo_val[1]} tem atualmente {jogadores[ciclo_val]}')

                sup_arr = []

                ciclo_val = next(ciclo)
            case _:
                print('Não é uma Opção Válida')
                continue
    if ciclo_val[0] == 'c':
        escolha = choice(['r','p'])
        sleep(1)
        escolhas = {'r':'rolar o dado','p':'passar para o próximo'}

        print(f'Computador {ciclo_val[1]} escolheu {escolhas[escolha]}')
        sleep(1)
        match escolha:
            case 'r':
                sup_arr.append(roll())
                print(f'rolou: {sup_arr[-1]}')

                if 1 in sup_arr:
                    sup_arr = []
                    print('Passando para o próximo jogador')

                    ciclo_val = next(ciclo)
                    continue
            case 'p':
                sum = 0
                for i in sup_arr:
                    sum+=i

                jogadores[ciclo_val] += sum

                print(f'Computador {ciclo_val[1]} tem atualmente {jogadores[ciclo_val]}')

                sup_arr = []

                ciclo_val = next(ciclo)

    valor = any(v >= OBJETIVO for v in jogadores.values())
    
    if valor:
        print('checando')
        for c,v in jogadores.items():
            if v >= OBJETIVO:
                print(f'{"Jogador" if c[0] == "p" else "Computador"} {c[1]} Ganhou o Jogo')
                break