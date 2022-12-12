print('\n=====DESAFIO 12=====')
print('Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto')
print('-'*94)

produto=float(input('\nDigite o valor do produto R$'))
desc= produto - (produto-0.05)
vdesc= produto * 0.05
vardes= produto - vdesc

print(f'O valor do produto sem desconto é de R${produto:.2f}')
print(f'o valor do produto com descoto de 5% é de R$:{desc:.2f}')
print(f'O preço abatido do produto foi de R${vdesc:.2f}')
print('-'*50)
print(f'O produto com desconto fica R$:{vardes:.2f}')