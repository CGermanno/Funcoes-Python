# -*- coding: utf-8 -*-

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
    print("[2] Criar Conta")
    print("[9] Sair")
    op = int(input("Escolha uma opção: "))
    return op


# ---- AUTENTICAÇÃO / CADASTRO ----------------------------------------------

def logar(usuarios, /):
    """usuarios é position-only: só pode ser passado por posição."""
    print("=== Login ===")
    cpf = input("Informe o CPF: ")
    senha = input("Informe a senha: ")

    for usuario in usuarios:
        if usuario["cpf"] == cpf and usuario["senha"] == senha:
            print(f"\nBem-vindo, {usuario['nome']}!\n")
            return usuario

    print("\nCPF ou senha incorretos.\n")
    return None


def criarUsuario(*, nome, cpf, senha, telefone):
    """Todos os campos são keyword-only: obrigam chamadas nomeadas."""
    return {
        "nome": nome,
        "cpf": cpf,
        "saldo": 0.0,
        "senha": senha,
        "telefone": telefone,
        "cc": cpf,
        "agencia": 33,
        "usuario": len(usuarios) + 1,
        "extrato": ""
    }


# ---- OPERAÇÕES BANCÁRIAS ---------------------------------------------------

def depositar(pessoa, /, *, mostrar_mensagem=True):
    """
    pessoa é position-only.
    mostrar_mensagem é keyword-only (ex.: mostrar_mensagem=False).
    """
    try:
        valor = float(input("Informe o valor: ").replace(",", "."))
    except ValueError:
        print("Valor inválido!")
        return 0.0

    if valor <= 0:
        print("Valor inválido!")
        return 0.0

    pessoa["saldo"] += valor
    pessoa["extrato"] += f"Depósito de R$ {valor:.2f}\n"

    if mostrar_mensagem:
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        print(f"Novo saldo de R$ {pessoa['saldo']:.2f}")

    return valor


def sacar(pessoa, /, *, limite=None, mostrar_mensagem=True):
    """
    pessoa é position-only.
    limite e mostrar_mensagem são keyword-only.
    """
    try:
        valor = float(input("Informe o valor: ").replace(",", "."))
    except ValueError:
        print("Valor inválido!")
        return 0.0

    if valor <= 0:
        print("Valor inválido!")
        return 0.0

    if limite is not None and valor > limite:
        print(f"Limite de saque é R$ {limite:.2f}.")
        return 0.0

    if valor > pessoa["saldo"]:
        print("Saldo insuficiente.")
        return 0.0

    pessoa["saldo"] -= valor
    pessoa["extrato"] += f"Saque de R$ {valor:.2f}\n"

    if mostrar_mensagem:
        print("*Dropando dinheiro...")
        print("*Dinheiro dropado.")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        print(f"Novo saldo de R$ {pessoa['saldo']:.2f}")

    return valor


def extrato(pessoa, /, *, mostrar_saldo=True):
    """pessoa é position-only; mostrar_saldo é keyword-only."""
    print("=== Extrato ===")
    linhas = pessoa["extrato"].rstrip()
    print(linhas if linhas else "(sem movimentações)")
    if mostrar_saldo:
        print(f"\nSaldo atual: R$ {pessoa['saldo']:.2f}")


# ---- LOOP PRINCIPAL ---------------------------------------------------------

op = menu2()

while op != 9:
    if op == 1:
        print("Opção 1 - Logar")
        pessoa = logar(usuarios)  # position-only
        if pessoa is not None:
            op = menu1()
            while op != 9:
                if op == 1:
                    print("Sacar")
                    # exemplo usando keyword-only 'limite'
                    sacar(pessoa, limite=1000.0)
                    op = menu1()

                elif op == 2:
                    print("Depositar")
                    depositar(pessoa)  # mostrar_mensagem default=True
                    op = menu1()

                elif op == 3:
                    print("Extrato")
                    extrato(pessoa, mostrar_saldo=True)
                    op = menu1()

                elif op == 9:
                    print("Saindo...")
                    break

    elif op == 2:
        print("Opção 2 - Criar usuário")
        nome = input("Informe Nome: ")
        cpf = input("Informe CPF: ")
        senha = input("Informe a senha: ")
        telefone = input("Telefone: ")

        pessoa = criarUsuario(  # keyword-only
            nome=nome,
            cpf=cpf,
            senha=senha,
            telefone=telefone
        )
        usuarios.append(pessoa)
        print("Usuário criado com sucesso!")
        print(usuarios)

    else:
        print("Opção inválida!")

    op = menu2()

print("Saindo...")
