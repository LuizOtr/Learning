from Identificação_de_Funções import * # importa tudo 

#import Identificação_de_Funções as iF  # --------- as> da um apelido para o import para não precisar ficar escrevendo tudo. 

minhaLista = []
print("Preenchendo")
preencherInventario(minhaLista)
print("Exibindo")
exibirInventario(minhaLista)

print("Pesquisando")
localizarPorNome(minhaLista)
print("Alterando")
depreciarPorNome(minhaLista, 20)

print("Excluindo")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("Resumindo")
resumirValores(minhaLista)