"""
Procure  criar  um  arquivochamado  DesafioDecisao.py  e  elaborar  o  código para resolver a seguinte situação: o seu módulo solicitaráo nível de acesso de uma pessoa que pode ser: ADM, USR ouGUEST e o gênero dessa pessoa, caso o nível seja  ADM,  ele  deverá  exibir  “Olá  administrador”  para  os  homens  ou  “Oláadministradora” para as mulheres. Se o nível for USR, deverá exibir “Olá usuário” para  os  homens  ou  “Olá  usuária”  para  as  mulheres.  Se  o  nível  for  GUEST,a mensagem deverá ser “Olá visitante”.Ese  o  nível  digitado  for  diferente  de  ADM, USR  ouGUEST  deverá  exibir  a  mensagem  “Olá  desconhecido(a)”. Considere Variáveis, tomada de decisão e laços de repetição apenas os gêneros masculino e feminino.

"""
print('-'*80)
nivel=input("Digite o nível de acesso: ").upper()
if nivel=="ADM" or nivel=="USR":
    genero=input("Digite o seu gênero: ").upper()
    if nivel=="ADM":
        if genero=="FEMININO":
            print("Olá administradora")
        else:
            print("Olá administrador")
    else:
        if genero=="FEMININO":
            print("Olá usuária")
        else:
            print("Olá usuário")
elif nivel=="GUEST":
    print("Olá visitante")
else:
    print("Olá desconhecido(a)")
print('-'*80)