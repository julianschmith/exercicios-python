numeros = [6, 7, 67, 69, 420]
maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print(f"O maior número da lista é: {maior}")