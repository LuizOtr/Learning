

print('-'*80)
# Lista preenchida estaticamente
lista_estatica = ["xpto", True]

# Lista preenchida dinamicamente
lista_dinamica = [input('Digite o usuário: '), bool(int(input("Está logado? ")))]

# Lista vazia
lista_vazia=[]
print('-'*80)

"""
Observe que,em todos os casos, os valores de uma lista devem estar entre colchetes “[ ]”, mesmo quando a lista for declarada vazia.
Na “lista_dinamica”, o segundo item está passando por duas conversões.Isso ocorreu porque desejamos um dado do tipo “boolean”, ou seja,  um  dado  booleano que pode possuir apenas os valores “True” ou “False”.Esse tipo de dado é utilizado normalmente  para  perguntas  que  possam  ter  como  resposta  somente  os  valores “sim”  ou  “não”,  como  é  o  caso  do  nosso  exemplo,  a  pergunta  “Está logado?” somente pode teras respostas “sim”ou ”não”.
Como o inputretorna uma string,devemos converter o dado para int(inteiro), para,então,posteriormente,convertê-lo para bool(booleano). Não podemos fazer a conversão diretamente de stringpara bool. O valor retornado será “False” somente se o número informado for igual azero, qualquer outro valor trará o retorno “True”.

"""