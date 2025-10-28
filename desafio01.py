usuarios = []


def menu1():
    print("==== MENU ====")
    print("[1] Sacar")
    print("[2] Depositar")
    print("[3] Extrato")
    print("[9] Sair")
    op = int(input("Escolha uma opção: "))
    return op


def menu2():
    print("==== MENU ====")
    print("[1] Logar")
    print("[2] Cricar Conta")
    print("[9] Sair")

    op = int(input("Escolha uma opção: "))
    return op


def logar():
    print("=== Login ===")
    cpf = input("Informe o CPF: ")
    senha = input("Informe a senha: ")

    # Percorre todos os usuários cadastrados
    for usuario in usuarios:
        if usuario["cpf"] == cpf and usuario["senha"] == senha:
            print(f"\nBem-vindo, {usuario['nome']}!\n")
            return usuario  # retorna o usuário logado

    print("\nCPF ou senha incorretos.\n")
    return None  # login falhou


def criarUsuario():
    print("=== Criar Usuário ===")
    nome = input("Informe Nome: ")
    cpf = input("Informe CPF: ")
    senha = input("Informe a senha")
    telefone = input("Telefone: ")

    pessoa = {
        "nome": nome,
        "cpf": cpf,
        "saldo": 0,
        "senha": senha,
        "telefone": telefone,
        "cc": cpf,
        "agencia": 33,
        "usuario": len(usuarios) + 1, 
        "extrato": ""
        }
    
    usuarios.append(pessoa)

    print("Usuário criado com sucesso!")
    return menu2


def depositar(pessoa):
    #deposita valor no saldo do cliente
    valor = 0
    valor = float(input("Informe o valor: "))

    #salva acao em 'extrato = ""'
    pessoa["saldo"] += valor    
    pessoa["extrato"] += f"Deposito de: {valor} \n"

    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    print(f"Novo saldo de R$ {pessoa['saldo']:.2f}")

    return valor


def sacar(pessoa):
    #subtrair valor do saldo do cliente
    valor = 0
    valor = float(input("Informe o valor"))

    pessoa["saldo"] -= valor
    pessoa["extrato"] += f"Saque de: {valor} \n"

    print("*Dropando dinheiro...")
    print("*Dinheiro dropado.")
    print(f"DepóSaque de R$ {valor:.2f} realizado com sucesso.\n")
    print(f"Novo saldo de R$ {pessoa['saldo']:.2f}")
    return valor


def extrato(pessoa):
    print("=== Extrato ===")
    print(pessoa["extrato"])
    print(f"Saldo atual: R$ {pessoa['saldo']:.2f}")




op = menu2()

while op != 9: 
    if op == 1:
        print("Opção 1 - Logar")
        pessoa = logar()
        if pessoa != None:
            print("deucerto")
            op = menu1()
            while op != 9:
                if op == 1:
                    print("Sacar")
                    sacar(pessoa)
                    op = menu1()


                elif op == 2:
                    print("Depositar")
                    depositar(pessoa)
                    op = menu1()


                elif op == 3:
                    print("Extrato")

                    extrato(pessoa)

                    op = menu1()


                elif op == 9:
                    print("Saindo...")
                    break

    elif op == 2:
        print("Opcao 2 - criar usuario")
        criarUsuario()
        print(usuarios)
    else:
        print("Opção inválida!")

### 

    op = menu2()


print("Saindo...")


