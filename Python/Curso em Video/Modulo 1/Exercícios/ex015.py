print('')
print('=====DESAFIO 015=====')
print('-'*115)
print("Escreva um programa que pergunta a quantidade de KM percorridos por um carro alugado e a quantidade de dias "
      "pelos\nquais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,"
      "15 por Km rodado.")
print('-'*115)

dia=int(input('\nQuantos dias o locador ficou com o carro? :'))
km=float(input('Quantos KM o Carro percorreu? :'))

nkm=km*0.15
ndia=dia*60
aluguel=int(nkm+ndia)

print(f'O aluguel do carro ficou R${aluguel}')