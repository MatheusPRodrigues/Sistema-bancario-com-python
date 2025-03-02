# Biblioteca para pausar o tempo da execução do programa
import time
# Bibliotece para limpar a tela do terminal
import os

def verificar_numero_cpf(*, cpf):
    if cpf.isnumeric() == True:
        return True
    else:
        print("Insira somente números!")
        time.sleep(2)
        os.system("cls")
        return False


def verificar_existe_cpf(cpf, usuarios):
    for usuario in usuarios:
        if cpf != usuario['cpf']:
            pass
        else:
            print("Este CPF já existe em nosso banco!")
            time.sleep(2)
            os.system("cls")
            return False

    return True


def criar_usuario(usuarios):
    cpf = input("Insira seu CPF: ")

    if verificar_existe_cpf(cpf, usuarios) == True:
        if verificar_numero_cpf(cpf=cpf) == True:
                nome = input("Insira seu o nome: ")
                data_nasc = input("Insira sua data de nascimento: ")
                logradouro = input("Insira seu logradouro: ")
                nmr = input("Insira o número de sua residência: ")
                bairro = input("Insira o bairro em que você mora: ")
                cidade_estado = input("Insira sua cidade/estado: ")

                usuarios.append({"cpf": cpf, "nome": nome, "data_nasc": data_nasc, "emprego": {"logradouro": logradouro, "nmr": nmr, "bairro": bairro, "cidade/estado": cidade_estado}})
                
                print("Usuário criado com sucesso!")

                time.sleep(2)
                os.system("cls")

                return usuarios

        else:
            pass


def listar_usuarios(usuarios):
    print("=================================================")
    for usuario in usuarios:
        print(f"CPF: {usuario['cpf']}")
        print(f"Nome: {usuario['nome']}")
        print(f"Data de nascimento: {usuario['data_nasc']}")
        print(f"Logradouro: {usuario['emprego']["logradouro"]}")
        print(f"Número da residência: {usuario['emprego']["nmr"]}")
        print(f"Bairro: {usuario['emprego']["bairro"]}")
        print(f"Cidade/Estado: {usuario['emprego']["cidade/estado"]}")
        print("=================================================")

    if len(usuarios) == 0:
        print("Não há usuários registrados!")
        time.sleep(2)
        os.system("cls")

    os.system("pause")
    os.system("cls")
        

def selecionar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if cpf == usuario['cpf']:
            return usuario['nome']
    
    else:
        print("Esse CPF ainda não foi cadastrado!")
        time.sleep(2)
        os.system("cls")


def criar_conta(agencia, numero, usuarios, contas):
    cpf = input("Insira seu CPF: ")
    
    if verificar_numero_cpf(cpf=cpf) == True:
        usuario = selecionar_usuario(cpf, usuarios)
        #print(usuario)

        if usuario != None:
            contas.append({"agencia": agencia, "numero_da_conta": numero, "usuario": usuario})

            print("Conta corrente criada com sucesso!")

            time.sleep(2)
            os.system("cls")
            
            return contas

    else:
        pass 


def listar_contas(contas):
    print("=================================================")
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Nº Conta corrente: {conta['numero_da_conta']}")
        print(f"Titular: {conta['usuario']}")
        print("=================================================")

    if len(contas) == 0:
        print("Não há contas corrente registradas!")
        time.sleep(2)
        os.system("cls")

    os.system("pause")
    os.system("cls")


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


def extrato(saques, /, *, depositos):
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

# ====== MENU ======
def main():
    # Váriaveis principais do programa
    global indicador_limite_saque
    LIMITE_SAQUE = 3
    N_AGENCIA = '0001'  

    lista_deposito = []
    lista_saques = []
    usuarios = []
    numero_da_conta = 1
    contas = []

    menu = """
        ====== Seja bem-vindo! ======

            [nu] -> Novo Usuário
            [lu] -> Listar Usuários
            [cc] -> Criar Conta Corrente
            [lc] -> Listar Contas Corrente
            [d] -> Depósito
            [s] -> Saque
            [e] -> Extrato
            [q] -> Sair

    """

    while True:
        print(menu)

        opcao = input("-> ")

        # Novo usuário
        if opcao == "nu":
            criar_usuario(usuarios)
        
        # Listar usuário
        elif opcao == "lu":
            listar_usuarios(usuarios)
            
        # Criar conta corrente
        elif opcao == "cc":
            numero_da_conta = len(contas) + 1
            criar_conta(N_AGENCIA, numero_da_conta, usuarios, contas)

        # Listando contas corrente
        elif opcao == "lc":
            listar_contas(contas)

        # Depósito
        elif opcao == "d":
            deposito = float(input("Insira o valor que deseja depositar: "))
            depositar(deposito, lista_deposito)
            # os.system("cls") serve para executar o comando cls no sistema, assim limpando o conteúdo do terminal
            os.system("cls")

        elif opcao == "s":
            #print("Saque")

            # Verificação do limite diário
            if indicador_limite_saque <= LIMITE_SAQUE:
                saque = float(input("Insira o valor que deseja sacar: "))
                sacar_dinheiro(saque=saque, lista=lista_saques)
                os.system("cls")
            else:
                print("Máximo de saques diários atingido!")
                time.sleep(2)
                os.system("cls")

        elif opcao == "e":
            extrato(lista_saques, depositos=lista_deposito)
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


# Váriavel global de saque
saldo = 500
indicador_limite_saque = 1

main()