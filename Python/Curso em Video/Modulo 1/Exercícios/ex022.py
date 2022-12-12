
print('\n'+' '*38+'=====DESAFIO 22=====')
print('-'*103)
print("""Crie um programa que leia o nome completo de uma pessoa e mostre: 
O nome com todas as letras maiusculas e minusculas, quantas lentras tem ao todo(sem considerar espaços)
E quantas letras tem o primeiro nome""")
print('-'*103)

while True:
    p1 = input('Digite um nome: ')

    if p1.isupper():
        print('Tudo maisculo')
    elif p1.islower():
        print('Tudo minusculas')
    else:
        print('Tudo Misturado')