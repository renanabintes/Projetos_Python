# Utilizando os conceitos aprendidos até dicionários, crie um programa onde 4 
# jogadores joguem um dado e tenham resultados aleatórios.# O programa tem que:
# • Perguntar quantas rodadas você quer fazer; 
# • Guardar os resultados dos dados em um dicionário.
# • Ordenar esse dicionário, sabendo que o vencedor tirou o maior número no dado.
# • Mostrar no final qual jogador ganhou mais rodadas e foi o grande campeão.

from random import randint

game = dict() 
ranking = list()
round = 0

while True:
    game = {
        'player1': randint(1,6),
        'player2': randint(1,6),
        'player3': randint(1,6),
        'player4': randint(1,6)
     }
    for k, v in game.items():
        print(f'The {k} took out {v} on the dice')
    match = input('Do you wish to continue: [Y/N]').strip().upper()[0]
    if match == 'Yes' or match == 'Y':
        print('Keep playing')
    elif match == 'No' or match == 'N': 
        print('End of the game')
        break
    else:
        print('Error: Use Yes or No only.')
        break
ranking = sorted(game.items())
for k, v in enumerate(ranking):
    print(f'{k+1}° position: {v[0]} with {v[1]}')

    





