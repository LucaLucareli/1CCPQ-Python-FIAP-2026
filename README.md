# 1CCPQ-Python-FIAP-2026 Documentação Básica de Python

## 1. O que é Python

Python é uma linguagem de programação simples, poderosa e fácil de aprender.

Ela é usada para:

- Desenvolvimento web
- Ciência de dados
- Automação
- Inteligência artificial
- Scripts e ferramentas

---

# 2. Primeiro Programa

```python
print("Hello, World!")
```

Esse comando imprime um texto na tela.

3. Variáveis

Variáveis armazenam valores.
```python
nome = "João"
idade = 20
altura = 1.75
```

Tipos comuns:

| Tipo  | Descrição | Exemplo  |
|-------|-----------|----------|
| str   | Texto     | "Python" |
| int   | Inteiro   | 10       |
| float | Decimal   | 3.14     |
| bool  | Booleano  | True     |

4. Entrada de Dados
```python
nome = input("Digite seu nome: ")
print("Olá,", nome)
```
5. Condicionais (if)
```python
idade = 18

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```
6. Loops
###### For
```python
for i in range(5):
    print(i)
```
###### While
```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```
7. Funções
```python
def saudacao(nome):
    print("Olá,", nome)

saudacao("Maria")
```
Função com retorno:
```python
def soma(a, b):
    return a + b

print(soma(5, 3))
```
8. Listas
```python
frutas = ["maçã", "banana", "laranja"]

print(frutas[0])

#Adicionar item:

frutas.append("uva")
```
9. Função map()

A função map() aplica uma função a todos os elementos de uma lista.

```python
#Exemplo 1
numeros = [1, 2, 3, 4]

def dobrar(n):
    return n * 2

resultado = map(dobrar, numeros)

print(list(resultado))

#Saída:

[2, 4, 6, 8]
#Exemplo 2 (com lambda)
numeros = [1, 2, 3, 4]

resultado = map(lambda x: x * 2, numeros)

print(list(resultado))
```
