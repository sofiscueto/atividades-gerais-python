# Atividade 4: Estrutura de Decisão e Laços
# Soma de Números Crie um programa que peça ao usuário para digitar números até que ele
# insira ‘0’ para sair. O programa deve calcular e imprimir a soma de todos os números digitados,
# excluindo o 0.

soma = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    soma += numero

print(f"A soma dos números digitados é: {soma}")
