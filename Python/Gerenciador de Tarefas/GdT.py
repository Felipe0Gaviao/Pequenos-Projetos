import json

try:
    with open('tasks.json', 'r') as fp:
        tasks = json.load(fp)
except (FileNotFoundError,json.decoder.JSONDecodeError):
    print('Tarefas não encontradas, criando novo arquivo vazio')
    with open('tasks.json', 'w') as fp:
        tasks = []
        json.dump(tasks, fp, indent=4)

def adicionar():
    nome=input("Insira um titulo para a Tarefa: ")
    desc=input("Insira uma Descrição: ")
    tasks.append({"n":nome,"d":desc,"c":False})

    print('adicionando...')
    with open('tasks.json','w') as fp:
        json.dump(tasks,fp,indent=4)
    print('adicionado!')

def listar():

    ide = 0

    if len(tasks) == 0:
        print('Não existem tarefas disponíveis, crie algumas antes de tentar listar')
    else:
        for i in tasks:

            nome = i['n']
            desc = i['d']
            c = 'Concluido' if i['c'] == True else 'Não Concluido'
            ide+=1
            print(f'{"-"*(10-len(str(ide)))}{ide}{"-"*(10-len(str(ide)))}\nNome: {nome}\nDescrição: {desc}\n{c}')
        

def concluir():
    index = input('Qual o número da tarefa que deseja concluir? ')

    if len(tasks) == 0:
        print('Não existem tarefas disponíveis, crie algumas antes de tentar concluir')
    else:
        while True:
            try:
                index = int(index)
                break
            except ValueError:
                print(f'{index} não é um número valido')
                index = input('Tente novamente: ')

        with open('tasks.json','w') as fp:
            json.dump(tasks,fp,indent=4)
    
        print('Feito!')

def remover():
    index = input('Qual o número da tarefa que você deseja remover? ')

    while True:
            try:
                index = int(index)
                break
            except ValueError:
                print(f'{index} não é um número valido')
                index = input('Tente novamente: ')

    if len(tasks) == 0:
        print('Não existem tarefas disponíveis, crie algumas antes de tentar remover')
    else:
        teste = input('você realmente quer fazer isso?')
        if teste == 'sim' or teste == 'ss' or teste == 's':

            del tasks[index-1]

            print('removendo...')
            with open('tasks.json','w') as fp:
                json.dump(tasks,fp,indent=4)
            print('removido!')

while True:
    print('Iniciando Gerenciador de Tarefas...')
    print('O que você gostaria de fazer?')

    match input('1/add/adicionar: adicionar uma tarefa na lista\n'+
                '2/list/listar: abrir a lista de tarefas\n'+
                '3/conc/concluir: concluir uma tarefa\n'+
                '4/remo/remover: remover uma tarefa da lista\n'+
                'q: sair do gerenciador\n'+
                ('-'*20)+'\n'):
        case a if a == '1' or a == 'add' or a == 'adicionar':
            adicionar()
        case b if b == '2' or b == 'list' or b == 'listar':
            listar()
        case c if c == '3' or c == 'conc' or c == 'concluir':
            concluir()
        case d if d == '4' or c == 'remo' or d == 'remover':
            remover()
        case 'q':
            quit()
        case _:
            print('não é uma ação válida, tente novamente')
            continue