from math import trunc
print('')
print('=====DESAFIO 16=====')
print('-'*96)
print('Crie um programa que leia um número real pelo teclado e mostre na sua tela a sua porção inteira!')
print('-'*96)
print('Ex: Digite um número:6.127'
      '\nO número 6.127 tem a parte inteira 6.'
      '\nDICA: ler todas as funções do modulo da classe math!')
print('-'*96)

n1=float(input('Digite um Número: '))
n2=trunc(n1)

print(f'O valor {n1} tem {n2} partes inteiras')