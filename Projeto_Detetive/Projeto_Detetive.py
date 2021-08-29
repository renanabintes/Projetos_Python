resp = 0
p1 = str(input("Você telefonou para a vítima? (Sim ou Não)").strip().lower())
if p1 == 'sim':
  resp += 1


p2 = str(input("Você esteve no local do crime? (Sim ou Não)").strip().lower())
if p2 == 'sim':
  resp += 1


p3 = str(input("Você mora perto da vítima? (Sim ou Não)").strip().lower())
if p3 == 'sim':
  resp += 1


p4 = str(input("Você devia para a vítima? (Sim ou Não)").strip().lower())
if p4 == 'sim':
  resp += 1


p5 = str(input("Você já trabalhou com a vítima? (Sim ou Não)").strip().lower())
if p5 == 'sim':
  resp += 1

# resp = resposta
# p = pergunta

if resp == 2 :
  print('"Suspeita"')
elif resp == 3 or resp == 4:
  print('"Cúmplice"')
elif resp == 5:
  print('"Assassino"')
else:
  print('"Inocente"')