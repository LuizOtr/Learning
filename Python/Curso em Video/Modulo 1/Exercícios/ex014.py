print('')
print("="*5+"DESAFIO 14"+"="*5)
print('-'*89)
print("Escreva um programa que converta uma temperatura de graus Celsius para graus Fahrenheit!")
#Formula (13 °C × 9/5) + 32 = 55,4 °F
print('-'*89)

cel=float(input('\nQuantos graus celsius quer converter?: '))

fah=float(cel*1.8)+32

print(f'A conversão de {cel} Celsius para Fahrnheit deu {fah:.2f}ºF')