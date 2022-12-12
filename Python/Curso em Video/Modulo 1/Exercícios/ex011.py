print('\n=====DESAFIO 11=====')
print('\nFaça um programa que leia a altura e largura de uma parede em metros, calcule sua área a quantidade necessária de \ntinta para pintá-la, sabendo qeu cada litro de tinta pinta uma área de 2m²')
print('-' *113)
altura=float(input('Qual e a altura da parede: '))
largura=float(input('Qual e a largura da parede: '))
area= altura*largura
tinta = area / 2

print(f'\nA área da sua parede é de:{area:.2f}m² e a quantidade de tinta necessária será:{tinta:.2f}L')