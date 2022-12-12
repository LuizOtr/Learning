print('-'*80)
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 'S'

while resposta == 'S':
    equipamentos.append(input('Equipamentos: '))
    valores.append(float(input('Valor: ')))
    seriais.append(int(input('Numero Serial: ')))
    departamentos.append(input('Departamento: '))
    resposta = input('Digite \'S\' Para Continuar: ').upper()
print('-'*80)
for indice in range (0, len(equipamentos)):
    print(f'\nEquipamento.....: {indice+1}')
    print(f'Nome............: {equipamentos[indice]}')
    print(f'Valor...........: {valores[indice]}')
    print(f'Serial..........: {seriais[indice]}')
    print(f'Departamento....: {departamentos[indice]}')
print('-'*80)

busca = input('\nDigite o nome do equipamento que deseja buscar: ')
for indice in range (0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print(f'\nEquipamento.....: {indice+1}')
        print(f'Nome............: {equipamentos[indice]}')
        print(f'Valor...........: {valores[indice]}')
        print(f'Serial..........: {seriais[indice]}')
        print(f'Departamento....: {departamentos[indice]}')
print('-'*80)

"""
Observamos  acima  que,dentro do “for”,montamos  uma  tomada  de  decisão simples, cuja função será comparar o conteúdo da variável “busca” com todos os elementos que estiverem armazenados dentro da lista “equipamentos”. Quando ele encontrar  um  valor  igual,  irá  exibir,então,o  valor  e  o  número  serial  desseequipamento.

"""