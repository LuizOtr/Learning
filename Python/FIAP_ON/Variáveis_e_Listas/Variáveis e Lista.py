'''
Vimos até o momento que as listas armazenam um número indeterminado de dados,  e  essa  é  uma  das  suas  principais  características.  Veremos  a  seguir  um exemplo prático dessaaplicação
'''

# Inventario
print('-'*80)
inventario = []
resposta = 'S'
while resposta == 'S':
    inventario.append(input('Equipamento: '))   # A Função do 'append' e inserir o dado na lista, no caso INVENTARIO.
    inventario.append(float(input('Valor: ')))
    inventario.append(int(input('Número Serial: ')))
    inventario.append(input('Departamento: '))
    resposta = input('Digite \"S\" para continuar: ').upper() # A função 'upper' serve para caso o usuário escreva 's' minusculo.
print('-'*80)

for elemento in inventario:
    print(elemento)
print('-'*80)

'''
No  código  acima,  utilizamos  o  nosso conhecidocomando “while”,que  será responsável por seguir adicionando dados para a nossa lista “inventario” enquanto o usuário digitar “S”.
Perceba  no  códigoacimaque  utilizamos  o  método  append()  para  adicionar novos itens  em  nossa  lista.Podemos  afirmar  que  a  cada  passagem  dentro  do “while”, quatro novos dados serão adicionados na lista (nome do equipamento, valor do equipamento, número serial do equipamento e o nome do departamento onde se encontra o equipamento).

'''