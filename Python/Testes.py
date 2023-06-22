lista = ['pedra','papel','tesoura']
escolha = input("escolha:").lower

match lista:
    case lista if escolha in lista:
        print('tem')
    case _:
        print('não tem')