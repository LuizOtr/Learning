
print('-' *50)
nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa?").upper()
if idade >= 65:
    print("Paciente COM prioridade")
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa=="NAO":
        print("Encaminhe o paciente para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")
else:
    print("Paciente SEM prioridade")
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa=="NAO":
        print("Encaminhe o paciente para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")
print('-' *50)

"""
O  resultado  final  para  o usuário  final  é  o  mesmo,  a  diferença  é  que  iremos resolvendo  o  problema  por  partes.Levando  em  consideração  o  código  acima, primeiro vamos identificar  a  idade  do  paciente  para  definir  se  ele  terá  atendimento prioritário  ou  não, e depois seo  paciente  está ou  não  sob  a  situação  suspeita  de doença infecto-contagiosa.

Você deve estar se perguntando: então, tanto faz usar decisão composta ou decisão  encadeada?  Para  o  exemplo acima,poderíamos  dizer  que sim,  mas,na prática,não  é  bem  assim.Observe  que  temos  apenas  duas  condições  (idade  e suspeita  de  doença infecto-contagiosa).Se  tivéssemos  mais  condições,teríamos uma sequência muito grande de “if ́s” e “elifs” e,consequentemente,uma  grande chance  de  errarmos  uma  das  linhas  de  condiçõescompostas.  Neste  caso,é altamente recomendável, por boa prática,utilizarmosas decisões encadeadas, pois facilitam a leitura e isolam as ações que devem ser levadas em consideração.

Além disso, a  decisão  encadeada foi  desenvolvida  para  que se possa  tomar uma decisão somente quando outra decisão já foi definida como verdadeira ou falsa.

"""