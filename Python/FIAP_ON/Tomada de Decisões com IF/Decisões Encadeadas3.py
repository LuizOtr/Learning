"""
Vamos  parao  seguinte  caso:  mulheres  grávidas  também  são  consideradas para  o  atendimento  prioritário  (sala  Branca  ou  Amarela).  Você vaiperguntar  para todos  os  pacientes  se  eles  estão  grávidos?Não,  apenas  para as  mulheres.  Então, Variáveis, tomada de decisão e laços de repetição você perguntaria para todas as mulheres? Não, você não precisaria perguntar para as  mulheres  com  idade  igual  ou  superior  a  65  anos,  assim  também poderia descartar criançascom menos de 10 anos.
"""
print('-'*80)
nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa? ").upper()

# PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca_infectocontagiosa=="SIM":
    print("Encaminhe o paciente para sala AMARELA")
elif doenca_infectocontagiosa=="NAO":
    print("Encaminhe o paciente para sala BRANCA")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")

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
Delimitamosos  dois  problemas  utilizando  o caractere“#’.  Este caracterepossui  muitos  nomes: hashtag,o  mais  descolado;mas  também  pode  ser:  jogo  da velha,  sustenido,  cerquilha,  antífen,  quadrado  e  o  mais  desejado  de  todos  os programadores: lasanha, porqueele parece uma lasanha, não é mesmo? Enfim, sua função  é  a  de  indicar  que  a  linha  iniciada  com  este caracterenão  deve  ser compilada,  ou  seja,  não  é  uma  linha  de  comandos  e,sim,uma  linha  particular  de comentários do programador.

"""