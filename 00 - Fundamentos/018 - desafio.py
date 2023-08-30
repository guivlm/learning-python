from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, "pt_BR")
menu = """
============
MEU BANCO
============

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

============
"""

extrato = ""
saldo = 0
LIMITE_NUMERO_SAQUES = 3
LIMITE_POR_SAQUE = 500
saques_realizados = 0

while True:
    opcao_selecionada = input(menu)

    if opcao_selecionada == "d":
        print(f"Depósito selecionado!")
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            print(f"Valor digitado é válido!")
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} em " + \
                datetime.today().strftime('%A, %d/%B/%Y, %H:%M:%S') + "\n"
            print(f"Seu saldo atual é de {saldo:.2f}")
        else:
            print(f"Operação falhou! O valor digitado está incorreto.")

    elif opcao_selecionada == "s":

        print(f"Saque selecionado!")
        valor = float(input("Digite o valor a ser sacado: "))

        pode_ainda_sacar = saques_realizados >= LIMITE_NUMERO_SAQUES
        valor_maior_saldo = valor > saldo

        if valor_maior_saldo:
            print(f"Não é possível sacar o dinheiro por falta de saldo!")
            print(f"Seu saldo atual é de {saldo:.2f}")
        elif valor <= 0:
            print(f"Operação falhou! O valor digitado está incorreto!")
        elif pode_ainda_sacar:
            print(f"Operação falhou! O limite de saques foi excedido!")
            print(f"Utilizado {saques_realizados:.2f} saques")
        elif valor > 0:
            saldo -= valor
            saques_realizados += 1
            extrato += f"Saque: R$ {valor:.2f} em " + \
                datetime.today().strftime('%A, %d/%B/%Y, %H:%M:%S') + "\n"
            print(f"Seu saldo atual é de {saldo:.2f}")

    elif opcao_selecionada == "e":
        print(f"\n ===== Extrato selecionado ===== \n")
        print(f"Não foram realizadas movimentações!" if not extrato else extrato)
        print(f"Seu saldo atual é de {saldo:.2f}")
        print(f"\n ================================ \n")

    elif opcao_selecionada == "q":
        break
    else:
        print("Opção digitada é incorreta. Selecione uma das opções acima!")

# Código do Professor
''''
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
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

'''
