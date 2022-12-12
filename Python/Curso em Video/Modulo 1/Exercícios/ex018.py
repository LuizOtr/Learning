from math import sin, cos, tan, radians

print('')
print('=====DESAFIO 18=====')
print('-'*102)
print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seu seno, cosseno e tangente!')
print('-'*102)

ang = float(input('Digite o valor de um ângulo: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tang = tan(radians(ang))
print("Seu seno: {:.2f}"
      "\nSeu cosseno: {:.2f}"
      "\nSua tangente: {:.2f}".format(seno, cos, tang))