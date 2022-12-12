'''
A  estrutura  “for”  também  permite uma  repetição,  mas  sua  aplicação  é  um tanto quanto diferente quando comparadaao “while”. O “for” indica o término do laço de duas formas básicas: porum número que delimita o seu final ou poruma lista dedados que foi verificada por completo. 
Em  suma,podemos afirmar que o “while” trabalha mais diretamente com a interação  do  usuário  final,  diferentemente  do  “for”, com  o  que normalmente  a situação  está  previamente  definida  pelo  próprio  sistema.  No  atual  momento,  diria para  vocês  fixarem-semais  no “while”.Logo,  com  a  evolução  dos  capítulos,vocês constatarão,de  maneira  mais  clara,a  diferença  entre  asaplicaçõesdos  dois comandos. De qualquer forma, vamos seguir com alguns exemplos para que você já possa conhecer a estrutura do “for”.
'''
print('-'*80)
for numero in range(1,int(input('Digite um numero para determinar o seu fim: ')),1):
    print(f"{numero}")
print('-'*80)