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




def dados():

    print("=== Criar Usuário ===")
    nome = input("Informe Nome: ")
    cpf = input("Informe CPF: ")
    senha = input("Informe a senha")
    telefone = input("Telefone: ")
    return nome, cpf, senha, telefone

def criarUsuario(*, nome, cpf, senha, telefone):

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