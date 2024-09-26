# Atividade 6: Exceções e Laços
# Conversão de Entrada Crie um programa que solicite ao usuário que insira um número e trate a
# exceção caso o usuário digite algo que não possa ser convertido para um número inteiro.


while True:
    entrada = input("Digite um número inteiro (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    try:
        numero = int(entrada)
        print(f"Você digitou o número: {numero}")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, insira um número inteiro.")
