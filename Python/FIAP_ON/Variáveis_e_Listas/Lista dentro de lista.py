'''
print  (inventario[0][2])  =>  será  exibido  o  dado  “123456”,  porque  ele retornará  o  elemento  0  da  lista  exterior  e,dentro  desse  elemento,0  irá buscar  o  dado  que  estiver  na  posição  2  da  lista  interior,  ou  seja,  o  serial (elemento 2) da impressora a laser. Outro exemplo:
•print (inventario[1][3]) => irá retornar “DP”, que é o conteúdo da posição 3 do segundo elemento dalista “inventario”.

'''
#Depreciação e exclussão

# Adicionar item no inventario
print('-'*90)
inventario = []
resposta = 'S'
while resposta == 'S':
    equipamento = [input('\nEquipamentos......: '),
        float(input('Valor.............: ')),
        int(input('Número Serial.....: ')),
        input('Depatarmento......: ')]
    inventario.append(equipamento)
    resposta = input('Digite \'S\' para continuar: ').upper()

print('-'*90)

# Exibir dados do inventário
for elemento in inventario:
    print(f'Nome...........: {elemento[0]}')
    print(f'Valor..........: {elemento[1]:.2f}')
    print(f'Serial.........: {elemento[2]}')
    print(f'Departamento...: {elemento[3]}')

print('-'*90)

# Localizar um item no inventario
busca = input('\nDigite o nome do equipamento que deseja buscar: ')
for elemento in inventario:
    if busca == elemento[0]:
        print(f'Valor...: {elemento[1]:.2f}')
        print(f'Serial..: {elemento[2]}')

print('-'*90)

# Depreciar itens no inventario
depreciação = input('\nDigite o nome do equipamento que será depreciado: ')
for elemento in inventario:
    if busca == elemento[0]:
        print(f'Valor antigo...: {elemento[1]:.2f}')
        elemento[1] = elemento [1] * 0.9
        print(f'Novo Valor: {elemento[1]:.2f}')

print('-'*90)

# Excluir um item do inventario
serial = int(input('\nDigite o serial do equipamento que será excluído: '))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

print('-'*90)

# Exibir dados do inventário
for elemento in inventario:
    print(f'Nome..........: {elemento[0]}')
    print(f'Valor.........: {elemento[1]:.2f}')
    print(f'Serial........: {elemento[2]}')
    print(f'Departamento..: {elemento[3]}')

print('-'*90)

# Resumo de valores do inventário
valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores)>0:
    print(f'O equipamento mais caro custa.....: {max(valores):.2f}')
    print(f'O equipamento mais barato custa...: {min(valores):.2f}')
    print(f'O total de equipamento é de.......: {sum(valores):.2f}')

'''
No código acima, criamos uma lista para armazenar somente os valores dos equipamentos, preenchemos a mesma dentro do “for” e,depois de ser preenchida, verificamos se a lista possui ao menos um valor,e,se a condiçãofor verdadeira, as funções abaixo serão executadas:
'''

"""
Observe   o   código   entre   os   dois   arquivos,  “ListasDentroDeListas.py”  e “MultiplasListas.py”, e  procure perceberqual  está  mais  legível  e  mais  simples  de compreender.  
Caso  você  não  tenha  uma  tendência  em  preferir  códigos  mais complexos,  irá  perceber  que  o  código do  arquivo  “ListasDentroDeListas.py” se tornou mais legívelque o anterior.Aúnica regra é saber que,na posição 0,teremos o nome do equipamento;na posição 1,o valor;na posição 2,o serial;e na posição 3,o departamento.
Com o código do arquivo “ListasDentroDeListas.py”,não corremoso risco de exibir  um  dado  de um  equipamento  com  o dado  de outro equipamento  de  maneira equivocada.Isso porque,antes, utilizávamos uma lista para cada dado, de maneira Listas e Funções.

"""