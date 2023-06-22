from random import choice

jog_pontos = 0
comp_pontos = 0

lista = ['pedra','papel','tesoura','q']
vitoria = {'pedra':'tesoura','tesoura':'papel','papel':'pedra'}

while True:

    jog_escolha = input("Escolha Pedra, Papel ou Tesoura? ou 'Q' para sair do jogo: ").lower()
    comp_escolha = choice(lista[:-1])

    if jog_escolha in lista:

        print(f"sua escolha: {jog_escolha} \ncomputador: {comp_escolha}")
        
        if jog_escolha == 'q':
            print(f"Foi um bom jogo\nVocê fez {jog_pontos} {'ponto' if jog_pontos == 1 else 'pontos'}\nO computador fez {comp_pontos} {'ponto' if comp_pontos == 1 else 'pontos'}")
            break

        if jog_escolha == comp_escolha:
            print("EMPATE!!!")
        elif vitoria[jog_escolha] == comp_escolha:
            print("Você Venceu!")
            jog_pontos+=1
        else:
            print("O Computador Venceu!")
            comp_pontos+=1
    else:
        jog_escolha = input(f"{jog_escolha} não é uma opção válida, tente novamente: ")