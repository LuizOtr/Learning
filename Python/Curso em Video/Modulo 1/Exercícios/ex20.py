from random import choice, choices, sample

print('')
print('=====DESAFIO 20=====')
print('-'*78)
print('O mesmo professor quer sortear a orde de apresentação de trabalho dos alunos, \nfaça um programa que mostre o nome dos'
      'quatro alunos e mostre a ordem sorteada.')
print('-'*78)

a1=input('Aluno 1: ')
a2=input('Aluno 2: ')
a3=input('Aluno 3: ')
a4=input('Aluno 4: ')

print(f'\n A ordem foi: {choices([a1, a2, a3, a4])}')