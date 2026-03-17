lista = list(map(int, input('Digite os números separados por espaço: ').split()))

base = int(input('Digite a base: ').strip())

resultado = 0
for i in range(len(lista)):
    resultado += lista[i] * base**(len(lista)-1-i)

print(f"O resultado é: {resultado}")