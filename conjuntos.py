from webbrowser import open_new


def união(a, b):
    uni = conjunto1 | conjunto2
    print(f'União: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {uni}')
    print()


def intersecção(a, b):
    intersec = conjunto1 & conjunto2
    print(f'Intersecção: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {intersec}')
    print()


def diferença(a, b):
    dif = conjunto1 - conjunto2
    print(f'Diferença: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {dif}')
    print()


def produto_cartesiano(a, b):
    lista = []
    for v in con1:
        for j in con2:
             lista.append((v, j))
    h = set(lista)
    print(f'Produto Cartesiano: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {h}')
    print()


# Escolha o nome do arquivo que o programa deve ler.
with open('arquivo1.txt','r+') as arquivo:
    informações = arquivo.readlines()
    informações = [x.strip('\n') for x in informações]


# Código Principal.
numero_ope = int(informações[0])
linha = 1
i = 0
while i < numero_ope:
    operação = informações[linha]
    con1 = [elemento.strip() for elemento in informações[linha + 1].split(',')]
    conjunto1 = set(con1)
    con2 = [elemento.strip() for elemento in informações[linha + 2].split(',')]
    conjunto2 = set(con2)
    linha += 3
    i+=1
    if operação == 'I':
        intersecção(conjunto1, conjunto2)
    elif operação == 'U':
        união(conjunto1, conjunto2)
    elif operação == 'D':
        diferença(conjunto1, conjunto2)
    elif operação == 'C':
        produto_cartesiano(con1, con2)




















