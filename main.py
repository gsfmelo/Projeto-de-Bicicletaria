# Variáveis globais

lista_peca = []
codigo_peca = 0

# Funcões

# Início da função cadastrarPeca
def cadastrarPeca(codigo):
    print('CADASTRE SUA PEÇA') # Apresenta o menu de cadastro de peças
    print('Código da peça: {}'.format(codigo)) # Imprime o código ao qual a peça será cadastrar
    nome = input('Digite o nome da peça: ') # Pede o nome da peça
    fabricante = input('Digite a marca fabricante da peça: ') # Pede fabricante da peça
    valor = int(input('Digite o valor da peça: ')) # Pede valor da peça
    dicionario_peca = {'codigo' : codigo,
                       'nome' : nome,
                       'fabricante' : fabricante,
                       'valor' : valor} # Cria dicionário para os dados
    lista_peca.append(dicionario_peca.copy()) # Adiciona itens ao dicionário
# Final da função cadastrarPecas
def consultarPeca():
    print('CONSULTE SUA(S) PEÇA(S)') # Apresenta menu de consulta
    while True:
        menu_consultar = input('Escolha a opção desejada: \n' +
                               '1 - Consultar todas as peças\n' +
                               '2 - Consultar peças por código\n' +
                               '3 - Consultar peças por fabricante\n' +
                               '4 - Retornar ao menu principal\n' +
                               'Opção escolhida: ')
        if menu_consultar == '1': # Verifica condições e imprime
            print('Opção "Consultar todas as peças" escolhida.')
            for pecas in lista_peca:
                for key, value in pecas.items():
                    print('{}: {}'.format(key, value))
                print('--------------------')
        elif menu_consultar == '2':
            print('Opção "Consultar peças por código" escolhida.')
            codigo_desejado = int(input('Digite o código da peça: '))
            for pecas in lista_peca:
                if pecas['codigo'] == codigo_desejado:
                    for key, value in pecas.items():
                        print('{}: {}'.format(key, value))
                print('--------------------')
        elif menu_consultar == '3':
            print('Opção "Consultar peças por fabricante" escolhida.')
            fabricante_desejado = input('Digite o nome do fabricante da peça: ')
            for pecas in lista_peca:
                if pecas['fabricante'] == fabricante_desejado:
                    for key, value in pecas.items():
                        print('{}: {}'.format(key, value))
                print('--------------------')
        elif menu_consultar == '4': # Volta ao menu principal
            break
# Final da função consultarPecas

# Início da função removerPecas
def removerPeca():
    print('Opção "Remover peças" escolhida') # Avisa que a opção foi escolhida
    codigo_remover = int(input('Digite o código da peça a ser removida: ')) # Pede o código da peça a ser removida
    for pecas in lista_peca:
        if pecas['codigo'] == codigo_remover:
            lista_peca.remove(pecas) # Remove a peça escolhida
            print('Peça removida.') # Imprime peça que foi removida
        print('--------------------')
# Final da função removerPecas

# Programa Principal
while True:
    print('Seja bem-vindo à bicicletaria de Geovanna Melo! RU: 4466904\n')  # Apresentação da bicicletaria
    menu_principal = input('Escolha a opção desejada: \n' +
                           '1 - Cadastrar peça\n' +
                           '2 - Consultar peça(s)\n' +
                           '3 - Remover peça\n' +
                           '4 - Sair\n' +
                           'Opção escolhida: ') # Menu principal do programa
    if menu_principal == '1': # Loop de verificação
        codigo_peca = codigo_peca + 1
        cadastrarPeca(codigo_peca)
    elif menu_principal == '2':
        consultarPeca()
    elif menu_principal == '3':
        removerPeca()
    elif menu_principal == '4': # Fecha o programa
        break
    else: # Pede para digitar um caractere válido
        print('Digite uma opção válida.')
        continue