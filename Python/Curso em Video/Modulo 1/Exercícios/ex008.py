print('\n=====DESAFIO 08=====')
print('\nEscreva um programa que leia um valor em metros e o exiba convertido em todas as medidas.')
print('-' *89)
num = float(input('Digite o valor da metragem:'))
dm = num * 10
cm = num * 100
mm = num * 1000
dam = num / 10
hm = num / 100 #hectômetro
km = num / 1000
print(f'\nO valor: {dm}m \nem milímetro: {mm:.0f}mm\nem centímero: {cm:.0f}cm\nem decímetro: {dm:.0f}dm \nem decâmetro: {dam}dam\nem hectômetro: {hm}hm\ne em kilometro: {km}km')