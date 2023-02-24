nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
if idade>=65:
    print(f"O paciente {nome} POSSUI atendimento prioritário!")
else:
    print(f"O paciente {nome} NÃO possui atendimento prioritário!")

# Alguns programadores menos avisados utilizam duas tomadas de decisões simples em vez de uma composta
# NUNCA faça isso. Veja como ficaria o código:

'''
 nome=input("Digite o nome: ")
 idade=int(input("Digite a idade: "))
 if idade>=65:
     print(f"O paciente {nome} POSSUI atendimento prioritário!")
 if idade < 65:
     print(f"O paciente {nome} NÃO possui atendimento prioritário!")


O código  acima  está  totalmente  fora  das  boas  práticas  de programação,  os dois  “ifs”  serão processadossempre  que o  programa for  executado.  Observe  o seguinte: se o paciente tiver 80 anos,o primeiro “if” será processado, mesmo assim, a linguagem verificaráo segundo “if”,e sabemos que não existe chance alguma de acondição do  segundo“if”  ser  verdadeira,  ou  seja,  a  linguagem vai consumir  um processamento desnecessário. Se  você  avaliar  que  a  condição que  estamos  propondo  (uma  comparação com  números)é  uma  condição  que  não  exige  muito  esforço  do  processador,  vocênão  verá  problemas,  mas  pense  que  futuramente  não  trabalharemos  apenas  com condições  tão  simples e,com  certeza,vamos exigir  esforço  do  processador,  por isso, devemos seguir as boas práticas desde já. NÃO substitua NUNCA uma decisão composta por duas ou mais decisões simples.

'''

