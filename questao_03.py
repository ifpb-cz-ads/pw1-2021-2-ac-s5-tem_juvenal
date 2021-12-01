# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.


salario = float(input("Digite seu salário: "))

if salario > 1250:
    novo = salario + (salario * 10/100);
    print(f" Você teve um aumento 10% R$ {novo:7.2f}")

elif salario <= 1250:
     novo = salario + (salario * 15/100)
     print(f" Você teve um aumento de 15% R$ {novo:7.2f}")
