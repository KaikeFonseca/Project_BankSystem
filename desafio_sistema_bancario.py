menu = """
--------------------------------------------

            [D] Depositar
            [S] Sacar
            [E] Extrato
            [Q] Sair

--------------------------------------------
=> """

saldo = 0;
limite = 500;
extrato = "";
numero_saques = 0;
LIMITE_SQUES = 3;

while True:

    opcao = input(menu)
    
    if opcao.upper() == "D":
        valor_deposito = float(input("Informe o valor a ser depositado: R$ ")) #SOLICITA O VALOR DO DEPOSITO
        
        if valor_deposito <= 0: #RETURNA PRO INICIO SE O VALOR MIN NÃO FOR SOLICITADO
            print("O valor a ser depositado deve ser maior que R$ 0,00")
            continue
        
        saldo += valor_deposito #INCRIMENTA VAL DEPOSITO NO SAQUE
        print(f"Depósito realizado com sucesso.\nSaldo: R$ {saldo:.2f}")
        extrato += f"O valor depositado foi de R$ {valor_deposito:.2f} \n" #FAZ UM 'LOG' NO EXTRATO

    elif opcao.upper() == "S": 
        if numero_saques >= 3: #VISUALIZA SE O NUMERO MÁXIMO DE SAQUES JÁ OCORREU
            print("Os 3 saques diários já foram realizados, por favor, retorne amanhã!")
            continue

        valor_saque = float(input("Informe o valor a ser sacado: R$ ")) #DISPONIBILIZA O SAQUE

        if valor_saque > 500:
            print("O valor a ser sacado não pode ser maior que R$ 500,00")
            continue

        if valor_saque > saldo:
            print("Saldo insuficiente!")
            continue
        
        if valor_saque >= 0: #verifica se o valor não é 0 ou negativo
            numero_saques += 1 #incrementa 1 no contador do saque diario

            saldo -= valor_saque #retirar o valor do saque do saldo da conta

            print(f"\n{numero_saques}º do dia realizado com sucesso!\nSaldo: R$ {saldo:.2f}")  #expoe para o usuario

            extrato += f"Saque: {numero_saques}. Valor sacado: R$ {valor_saque:.2f}\n" #armazena no log do extrato
        else:
            print("O valor não pode ser 0 ou negativo.")
            continue
    
    elif opcao.upper() == "E":

        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print("========================================")
    
    elif opcao.upper() == "Q":
        print("Obrigado por usar nosso sistema!")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
              