"""
Também poderemos encontrar uma situação em que o Verdadeiro e o Falso,simplesmente,  nãosejam  suficientes.  Por  exemplo,  vamos  imaginar  que  pessoas com  idade  igual  ou  superior  a  65 receberão atendimento  prioritário,  mas  que também   pessoas   com   suspeita   de   doenças infecto-contagiosas deverão   ser direcionadaspara uma sala de espera distinta, por motivos óbvios. Este é um  casoem  queum  Verdadeiro  ou um Falso  na  idade  não  resolve, pois precisamosverificar se a idade do paciente émaior ou igual a 65anose,se a resposta  for  Falsa,  devemos  verificar  ainda  se  o  paciente  está  com  suspeita  de doença infecto-contagiosa.Ese,ainda assim,for Falsa a condição, então,podemos considerar que o paciente deve aguardar sem prioridade na sala comum de espera. Vamos  alterar  o  nosso  código  proposto  anteriormente  paraeste  novo  cenário,  da seguinte forma:

"""

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa?").upper()
if idade>=65:
    print(f"O paciente {nome} POSSUI atendimento prioritário!")
elif doenca_infectocontagiosa=="SIM":
    print(f"O paciente {nome} deve ser direcionado para sala de espera reservada.")
else:
    print(f"O paciente {nome} NÃO possui atendimento prioritário e pode aguardar na sala comum!")