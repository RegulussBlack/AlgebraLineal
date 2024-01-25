# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:37:17 2024

@author: Fabricio
"""

import numpy as np

def es_matriz_invertible(matriz):
    try:
        
        np.linalg.inv(matriz)
        return True
    except np.linalg.LinAlgError:
        return False

def main():
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))

    matriz = []

    print("Ingrese los elementos enteros de la matriz:")

    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Ingrese el elemento en la posición [{i + 1}][{j + 1}]: "))
            fila.append(elemento)
        matriz.append(fila)

    if es_matriz_invertible(matriz):
        inversa = np.linalg.inv(matriz)
        print("La matriz es invertible.")
        print("Matriz Inversa:")
        print(inversa.astype(int))  
    else:
        print("La matriz no es invertible.")

if __name__ == "__main__":
    main()
