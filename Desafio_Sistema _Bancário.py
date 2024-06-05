from colorama import Fore, Style

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 4

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print(Fore.RED + "Operação falhou! O valor informado é inválido." + Style.RESET_ALL)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(Fore.RED + "Operação falhou! Você não tem saldo suficiente." + Style.RESET_ALL)

        elif excedeu_limite:
            print(Fore.RED + "Operação falhou! O valor do saque excede o limite." + Style.RESET_ALL)

        elif excedeu_saques:
            print(Fore.RED + "Operação falhou! Número máximo de saques excedido." + Style.RESET_ALL)

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print(Fore.RED + "Operação falhou! O valor informado é inválido." + Style.RESET_ALL)

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")