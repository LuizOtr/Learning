print('\n=====DESAFIO 09=====')
print('\nFaça um programa que leia um número inteiro e mostre a sua tabuada.')
print('-' *68)
n1=int(input('\nDigite um número: '))

aux = 0
print('-' *20)
print(f'Tabuada de {n1}')
print("-" * 20 )
while(aux <=10):
    n2=aux*n1
    print(f'{aux} x {n1} = {n2} ')
    aux=aux +1
print('-' *20)