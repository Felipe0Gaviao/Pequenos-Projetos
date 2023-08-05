import random

def digito(x:str):
    try: x=int(x);x = digito(input("tem que ser um número maior que 0: ")) if x<=0 else int(x);return x
    except: print(f"{x} não é um número"); x = digito(input("Tente novamente: "));return x

numero_maximo = digito(input("digite um número: "))
numero_aleatorio = random.randint(0,numero_maximo)
tentativas = 0
escolha = digito(input(f"Chute um número entre 0 e {numero_maximo}: "))

while escolha != numero_aleatorio:
    tentativas += 1
    print(f"Errou!")
    print(f"Dica: você está acima do número" if escolha>numero_aleatorio else f"Dica: você está abaixo do número")

    escolha = digito(input("Tente novamente: "))
else:
    print(f"Parabéns, você acertou!")
    print(f"você tentou chutar {tentativas} {'vez' if tentativas == 1 else 'vezes'} antes de acertar")