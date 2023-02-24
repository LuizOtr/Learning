
'''
O  índice  é  o  número que  define  onde  está armazenado  um elemento  dentro de uma lista. Quando umprimeiro append() é executado na lista,ele abre a posição 0  (zero)  para  armazenar  o  dado,  quando  ele  for  executado  novamente,  abrirá  a posição  1  (um)  para o  próximo dado,  e  assim  sucessivamente.  Se  armazenarmos trêselementos em uma lista, teremos índices de 0 a 2.

'''

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
    departamentos.append(input('Departamento '))
    resposta = input('Digite \'S\' Para Continuar: ').upper()
print('-'*80)
for indice in range (0, len(equipamentos)):
    print(f'\nEquipamento.....: {indice+1}')
    print(f'Nome............: {equipamentos[indice]}')
    print(f'Valor...........: {valores[indice]}')
    print(f'Serial..........: {seriais[indice]}')
    print(f'Departamento....: {departamentos[indice]}')
print('-'*80)

"""
A estrutura do nosso “for” mudou, agora não estamos trabalhando com base nos  elementos  diretamente,mas,sim,de  acordo  com  o  índice.  Para  a  variável “índice”  que  criamos  no  “for”,  será  atribuído  o  valor  de  0  até  a  quantidade  de elementos  que  existirem  dentro  danossa lista “equipamentos”(função “len()”),  que obviamente será a mesma quantidade de elementos que existirão nas listas: valores, seriais e departamentos, conforme apresentado nas tabelas do tópico anterior,deste mesmo  capítulo.  Com  o  índice  em  mãos,poderemos  recuperar  os  dados  de  todas as nossas listas e a saída dos dados ficará muito mais apresentável.

"""