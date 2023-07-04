print("Bem vindo ao Quizz")

iniciar_jogo = input("Você gostaria de jogar? ")
pontos = 0
q_contar = 0

if iniciar_jogo.lower() == "sim":
    print("Okay, então vamos começar o jogo")
else:
    quit()

def questao(pergunta,resposta):

    global pontos, q_contar

    q_contar += 1

    user = input(f'{pergunta}\n')
    resposta = str(resposta)

    if user.lower() == resposta.lower():
        print(f'Acertou! A resposta é {resposta}')
        pontos += 1
    else:
        print(f'Errou! A resposta certa era {resposta}')

questao("Em que ano o Titanic afundou no Oceano Atlântico em 15 de abril, em sua viagem inaugural de Southampton?","1912")
questao("Qual é o título do primeiro filme de Carry On feito e lançado em 1958?","Sargento")
questao("Qual é o nome da maior empresa de tecnologia da Coréia do Sul?","Samsung")
questao("Qual cantor liderou o grupo pop dos anos 1970 Showaddywaddy?","Dave Bartram")
questao("Qual agora famoso chef de TV começou a cozinhar aos oito anos de idade no pub de seus pais, 'The Cricketers, em Clavering, Essex?","Jamie Oliver")
questao("Qual jogador de dardos holandês venceu o Campeonato do Mundo BDO de 2012 no Lakeside Country Club, Frimley Green, em 15 de janeiro?","Kist Cristão")
questao("Qual metal foi descoberto por Hans Christian Oersted em 1825?","alumínio")
questao("Qual é a capital de Portugal?","Lisboa")
questao("Quantas respirações o corpo humano toma diariamente?","20,000 diariamente")
questao("Quem foi o primeiro-ministro da Grã-Bretanha de 1841 a 1846?","Robert Peel")
print(f"você acertou {pontos} Questões!")
print(f"Acertou {(pontos/q_contar)*100}% das questões")