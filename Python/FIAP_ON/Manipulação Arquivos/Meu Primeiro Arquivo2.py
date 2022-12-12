'''
No  segundo  parâmetro,estamos  especificandoo valor “r”,que  significa  que abriremos  o  arquivo  somente  para  leitura  e,dentro  do with,chamamos  a  função read(), que lê o conteúdo do arquivo.Mas como você pode observar,foi gerado um erro ao  tentar  executar essas duas  linhas  de  código.Isso  aconteceu  porqueo arquivo não existe, como você pode tentar efetuar a leitura de um arquivo sem que ele  exista?  O  Python,então,retornará  a  mensagem  de  erro: FileNotFoundError: [Errno  2]  No  such  file  or  directory:  'teste.txt'.  Isso  foi  apenas  para  que  você pudesse  já  observar  o  funcionamento  do  segundo  parâmetro,  uma  vez  que  a  ideia principal, nessa parte, é a de criar um arquivo e nãoa deler o arquivo.
'''

with open('primeiro_arquivo.txt', 'r') as arquivo:    # 'a' permirte inserir novas informações e 'w' ele cria um novo arquivo.
    for linha in arquivo.readlines():
        print(linha)

'''
Repare que os acentos podem estar com caracteres estranhos, isso pode ou não acontecer,  depende  da  configuração  da  sua  IDE  (PyCharm)  paraaleitura  de encodespara  exibição  de  caracteres  do  tipo  texto.Clique em “Reload  in  another encoding” e opte pela opção windows-1252ou ISO-8859-1, ou ainda algum  outro encodingcompatível com o seu layout de teclado, idioma e/ousistema operacional. Pode  alteraro encode,  fechar  o  arquivo,  gerar  um  novo  arquivo  (executando  seu código) e abri-lo novamente para verificar se a alteração foi realizada com sucesso.
'''