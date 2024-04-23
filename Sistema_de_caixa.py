saldo_conta = 0
saldo_banco = 200
opcao = -1

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
    opcao = int(input("Escolha um das opções: "))
    if opcao == 1:
        saldo_a_depositar = int(input("Qual o valor a ser depositado: "))
        saldo_conta += saldo_a_depositar
        print(f"Deposito de {saldo_a_depositar} feito com sucesso")
        print(f"Seu saldo atual é {saldo_conta}")
    elif opcao == 2:
        saldo_a_sacar = int(input("Qual o valor pretende sacar: "))
        if saldo_a_sacar > saldo_conta:
            print(f"O valor de {saldo_a_sacar} é superior a quantidade de dinheiro em sua conta bancaria, por favor usar um valor menor")
        elif saldo_a_sacar >= saldo_banco:
            print(f"O valor de {saldo_a_sacar} é superior a quantidade de dinheiro em caixa, por favor usar um valor menor")
        else:
            saldo_conta -= saldo_a_sacar
            print(f"saque de {saldo_a_sacar} realizado com sucesso!")
            print(f"seu saldo atual é de {saldo_conta}")
    elif opcao == 3:
        print(f"Seu saldo atual é de {saldo_conta}\n")
    elif opcao == 0: 
        print("Encerrado a cessão. Até mais tarde!")
    else:
        print("Opção invalida, tentar novamente! \n")
    
    
