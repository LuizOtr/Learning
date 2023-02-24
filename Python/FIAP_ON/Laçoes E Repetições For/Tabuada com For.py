print('-'*80)

tabuada = int(input('Digi8te um numero para exibir a tabuada: '))
print(f'Tabuada do número,{tabuada}')
for valor in range(1,11,1):
    print(str(tabuada) + 'x' + str(valor) + '=' + str((tabuada*valor)))

print('-'*80)

"""
Repare que,para multiplicarmos os dois valores,utilizamos o operador “*”. No range(),  definimos  que  os  valores  gerados  deverão  estar  entre 1  e  11,  com incremento de 1 em 1. O “11” foi definido porqueele não se inclui no range, ou seja, quando chegar em 11 ele para,portanto,não executará mais o laço quando atingir este valor.Preparamos muitos códigos,mas muita coisa ainda vem pela frente. Procure refazer,  principalmente,os  desafios  deste  capítulo,antes  de  entrar  no  próximo, quando,então,explicaremos   sobre   listas,   uma   das   principais   estruturas   de armazenamento temporário do Python.

"""