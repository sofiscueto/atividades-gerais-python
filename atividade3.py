# Atividade 3: Estruturas de Decisão e Laços
# Crie uma lista de números de 1 a 5 e imprima se cada número é par ou ímpar

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} é par.")
    elif numero % 2 != 0:
        print(f"{numero} é ímpar.") 
        
