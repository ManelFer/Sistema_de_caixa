class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.agencia = "0001"
        self.saldo_banco = 200

    def menu(self):
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

    def depositar(self, conta):
        saldo_a_depositar = int(input("Qual o valor a ser depositado: "))
        conta.saldo += saldo_a_depositar
        print(f"Deposito de {saldo_a_depositar} feito com sucesso")
        print(f"Seu saldo atual é {conta.saldo}")
        return conta

    def sacar(self, conta):
        while True:
            try:
                saldo_a_sacar = int(input("Digite um valor para saque: "))
                if saldo_a_sacar <= 0:
                    print("Valor invalido, digitar um valor real!")
                else:
                    break
            except ValueError:
                print("Valor invalido, digite um número: ")

        if saldo_a_sacar > conta.saldo:
            print(f"O valor de {saldo_a_sacar} é superior a quantidade de dinheiro em sua conta bancaria, por favor usar um valor menor")
        elif saldo_a_sacar >= self.saldo_banco:
            print(f"O valor de {saldo_a_sacar} é superior a quantidade de dinheiro em caixa, por favor usar um valor menor")
        else:
            conta.saldo -= saldo_a_sacar
            print(f'Saque de {saldo_a_sacar} realizado com ucesso')
            print(f'Seu saldo atual é de {conta.saldo}')
        return conta

    def imprimir_extrato(self, conta):
        print(f"Seu saldo atual é de {conta.saldo}\n")

    def novo_usuario(self):
        cpf = input("Digite seu cpf (Somente números): ")
        usuario = self.filtro_usuario(cpf)
        if usuario:
            print("Já existe um usuario")
            return
        nome = input("Qual o seu nome: ")
        data_nascimento = input("Informe sua data de nascimento(dd-mm-aaaa): ")
        endereco = input("Informe seu endereço (logadouro, nro - bairro - cidade): ")

        self.usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("Usuario criado com sucesso")

    def filtro_usuario(self, cpf):
        usuarios_filtros = [usuario for usuario in self.usuarios if usuario["cpf"] == cpf]
        return usuarios_filtros[0] if usuarios_filtros else None

    def nova_conta(self):
        cpf = input("Informe CPF do cliente: ")
        usuario = self.filtro_usuario(cpf)
        if usuario:
            print("=== Conta criada com sucesso === ")
            numero_conta = len(self.contas) + 1
            return {"agencia": self.agencia, "numero_conta": numero_conta, "usuario": usuario}
        print(" Usuario não encontrado, criação encerrada! ")

    def lista_contas(self):
        for conta in self.contas:
            linha = f"""
                        Agência: {conta['agencia']}
                        c/c: {conta['numero_conta']}
                        Titular: {conta['usuario']['nome']}
                    """
            print("=" * 100)
            print(linha)

    def sair(self):
        print("==== Encerrado a cessão. Até mais tarde! ====")

class Conta:
    def __init__(self, saldo=0):
        self.saldo = saldo

def main():
    banco = Banco()
    opcao = -1

    while opcao != 0:
        banco.menu()
        try:
            opcao = int(input("Escolhar uma das opções: "))
            if opcao not in [0, 1, 2, 3, 4, 5, 6]:
                print("opção invalida")
                continue
        except ValueError:
            print("Opção invalida. Digite um número conforme o sistema indica")

        if opcao == 1:
            if not banco.contas:
                print("sem contas")
                while True:
                    resposta = input("Digite 'v' para Verificar se tem conta ativa ou digite 'n' para Não ver conta ativa: ").lower()
                    if resposta == 'v':
                        conta = banco.nova_conta()
                        if conta:
                            banco.contas.append(conta)
                        break
                    elif resposta == 'n':
                        print("=== ok, até mais tarde ===")
                        break
                    else: print("=== Resposta invalida ===")
            else:
                conta = banco.contas[0]  # assume que a primeira conta é a atual
                banco.depositar(conta)
        elif opcao == 2:
           conta = banco.contas[0]  # assume que a primeira conta é a atual
           banco.sacar(conta)
        elif opcao == 3:
           conta = banco.contas[0]  # assume que a primeira conta é a atual
           banco.imprimir_extrato(conta)
        elif opcao == 4:
            banco.novo_usuario()
        elif opcao == 5:
            conta = banco.nova_conta()
            if conta:
                banco.contas.append(conta)

        elif opcao == 6:
            banco.lista_contas()
        elif opcao == 0:
            banco.sair()
        else:
            print("Opção invalida, tentar novamente! \n")

if __name__ == "__main__":
    main()
