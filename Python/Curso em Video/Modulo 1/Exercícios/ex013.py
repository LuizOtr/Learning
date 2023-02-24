print('\n=====DESAFIO 13=====')

print('-'*100)
print('Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.')
print('-' *100)

salario=float(input('\nDigite o valor do seu salário:R$'))
aumento=salario*0.15
nvsalario=float(salario+aumento)
print('-' *80)
print(f'Seu salário foi de R${salario:.2f} para R${nvsalario:.2f} O total do aumento foi de R${aumento:.2f}')
print('-' *80)