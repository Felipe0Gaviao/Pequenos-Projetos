#senha_mestra = input("Qual é a senha? ")

def ver():

    print("abrindo arquivo...")
    with open('contas.txt','r') as file:
        for lines in file.readlines():
            info = lines.rstrip('\n')
            us,sn = info.split(' | ')
            print(f"{us}, {sn}")

def add():
    nome = input("Nome da conta:\n")
    senha = input("Senha:\n")

    print("adicionando...")
    with open('contas.txt','a') as file:
        file.write(f"Nome: {nome} | Senha: {senha}\n")
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