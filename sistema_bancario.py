def menu():
    texto_menu = f'''
        =========== MENU ===========

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [0] Sair

    => '''
    
    opcao = int(input(texto_menu.lstrip()))

    return opcao

saldo = 0
extrato = []
numero_saques = 0
LIMITE_POR_SAQUE = 500
LIMITE_SAQUES = 3

while True:

    operacao = -1

    # escolha da operação:
    operacao = menu()

    # depositar:
    if operacao == 1:
        valor = 0
        while valor <= 0:
            valor = float(input('Quanto você deseja depositar? '))
            if valor <= 0:
                print('Por favor, escolha um valor válido.')

        saldo += valor
        extrato.append(f'Depósito:\t+ R$ {valor:.2f}\n')
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    # sacar:
    elif operacao == 2:
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saques:
            print('Você já excedeu o limite de saques do dia.')

        else:
            valor = float(input('Quanto deseja sacar? '))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > LIMITE_POR_SAQUE

            if excedeu_saldo:
                print('Operação falhou! Você não tem saldo suficiente.')
            
            elif excedeu_limite:
                print('Operação falhou! O valor desejado de saque excede o limite.')
            
            elif valor > 0:
                saldo -= valor
                extrato.append(f'Saque:\t\t- R$ {valor:.2f}\n')
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            
            else:
                print('Operação falhou! O valor informado é inválido.')
    
    # extrato:
    elif operacao == 3:
        print('\n========== EXTRATO ==========')
        if not extrato:
            print('Não foram realizadas movimentações.')
        else:
            for movimentacao in extrato:
                print(movimentacao, end='')
        
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('\n=============================')

    # sair:
    elif operacao == 0:
        break
    
    # operação inválida:
    else:
        print('Operação inválida! Por favor, selecione novamente a operação desejada.')