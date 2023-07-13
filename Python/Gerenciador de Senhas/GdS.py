from cryptography.fernet import Fernet

def criar_chave():
    chave = Fernet.generate_key()
    with open("Python\Gerenciador de Senhas\chave.key", "wb") as arc_chave:
        arc_chave.write(chave)

def carregar_chave():
    arc = open("Python\Gerenciador de Senhas\chave.key", "rb")
    ch = arc.read()
    arc.close
    return ch


chave_m = carregar_chave()
fer = Fernet(chave_m)


def ver():

    print("abrindo arquivo....git")
    with open('Python\Gerenciador de Senhas\contas.txt','r') as file:
        for lines in file.readlines():
            info = lines.rstrip('\n')
            us,sen = info.split(' | ')
            print(f"Conta: {us}, Senha: {fer.decrypt(sen.encode()).decode()}")

def add():
    us = input("Nome da conta:\n")
    sn = input("Senha:\n")

    print("adicionando...")
    with open('Python\Gerenciador de Senhas\contas.txt','a') as file:
        file.write(f"{us} | {fer.encrypt(sn.encode()).decode()}\n")
    print("adicionando!")
    

while True:
    metodo = input(f"O que gostaria de fazer?\n(1) Ver senhas salvas.\n(2) Adicionar nova senha.\n(q) Sair.\n{'-'*20}\n").lower()

    match metodo:
        case '1' | 'ver':
            ver()
        case '2' | 'adicionar' | 'add':
            add()
        case 'q':
            print(f"{'-'*20}\naté outra hora")
            break
        case _:
            print(f"{metodo} não é um método valido, tente novamente...\n{'-'*20}")
            continue