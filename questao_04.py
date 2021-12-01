
distancia = float(input("Digite sua distancia em km: "))

valor01 = 0.45
valor02 = 0.50

if distancia >200:
    passagem = distancia * valor01
    print(f" O valor da passage é  R$ {passagem:7.2f}")

else:
   passagem = distancia * valor02
   print(f" O valor da passage é  R$ {passagem:7.2f}")
