temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

indexMaisCritico = 0
valorMaisCritico = 0
for i in range (len(temperaturas)):
    mediaSala = 0
    qntTemp = len(temperaturas[i])
    qntTempMaiorIgual33 = 0
    for j in range (qntTemp):
        temp = temperaturas[i][j]
        mediaSala += temp
        if temp >= 33:
            qntTempMaiorIgual33 += 1
    print(f'Sala {i+1}:\nMédia sala: {mediaSala/qntTemp}\nQuantidade de registros críticos: {qntTempMaiorIgual33}\n')
    if(qntTempMaiorIgual33 > valorMaisCritico):
        indexMaisCritico = i

print(f'A sala que teve a maior quantidade de registros críticos foi a sala {indexMaisCritico+1}')
