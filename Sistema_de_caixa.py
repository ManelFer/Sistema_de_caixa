saldo_conta = 0
saldo_banco = 200
opcao = -1

def opcao1():
    global saldo_conta, saldo_banco
    saldo_a_depositar = int(input("Qual o valor a ser depositado: "))
    saldo_conta += saldo_a_depositar
    print(f"Deposito de {saldo_a_depositar} feito com sucesso")
    print(f"Seu saldo atual é {saldo_conta}")

def opcao2():
    global  saldo_conta, saldo_banco
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
        

def opcao3():
    print(f"Seu saldo atual é de {saldo_conta}\n")

def opcao0():
    print("Encerrado a cessão. Até mais tarde!")

print(
    '''
    ====== Sistema Bancario ======

    1 - Depositar saldo na sua conta
    2 - Sacar Saldo da sua conta
    3 - ver saldo da sua conta
    0 - Fechar programa

    ====== Sistema Bancario ======
'''
)

while opcao != 0:
    try:
        opcao = int(input("Escolhar uma das opções: "))
        if opcao not in [0, 1, 2, 3]:
            print("opção invalida")
            continue
    except ValueError:
        print("Opção invalida. Digite um número conforme o sistema indica")

    if opcao == 1: opcao1()
        
    elif opcao == 2: opcao2()
        
    elif opcao == 3: opcao3()
        
    elif opcao == 0: opcao0()
        
    else:
        print("Opção invalida, tentar novamente! \n")
    
    
