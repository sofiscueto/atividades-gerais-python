# Atividade 2: Funções e Exceções
# Crie uma função que divide dois números e trate as possíveis exceções e no fim apresente o resultado ou a mensagem de erro

def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
        return f"O resultado da divisão é: {resultado}"
    except ZeroDivisionError:
        return "Erro: Não é possível dividir por zero."
    except TypeError:
        return "Erro: O valor deve ser inteiro."

print(dividir(10, 2))  
print(dividir(10, 0))  
print(dividir(10, "a")) 