from random import choice

print('')
print('=====DESAFIO 19=====')
print('-'*85)
print('Um professor que sortear um dos seus quatro alunos para apagar o quadro.\n'
        'Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.')
print('-'*85)


a1=input('Aluno 1: ')
a2=input('Aluno 2: ')
a3=input('Aluno 3: ')
a4=input('Aluno 4: ')

print(f'\n O Aluno escolhido foi: {choice([a1, a2, a3, a4])}')

