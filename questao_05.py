
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operção a realizar (+,-,* ou /):")

if operacao == "+":
    resultado = n1 + n2;
elif operacao == "-":
    resultado = n1 - n2;
elif operacao == "*":
     resultado = n1 * n2;
elif operacao == "/":
    resultado = n1/n2;

else:
    print("Operação invalida!")
    resultado = 0

print("Resultado: ", resultado);
