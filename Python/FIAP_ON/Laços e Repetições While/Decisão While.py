"""
Repare  que  se  a  condição  for  eternamente  verdadeira,você  criará  o  que chamamos  de “loop  infinito”, isto  é,  o  programa  ficará  executando  este  bloco  de código  até  que  o  programa  seja  encerrado  de  maneira  abrupta,  seja  por  falha  do sistema,  estouro  da  memória, computador  foi  desligado  ou  algo  do  gênero.  Esse deve ser o nosso maior cuidado, em não criarmos “loops infinitos”. 

"""
print('-'*80)
numero=int(input("Digite um numero: "))
while numero<50:
    print("\t" + str(numero))
    numero=numero+1
print("Laço encerrado....")
print('-'*80)