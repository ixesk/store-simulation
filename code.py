# Dados dos items da loja
Camaro = {'Nome': 'Camaro', 'Modelo': 'A12', 'Ano': 2010, 'Motor': 'V8', 'Preço': 350_000}
Jeep = {'Nome': 'Jeep', 'Modelo': 'Road 20', 'Ano': 2020, 'Motor': 'V8', 'Preço': 800_000}
Ferrari = {'Nome': 'Ferrari', 'Modelo': 'Italia', 'Ano': 2019, 'Motor': 'V12', 'Preço': 1_200_000}
Porsche = {'Nome': 'Porsche', 'Modelo': 'C9', 'Ano': 2011, 'Motor': 'V12', 'Preço': 750_000}
Corvette = {'Nome': 'Corvette', 'Modelo': 'Z06', 'Ano': 2011, 'Motor': 'V8', 'Preço': 500_000}

# Entrada
comando = input('Pesquisar: ')

carrinho = []  # Os dados nesta lista serão perdidos se o programa for reiniciado.

# Processamento/Saída
while comando != 'sair':
    comando = input('Pesquisar: ')
   
    if comando == 'Camaro':
        for chave, valor in Camaro.items():
            print(f'{chave}: {valor}')
        quest = input(f'Deseja adicionar {comando} ao carrinho? ')
        if quest == 'Sim':
            carrinho.append(Camaro)
            print('Adicionado ao carrinho.')
        else:
            pass

    if comando == 'Jeep':
        for chave, valor in Jeep.items():
            print(f'{chave}: {valor}')
        quest = input(f'Deseja adicionar {comando} ao carrinho? ')
        if quest == 'Sim':
            carrinho.append(Jeep)
            print('Adicionado ao carrinho.')
        else:
            pass

    if comando == 'Ferrari':
        for chave, valor in Ferrari.items():
            print(f'{chave}: {valor}')
        quest = input(f'Deseja adicionar {comando} ao carrinho? ')
        if quest == 'Sim':
            carrinho.append(Ferrari)
            print('Adicionado ao carrinho.')
        else:
            pass

    if comando == 'Porsche':
        for chave, valor in Porsche.items():
            print(f'{chave}: {valor}')
        quest = input(f'Deseja adicionar {comando} ao carrinho? ')
        if quest == 'Sim':
            carrinho.append(Porsche)
            print('Adicionado ao carrinho.')
        else:
            pass

    if comando == 'Corvette':
        for chave, valor in Corvette.items():
            print(f'{chave}: {valor}')
        quest = input(f'Deseja adicionar {comando} ao carrinho? ')
        if quest == 'Sim':
            carrinho.append(Corvette)
            print('Adicionado ao carrinho.')
        else:
            pass

    if comando == 'carrinho':
        print(carrinho)
        quest = input('Deseja remover algum item? (Informe o nome do Item) ')

    if comando == 'sair':
        break

print(carrinho)
print('Saiu da loja com sucesso.')
