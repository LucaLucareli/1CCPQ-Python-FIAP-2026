# print("Conversor de números")
# print("1 - Decimal para Binário")
# print("2 - Binário para Decimal")

# opcao = input("Escolha a opção (1 ou 2): ")

# if opcao == "1":
#     decimal = int(input("Digite um número decimal: "))
#     n = decimal
#     binario = ""
#     print(f"Convertendo {decimal} para binário:")
#     while n > 0:
#         resto = n % 2
#         binario = str(resto) + binario
#         print(f"{n} ÷ 2 = {n//2}, resto = {resto}")
#         n = n // 2
#     if binario == "":
#         binario = "0"
#     print(f"{decimal} em binário é {binario}")
    
# elif opcao == "2":
#     binario = input("Digite um número binário: ")
#     decimal = 0
#     print(f"Convertendo {binario} para decimal:")
#     for i, digito in enumerate(binario[::-1]):
#         valor = int(digito) * (2 ** i)
#         print(f"{digito} * 2^{i} = {valor}")
#         decimal += valor
#     print(f"{binario} em decimal é {decimal}")

# else:
#     print("Opção inválida!")


print("Conversor de números para binario")

binarios = ["1010","1111","1100","10101","110011","0111","11001","0110101","0111101","1001000","1010100","1011010","1100001","1100011"]

for b in binarios:
    decimal = 0
    # print(f"\nConvertendo {b} para decimal:")
    for i, digito in enumerate(b[::-1]):
        valor = int(digito) * (2 ** i)
        #print(f"{digito} * 2^{i} = {valor}")
        decimal += valor
    print(f"{b} em decimal é {decimal}")

print("Conversor de binario para números")


hexadecimais = [
    {"num": "19A", "base": 16},
    {"num": "28B", "base": 16},
    {"num": "A16B", "base": 16},
    {"num": "1001", "base": 2},
    {"num": "111111111", "base": 2},
    {"num": "100101", "base": 2},
    {"num": "1243", "base": 6},
    {"num": "1745", "base": 8},
    {"num": "2023", "base": 4},
    {"num": "11000", "base": 2},
    {"num": "4A93", "base": 16},
    {"num": "FF", "base": 16},
    {"num": "11001", "base": 2},
    {"num": "00101", "base": 2},
]

for h in hexadecimais:
    num_str = h["num"].upper()  # pega a string e coloca maiúscula
    base = h["base"]
    decimal = 0
    print(f"\nConvertendo {num_str} (base {base}) para decimal:")
    
    # percorre cada dígito da direita para a esquerda
    for i, digito in enumerate(num_str[::-1]):
        if digito.isdigit():
            valor = int(digito)
        else:
            valor = ord(digito) - ord('A') + 10  # letras A-F
        resultado = valor * (base ** i)
        print(f"{digito} * {base}^{i} = {resultado}")
        decimal += resultado
    
    print(f"{num_str} em decimal é {decimal}")