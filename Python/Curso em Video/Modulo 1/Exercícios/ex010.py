print('=====DESAFIO 10=====')
print('\nCrie um programa que lea quanto dinheiro uma pessoa tem e mostre a quantidade em dolar.')
print('-' *87)

dolar=float(input('Informe a quantidade de dólar para conversão, US$: '))
cotacao=float(input('Informe o valor da cotação do dólar R$: '))
conversao =cotacao/dolar
print('-' *87)
print(f'A quantidade de dólar convertido em real é: R${conversao:.2f}')
print('-' *87)