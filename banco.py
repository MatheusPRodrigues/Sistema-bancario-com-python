# Biblioteca para pausar o tempo da execução do programa
import time

# Bibliotece para limpar a tela do terminal
import os

def valor_negativo(x):
    if x > 0:
        return True
    
    else:
        return False


def depositar(deposito, lista):
    global saldo

    # Verifica se o valor é negativo ou não
    if valor_negativo(deposito) == True:
        print("Valor aceito!")
        time.sleep(1)

        lista.append(deposito)
    
        saldo += deposito

        return saldo, lista


    else:
        print("Não é possível depositar valores menores ou igual a zero! Tente novamente!")
        time.sleep(2)


def sacar_dinheiro(saque, lista):
    global saldo
    global indicador_limite_saque
        
    # Verificação de número negativo
    if valor_negativo(saque) == True:

        # Verificação se saldo é suficiente
        if saque <= saldo:

            if saque <= 500:
                print("Saque será realizado!")
                time.sleep(1)

                lista.append(saque)

                saldo -= saque
                indicador_limite_saque += 1

                return saldo, lista

            else:
                print("Valor máximo para saque é R$500,00! Tente novamente!")
                time.sleep(2)

        else:
            print("Não será possível sacar por falta de saldo!")
            time.sleep(2)

    else:
        print("Não é possível depositar valores menores ou igual a zero! Tente novamente!")
        time.sleep(2)


def extrato(depositos, saques):
    global saldo

    txt = "============== EXTRATO ==============\n"

    num_depositos = len(depositos)
    num_saques = len(saques)

    if num_depositos == 0 and num_saques == 0:
        txt += "Não foram realizadas movimentações!\n"

    else:

        if num_depositos == 0:
            txt += "Nenhum depósito realizado até o momento\n"

        else:
            i = 0

            for i in range(0, num_depositos):
                txt += f"{i + 1}º Depósito, valor: R${depositos[i]:.2f}\n"

        txt += "=====================================\n"

        if num_saques == 0:
            txt += "Nenhum saque realizado até o momento\n"

        else:
            j = 0

            for j in range(0, num_saques):
                txt += f"{j + 1}º Saque, valor: R${saques[j]:.2f}\n"

    txt += "=====================================\n"
    txt += f"Saldo:                    R${saldo:.2f}\n"
    txt += "====================================="

    # Saída do extrato
    print(txt)
    os.system("pause")


# Váriaveis principais do programa
saldo = 500
lista_deposito = []
lista_saques = []
indicador_limite_saque = 1
LIMITE_SAQUE = 3



# ====== MENU ======
menu = """
    ====== Seja bem-vindo! ======

        [d] -> Depósito
        [s] -> Saque
        [e] -> Extrato
        [q] -> Sair

"""

while True:
    print(menu)

    opcao = input("-> ")

    #Depósito
    if opcao == "d":
        deposito = float(input("Insira o valor que deseja depositar: "))
        depositar(deposito, lista_deposito)
        # os.system("cls") serve para executar o comando cls no sistema, assim limpando o conteúdo do terminal
        os.system("cls")

    elif opcao == "s":
        #print("Saque")

        # Verificação do limite diário
        if indicador_limite_saque <= LIMITE_SAQUE:
            saque = float(input("Insira o valor que deseja sacar: "))
            sacar_dinheiro(saque, lista_saques)
            os.system("cls")
        else:
            print("Máximo de saques diários atingido!")
            time.sleep(2)
            os.system("cls")

    elif opcao == "e":
        extrato(lista_deposito, lista_saques)
        os.system("cls")

    elif opcao == "q":
        # Paro o sistema
        print("Agradeçemos por usar nosso sistema!")
        time.sleep(2)
        os.system("cls")
        break
    
    else:
        print("Operação inválida! Por favor selecione novamente a operação desejada.")
        time.sleep(2)
        os.system("cls")