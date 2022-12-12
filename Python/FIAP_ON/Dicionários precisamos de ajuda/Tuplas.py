
usuario = {}
emails = ['xrtq@gmail.com', 'ramiro@gmail.com']

tupla = list(enumerate(emails))

for chave in range (0,len(tupla)):
    print(f'Email: ', tupla[chave][1])
    usuarios[tupla[chave]]=[input('Digite o nome: '), input('Digite o nível: ')]

for chave, dado in usuarios.item():
    print(f'Usuario..: {chave[0]}')
    print(f'Email....: {chave[1]}')
    print(f'Nome.....: {dado[0]}')
    print(f'Nível....: {dado[1]}')