usuarios = {}
print(usuarios)

usuarios = {
    "chaves" : ["chaves do 8", '24,12,2017', 'Recep_01'],
    'quico' : ['Quico das Dlores', '20,12,2017', 'Raiox_03']
}
print(usuarios)

'''
vamos  analisar  o  código.Na  primeira  linha,estamos  criando o  dicionário  de dados.Repare  que,em  vezde  utilizarmos  os  colchetes  (como  fizemos  com  as listas), usamosas chaves “{}”, essa é a representação de um dicionário de dados.
Na segunda linha, preenchemosfielmente o nosso dicionário de acordo com onosso exemplo de um dicionário de dados.Acima, perceba que adotamos os logins como  chave  de  cada  objeto  (no  caso,  são  dois).Depois  da  chave,utilizamos  dois pontos  (:)  e,então,surgem  os  dados  da  chave  que  foi  preenchida.Como  no Manipulação de Dicionários e Tuplas
'''

usuarios['florinda'] = ['Dona florinda', '24/12/2017', 'Raiox_01']
print(usuarios)

'''
A   linha acima   apresentada   normalmente   é   utilizada   quando   queremos adicionar  os  objetos  de  maneira  singular,  ou  seja,  objeto  por  objeto.Repare  que,após   o   nome   do   dicionário,   colocamos   entre   colchetes   do   dado   que   será armazenado  na  chave  e  igualamos  com  o  dado  quepertence àchave.No  nosso caso,uma lista com nome, data do último acesso ao sistema e a última estação que foi  utilizada  pelo  usuário. Da  primeira  forma  que  foi  apresentada  (no  Código-fonte: “Exemplo  de  um  dicionário  de  dados”),  se  tentarmos  dividir  em dois  momentos  a adição  dos  objetos  no  dicionário,  simplesmente  estaremos  considerando  a  última linha  onde  foi inserido o  conteúdo,  sobrescrevendo  todos  os  objetos  inseridos anteriormente.
'''

print('-'*50)
print(usuarios.get('quico'))

'''
No  primeiro  print(), exibimostudooque  existe  dentro  do  dicionário.Já  no último  print(), somente  os  dados  do  objeto  que  tiver  a  chave  “Chaves”.Isso  foi possível porqueinvocamos o nosso dicionário “usuarios” e utilizamos o seu método get(), que recebe um dado e vai pesquisá-lo entre as chaves que existem dentro do dicionário, caso ele encontre, retornará os dados relativos à chave encontrada. 
Se você alterar, dentro do get(), o valor “Chaves” para “Chapolim”,verá  que será  retornado  o  valor  “None”,  palavra  reservada  que  representa  um  valor  não encontrado dentro do Python.Percebeu que não precisamos criar um foreachpara localizar uma informação dentro do dicionário? Por isso, em determinadas situações,é muito mais prático e eficiente utilizar dicionários, assim como você pode ter outras situações em  que as  listas  serão  o  caminho  mais  viável,  ou  ainda,  conforme demonstramos  neste  exemplo,  você  pode  ter  uma  lista  dentro  de  um  dicionário. Cabe a você julgar a melhor estrutura que atenderáàsua necessidade.
'''