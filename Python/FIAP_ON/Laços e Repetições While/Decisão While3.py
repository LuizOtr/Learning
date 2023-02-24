"""
Queremos  obter  oseguinte  resultado:  enquanto  o  usuário  digitar  algo diferente (representamos  diferente  dentro  do  Python,  através do  seguinte operador: !=) de “SIM” ou “NAO”, o programa continuará perguntando se o paciente  suspeita ter  algumadoença infecto-contagiosa.Tente primeiro fazer sozinho, sem olhar o código abaixo.

"""

print('-'*80)
nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa? ").upper()
# PRIMEIRO PROBLEMA A SER RESOLVIDO
while doenca_infectocontagiosa!="SIM" and  doenca_infectocontagiosa!="NAO":
    print("Digite SIM ou NAO")
    doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()

if doenca_infectocontagiosa=="SIM":
    print("Encaminhe o paciente para sala AMARELA")
else:
    print("Encaminhe o paciente para sala BRANCA")

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero=input("Digite o gênero do paciente: ").upper()
    if genero=="FEMININO" and idade>10:
        gravidez=input("A paciente está grávida? ").upper()
        if gravidez=="SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")
print('-'*80)

"""
Repare que o código alterado ocorreu apenas no “primeiro problema”, e que a estrutura do “if” logo abaixo do “while” também foi alterada.Não faz mais sentido ter o “elif”,pois somente serão aceitos os valores “SIM” e “NAO”.Qualquer  valor  fora disso ficará preso no “while”, até que se digite o valor desejável.Dentro do código apresentado,podemos utilizar ainda outro “while” para que permitaadicionar  mais  que  um  paciente,  assim  como  fizemos  com  o  usuário  no segundo exemplo deste tópico. Tente, mãos na massa!

"""