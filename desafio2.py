def fibonacci_lista(limite):
    """"Gera uma lista de números de FIbonacci até um limite"""
    sequencia = [0, 1]
    while True:
        proximo = sequencia[-1] + sequencia[-2]
        if proximo > limite:
            break
        sequencia.append(proximo)
    return sequencia

"""Verifica se o número informado pertence à sequência de Fibonacci."""
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

# Gera e exibe uma lista de Fibonacci até um limite, por exemplo, 1000
limite = 10000
lista_fibonacci = fibonacci_lista(limite)
print(f'Sugestão de números da sequência de Fibonacci até {limite}: ')
print(lista_fibonacci)

# Solicita uma número ao usuário
numero = int(input('Digite um número: '))

# Verfica se o número pertence à sequência.
if fibonacci(numero):
    print(f'O número {numero} pertencen à sequência de Fibonacci.')
else:
    print(f'O número {numero} NÃO pertence à sequência de Fibonacci.')
