

#listar contas = LC & Listar user = LU
def menu():
    menu = """
    --------------------------------------------

                [D] Depositar
                [S] Sacar
                [E] Extrato
                [C] Criar user
                [CC] Criar conta corrente
                [SECRET] Listar contas
                [SECRET] Listar users  
                [Q] Sair

    --------------------------------------------
    => """
    return input(menu)

def depositar(sal, val, extrato, /):
    if val <= 0: #RETORNA PRO INICIO SE O VALOR MIN NÃO FOR SOLICITADO
            print("\n")
            print("-"*50)
            print("\nValor Inválido\n")
            print("-"*50)
    else:
        sal += val #INCRIMENTA VAL DEPOSITO NO SAQUE
        print(f"\n=== Depósito realizado com sucesso. ===\nSaldo: R$ {sal:.2f}")
        extrato += f"O valor depositado foi de R$ {val:.2f} \n" #FAZ UM 'LOG' NO EXTRATO

    return sal, extrato

def saque(*,sal, val, ext, lim, num_saq, lim_saq):
    #global numero_saques
    if num_saq > lim_saq: #VISUALIZA SE O NUMERO MÁXIMO DE SAQUES JÁ OCORREU
            print("Os 3 saques diários já foram realizados, por favor, retorne amanhã!")

    else: 
        if val > lim: #valor do  saque maior que limite
            print("O valor a ser sacado não pode ser maior que R$ {lim}")

        elif val > sal: #valor do saque maior que saldo
            print("Saldo insuficiente!")
        
        elif val >= 0: #verifica se o valor não é 0 ou negativo
            #numero_saques += 1 #incrementa 1 no contador do saque diario

            sal -= val #retirar o valor do saque do saldo da conta

            print(f"\n{num_saq}º do dia realizado com sucesso!\nSaldo: R$ {sal:.2f}")  #expoe para o usuario

            ext += f"Saque: {num_saq}. Valor sacado: R$ {val:.2f}\n" #armazena no log do extrato
        else:
            print("O valor não pode ser 0 ou negativo.")
        
    return sal, ext

def exibir_extrato(sal ,/,*, ext):
    print("\n=============== EXTRATO ===============")
    print("Não foram realizadas movimentações." if not ext else ext)
    print(f"\nSaldo: R$ {sal:.2f}\n")
    print("========================================")

def criar_usuario(users):
    CPF = input("Informe o CPF (somente números): ")
    cpf_existente = False
    for usuario in users: 
        if usuario["CPF"] == CPF:
            cpf_existente = True
            break

    if cpf_existente:
        print("\nUsuário já existente!")
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        
        usuarios.append({"nome": nome, "dt_nascimento": data_nascimento, "CPF": CPF, "endereco": endereco})
        print("***** Usuário cadastrado com sucesso! *****")

def criar_conta_corrente(agencia, count, users):
    global conta
    CPF = input("Informe o CPF (somente números): ")
    cpf_encontrado = False
    for usuario in users: 
        if usuario["CPF"] == CPF:
            cpf_encontrado = True
            break

    if cpf_encontrado:
        print("\n=== Conta criada com sucesso! ===")
        conta += 1
        return {"agencia": agencia, "numero_conta": count, "usuario": usuario}
    else:
        print("Conta não encontrada! Não será possível criar uma conta.")

def listar_contas(contas):
    for conta in contas:
        acc = f"""\n
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("#" * 50)
        print(acc)

def listar_usuarios(users):
    for user in users:
        us = f"""\n
            Nome:\t\t{user['nome']}
            Data Nascimento:\t{user['dt_nascimento']}
            CPF:\t\t{user['CPF']}
            Endereço:\t\t{user['endereco']}
        """
        print("\n")
        print("-" * 50)
        print(us)
        print("-" * 50)
        print("\n")

def main():
    AGENCIA = "0001";
    conta = 1;

    saldo = 0;
    limite = 500;
    extrato = "";
    numero_saques = 1;
    LIMITE_SAQUES = 3;

    usuarios = []
    contas = []

    while True:

        opcao = menu()

        
        if opcao.upper() == "D":
            valor_deposito = float(input("Informe o valor a ser depositado: R$ ")) #SOLICITA O VALOR DO DEPOSITO
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao.upper() == "S": 
            valor_saque = float(input("Informe o valor a ser sacado: R$ ")) #DISPONIBILIZA O SAQUE
            saldo, extrato = saque(sal= saldo, val= valor_saque, ext= extrato, lim= limite, num_saq= numero_saques, lim_saq= LIMITE_SAQUES)
            numero_saques += 1

        elif opcao.upper() == "E":
            exibir_extrato(saldo, ext= extrato)

        elif opcao.upper() == "C":
            criar_usuario(usuarios)

        elif opcao.upper() == "CC":
            nova_conta = criar_conta_corrente(AGENCIA, conta, usuarios)

            if nova_conta:
                contas.append(nova_conta)    

        elif opcao.upper() == "LC":
            listar_contas(contas)
        
        elif opcao.upper() == "LU":
            listar_usuarios(usuarios)

        elif opcao.upper() == "Q":
            print("Obrigado por usar nosso sistema!")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")             