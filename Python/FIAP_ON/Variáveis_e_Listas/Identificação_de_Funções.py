
print('-'*90)
def preencherInventario(lista):
    resposta = 'S'
    while resposta == 'S':
        equipamento = [input('\nEquipamentos......: '),
            float(input('Valor.............: ')),
            int(input('Número Serial.....: ')),
            input('Depatarmento......: ')]
        lista.append(equipamento)
        resposta = input('Digite \'S\' para continuar: ').upper()
print('-'*90)

# Exibir dados do inventário
def exibirInventario (lista):
    for elemento in lista:
        print(f'Nome...........: {elemento[0]}')
        print(f'Valor..........: {elemento[1]:.2f}')
        print(f'Serial.........: {elemento[2]}')
        print(f'Departamento...: {elemento[3]}')

print('-'*90)

# Localizar um item no inventario
def localizarPorNome (lista):
    busca = input('\nDigite o nome do equipamento que deseja buscar: ')
    for elemento in lista:
        if busca == elemento[0]:
            print(f'Valor...: {elemento[1]:.2f}')
            print(f'Serial..: {elemento[2]}')

print('-'*90)

# Depreciar itens no inventario
def depreciarPorNome (lista, porc):
    depreciacao = input('\nDigite o nome do equipamento que será depreciado: ')
    for elemento in lista:
        if depreciacao == elemento[0]:
            print(f'Valor antigo...: {elemento[1]:.2f}')
            elemento[1] = elemento [1] * (1-porc/100)
            print(f'Novo Valor: {elemento[1]:.2f}')

print('-'*90)

# Excluir um item do inventario
def excluirPorSerial(lista):
    serial = int(input('\nDigite o serial do equipamento que será excluído: '))
    def elemento (lista):
        if elemento[2] == serial:
            lista.remove(elemento)

print('-'*90)

# Exibir dados do inventário
def exibirDados(lista):
    for elemento in lista:
        print(f'Nome..........: {elemento[0]}')
        print(f'Valor.........: {elemento[1]:.2f}')
        print(f'Serial........: {elemento[2]}')
        print(f'Departamento..: {elemento[3]}')

print('-'*90)

# Resumo de valores do inventário
def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores)>0:
        print(f'O equipamento mais caro custa.....: {max(valores):.2f}')
        print(f'O equipamento mais barato custa...: {min(valores):.2f}')
        print(f'O total de equipamento é de.......: {sum(valores):.2f}')
