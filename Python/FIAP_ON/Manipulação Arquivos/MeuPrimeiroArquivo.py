

arquivo = open('primeiro_arquivo.txt', 'w')

arquivo.write('meu primeiro arquivo! Ai que festa!')

arquivo.close()

'''
Para um primeiro teste, apresentamos a utilização da função open()junto ao comando “with”, esse comando  permitirá  representar,  dentro  do  bloco  identado,  o arquivo  “teste.txt” por   meiodo  “alias” arquivo.Outragrande   vantagem   que obteremos  todas  as  vezes  que  formos  utilizar  a  função open()combinada  ao comando withé que o controle do encerramento do arquivo em memória ficará por conta do comando with, isso faz com que você não precise utilizar o método close(), tampouco  ocorrerá  o  fato  do  arquivo  ficar  aberto  na  memória  sem  qualquer necessidade. Por isso,recomendo que utilize esse combinado open() + with, você não vai se arrepender!
Seguindo   a   leitura   do   código   apresentado   anteriormente,   perceba   que colocamos,no  primeiro  parâmetro  da  função open(),o  arquivo  “teste.txt”  sem qualquer  caminho  sendo  especificado.Isso  indica  que  o  Python  irá  considerar  o caminho  do  seu  arquivo  que  contém  o  código-fontee  que,consequentemente,estará sendo executado, ou seja, o caminho adotado para o arquivo “teste.txt” será o mesmo  do  arquivo  “GravarArquivo.py”.  Caso  queira,  nada  impede  de  definir  um caminho  para  o  arquivo,  você  deverá  substituir  “teste.txt”  por,  por  exemplo,“c:\meus_arquivos\teste.txt”.Perceba   que   o   destaque   negritado   representa   o caminho, isso significa que terá que ter acesso ao “c:\” e que,dentro desta unidade, Manipulação de arquivos eJSON


'''