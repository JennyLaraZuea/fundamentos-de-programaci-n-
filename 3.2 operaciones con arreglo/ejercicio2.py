#ejercicio 2 matriz 3*3
matriz=[
    [9, 5, 3],
    [7, 1, 4],
    [6, 2, 8]
]
print(matriz)
#metodo de ordenacion buble_sort
def buble_sort(fila):
    #algoritmo buble sort
    n= len(fila)
    for i in range(n):
        for j in range(n-1, i, -1):
            if fila[j] > fila[j-1]:
                fila[j], fila[j-1] = fila[j-1], fila[j]
                print(fila)
print("matriz original")
print(matriz)
buble_sort(matriz[2])
print(matriz)
