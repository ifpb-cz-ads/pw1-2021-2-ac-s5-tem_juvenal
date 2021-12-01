
#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
#O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor= float(input("Digite o valor da casa: "))
salario = float(input(("Digite o seu salário: ")))
anos = float(input("Digite a quantidade de anos: "))

meses = anos * 12;

prestacao = valor / meses

if prestacao > salario * 0.3:
    print("Emprestimo não aprovado!")

else:
    print(f"Valor da prestção: R$: {prestacao:7.2f}")