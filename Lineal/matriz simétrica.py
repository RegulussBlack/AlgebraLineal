# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:10:18 2024

@author: Fabricio
"""
def es_matriz_simetrica(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    if filas != columnas:
        return False  

    for i in range(filas):
        for j in range(i):
            if matriz[i][j] != matriz[j][i]:
                return False  

    return True 


def main():
    filas = int(input("¿Cuántas filas tiene la matriz? : "))
    columnas = int(input("¿Cuántas columnas de la matriz? : "))

    matriz = []

    print("Ingrese los elementos de la matriz:")

    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Ingrese el elemento en la posición [{i + 1}][{j + 1}]: "))
            fila.append(elemento)
        matriz.append(fila)

    if es_matriz_simetrica(matriz):
        print("La matriz ingresada es simétrica.")
    else:
        print("La matriz ingresada no es simétrica.")


if __name__ == "__main__":
    main()

