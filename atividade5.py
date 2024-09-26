# Atividade 5: Laços
# Tabuada Crie um programa que solicite ao usuário um número inteiro e, em seguida, exiba a
# tabuada desse número de 1 a 10.

numero = int(input("Digite um número inteiro para ver a tabuada: "))

print(f"Tabuada de {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
