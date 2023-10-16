# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida
km = float(input("Insira o valor da velocidade em km: "))
multa = 60 * 7
if km > 60:
  print(f"Você recebeu uma multa de: {multa}")
else:
  print("Você não recebeu multa")