cand1 = 0
cand2 = 0
cand3 = 0
nulo = 0
branco = 0
def votacao(autorizacao, voto):
    if autorizacao == 'NEGADO':
        print('Você não pode votar.')
    else:
        if voto == 1:
            global cand1
            cand1 += 1
        elif voto == 2:
            global cand2
            cand2 += 1
        elif voto == 3:
            global cand3
            cand3 += 1
        elif voto == 4:
            global nulo
            nulo += 1
        elif voto == 5:
            global branco
            branco += 1


def autoriza_voto(ano_nascimento):
   from datetime import date
   ano_atual = date.today().year
   idade = ano_atual - ano_nascimento
   if idade < 16:
      return 'NEGADO'
   elif idade >= 16 or idade < 18 or idade > 70:
      return 'OPCIONAL' 
   else:
      return 'OBRIGATÓRIO' 

eleitores = int(input("Insira o total de eleitores: "))

for votos in range(eleitores):
    print(f'''
            1 - Lula
            2 - Bolsonaro
            3 - Ciro
            4 - Nulo
            5 - Branco
    ''')
    nasc = int(input('Digite seu ano de nascimento: '))
    autorizacao = autoriza_voto(nasc)
    urna = int(input("Digite o número do seu candidato: "))
    votacao(autorizacao, urna)
   

print(f'''
        Lula tirou: {cand1} votos.
        Bolsonaro tirou: {cand2} votos.
        Ciro tirou: {cand3} votos.
        Votos nulos: {nulo}.
        Votos brancos: {branco}.
        ''')

if cand1 > cand2 and cand1 > cand3:
    print('Lula venceu 2022')
elif cand2 > cand1 and cand2 > cand3:
    print('Bolsonaro venceu 2022')
elif cand3 > cand1 and cand3 > cand2:
    print('Ciro venceu 2022')
else:
    print('Ocorreu um empate. Aguarde o segundo turno.')