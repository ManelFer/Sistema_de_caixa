def menu():
    print(
        '''
        ====== Sistema Bancario ======

        1 - Depositar saldo na sua conta
        2 - Sacar Saldo da sua conta
        3 - Ver saldo da sua conta
        4 - Novo usuario
        5 - Nova Conta
        6 - Lista contas
        0 - Fechar programa

        ====== Sistema Bancario ======
        '''
    )

def depositar(saldo_conta):
    saldo_a_depositar = int(input("Qual o valor a ser depositado: "))
    saldo_conta += saldo_a_depositar
    print(f"Deposito de {saldo_a_depositar} feito com sucesso")
    print(f"Seu saldo atual é {saldo_conta}")
    return saldo_conta

def sacar(saldo_conta, saldo_banco, saldo_a_sacar):
    while True:
        try:
            saldo_a_sacar = int(input("Digite um valor para saque: "))
            if saldo_a_sacar <= 0:
                print("Valor invalido, digitar um valor real!")
            else:
                break
        except ValueError:
            print("Valor invalido, digite um número: ")

    if saldo_a_sacar > saldo_conta:
        print(f"O valor de {saldo_a_sacar} é superior a quantidade de dinheiro em sua conta bancaria, por favor usar um valor menor")
    elif saldo_a_sacar >= saldo_banco :
        print(f"O valor de {saldo_a_sacar} é superior a quantidade de dinheiro em caixa, por favor usar um valor menor")
    else:
        saldo_conta -= saldo_a_sacar
        print(f'Saque de {saldo_a_sacar} realizado com ucesso')
        print(f'Seu saldo atual é de {saldo_conta}')
    return saldo_conta

def imprimir_extrato(saldo_conta):
    print(f"Seu saldo atual é de {saldo_conta}\n")

def novo_usuario(usuarios):
    cpf = input("Digite seu cpf (Somente números): ")
    usuario = filtro_usuario(cpf, usuarios)
    if usuario:
        print("Já existe um usuario")
        return
    nome = input("Qual o seu nome: ")
    data_nascimento = input("Informe sua data de nascimento(dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logadouro, nro - bairro - cidade): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuario criado com sucesso")
    
def filtro_usuario(cpf, usuarios):
    usuarios_filtros = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtros[0] if usuarios_filtros else None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe CPF do cliente: ")
    usuario = filtro_usuario(cpf, usuarios)
    if usuario:
        print("=== Conta criada com sucesso === ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print(" Usuario não encontrado, criação encerrada! ")

def lista_contas(contas):
    for conta in contas:
        linha = f"""
                    Agência: {conta['agencia']}
                    c/c: {conta['numero_conta']}
                    Titular: {conta['usuario']['nome']}
                """
        print("=" * 100)
        print( linha )

def sair():
    print("==== Encerrado a cessão. Até mais tarde! ====")

def main():
    AGENCIA = "0001"

    saldo_conta = 0
    saldo_banco = 200
    saldo_a_sacar = 0
    usuarios = []
    contas = []
    opcao = -1

    while opcao!= 0:
        menu()
        try:
            opcao = int(input("Escolhar uma das opções: "))
            if opcao not in [0, 1, 2, 3, 4, 5, 6]:
                print("opção invalida")
                continue
        except ValueError:
            print("Opção invalida. Digite um número conforme o sistema indica")

        if opcao == 1: 
            saldo_conta = depositar(saldo_conta)
        elif opcao == 2: 
            saldo_conta = sacar(saldo_conta, saldo_banco, saldo_a_sacar)
        elif opcao == 3: 
            imprimir_extrato(saldo_conta)
        elif opcao == 4:
            novo_usuario(usuarios)
        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == 6:
            lista_contas(contas)
        elif opcao == 0: 
            sair()
        else:
            print("Opção invalida, tentar novamente! \n")

if __name__ == "__main__":
    main()


    
