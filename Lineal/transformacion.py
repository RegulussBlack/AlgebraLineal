# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:47:37 2024

@author: Fabricio
"""
import numpy as np

def obtener_matriz_transformacion_lineal(m, n):
    print(f"Ingrese los elementos de la matriz {m}x{n} para la transformación lineal:")
    matriz_transformacion = np.zeros((m, n), dtype=float)

    for i in range(m):
        for j in range(n):
            elemento = float(input(f"Ingrese el elemento en la posición ({i+1}, {j+1}): "))
            matriz_transformacion[i, j] = elemento

    return matriz_transformacion

def main():
    m = int(input("Ingrese la dimensión m para la transformación lineal de R^n a R^m: "))
    n = int(input("Ingrese la dimensión n para la transformación lineal de R^n a R^m: "))
    
    matriz_transformacion = obtener_matriz_transformacion_lineal(m, n)

    print("\nMatriz de la Transformación Lineal:")
    print(matriz_transformacion)

if __name__ == "__main__":
    main()
