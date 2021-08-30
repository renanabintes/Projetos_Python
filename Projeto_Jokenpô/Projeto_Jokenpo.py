from random import shuffle

while True:
  rodada = 0
  escolha = str(input('Digite uma opção: [Pedra, Papel ou Tesoura'))
  c1 = ('Pedra')
  c2 = ('Papel')
  c3 = ('Tesoura')
  computador = [c1, c2, c3]
  random.shuffle(computador)
  cont = input('Deseja jogar novamente? [S/N]').strip().upper()[0]
  if cont == "N"
  print('Fim de jogo!')
  break