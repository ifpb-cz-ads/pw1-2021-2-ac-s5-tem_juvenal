#2) Escreva um programa que leia três números e que imprima o maior e o menor.

primeiro = int(input("Digite primeiro número:"))
segundo = int(input("Digite segundo número:"))
terceiro = int(input("Digite terceiro número:"))

maior = primeiro;

if segundo > maior:
    maior = segundo;
if terceiro > maior:
    maior = terceiro;


menor = primeiro;

if segundo < menor:
    menor = segundo;

if terceiro < menor:
    menor = terceiro;

print("Maior: ",maior)
print("Menor: ", menor)
