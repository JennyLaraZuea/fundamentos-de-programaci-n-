#matrz de 3*3
matriz = [
    [9, 5, 3],
    [7, 1, 4],
    [6, 2, 8]
]
print(matriz)
#funcion buscar valor especifico
def buscar_valor(matriz,valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == valor_buscado:
                return i,j


valor_buscado = 8

#print(buscar_valor(matriz,valor_buscado))
if valor_buscado == valor_buscado:
    print("valor encontrado en la pocicion",buscar_valor(matriz,valor_buscado))
else:
    print("valor incorrecto")