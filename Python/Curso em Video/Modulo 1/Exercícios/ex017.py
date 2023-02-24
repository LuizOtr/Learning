from math import hypot

print('')
print('=====DESAFIO 17=====')
print('-'*110)
print('Faça um programa que leia os dois catetos de um triangulo retângulo e calcule o comprimento de sua hipotenusa!')
print('-'*110)

catop = float(input('Informe o cateto oposto: '))
catadj = float(input('Agora informe o cateto adjacente: '))

print('A hipotenusa do triangulo tem o valor de: {:.0f}'.format(hypot(catop, catadj)))