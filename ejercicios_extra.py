#!/usr/bin/env python
'''
Listas [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Torres Molina Emmanuel O."
__email__ = "emmaotm@gmail.com"
__version__ = "1.2"

import math


def practica_listas():
    # 1) Crear una lista que contenga los nùmeros del -5 al 5

    # La lista solicitada es una secuencia numérica ordenada, se puede
    # crear utilizando range

    lista1 = []  # Lista vacía

    # Crear una lista de rango -5 a 5 inclusive
    inicio = -5
    fin = 5
    lista1 = list(range(inicio, fin + 1))
    print('1:', lista1)

    # 2) Crear una lista que contenga únicamente los números
    # impares entre -5 y 5

    lista2_1 = []  # Lista vacía
    lista2_2 = []  # Lista vacía
    # Crear una lista de rango -5 a 5 inclusive de 
    # solo números impares
    paso = 2
    lista2_1 = list(range(inicio, fin + 1, paso))   # Esto Sirve sólo porque la lista comienza con un número Impar.
    print('2.1:', lista2_1)

    # Otra Forma de Hacerlo y que es la manera Correcta y Sirve para Cualquier lista de Números:
    for i in range(len(lista1)):
        resto = lista1[i] % 2       # Calculo el Resto de la División entre el número y 2.
        if resto != 0:  # Si el resto es distinto de 0 es porque el dividendo es impar!!
            lista2_2.append(resto)

    # Ahora Usando Compresión de Listas:
    #lista2 = [numerito for numerito in range(-5, 6) if ((numerito % 2) != 0)]
    
    print('2.1:', lista2_1)

    # 3) De la lista1 filtrar los números negativos, es decir,
    # crear una lista a partir de lista1 de solo números negativos

    lista3 = []  # Lista vacía
    # Filtrar numeros negativos
    for i in range(len(lista1)):
        if lista1[i] < 0:
            lista3.append(lista1[i])
    
    print('3:', lista3)

    # 4) De la lista1 filtrar los números mayores a 2, es decir,
    # crear una lista a partir de lista1 de solo números mayores a 2

    lista4 = []  # Lista vacía
    # Filtrar numeros mayores a 2
    for n in lista1:
        if n > 2:
            lista4.append(n)

    print('4:', lista4)

    # 5) De la lista1 realizar la suma de todos los números.

    suma_total = 0
    # Sumar números
    for k in lista1:
        suma_total += k
    print('5.1:', suma_total)

    # Suma de Números ahora Usando la función "sum ()" de Python:
    suma_total = sum(lista1)
    print('5.2:', suma_total)

    # 6) De la lista1 realizar el módulo, es decir, pasar todos
    # los números a positivo.

    lista6 = []  # Lista vacía

    #Aplicar módulo:
    for i in range(len(lista1)):
        valor_abs = abs(lista1[i])
        lista6.append(valor_abs)
    
    # Ahora Usando Compresión de Listas:
    #lista6 = [abs(numerito) for numerito in lista1]
    
    print('6:', lista6)

    # 7) Calcular la suma entre la lista 1 y la lista 6
    # Como son del mismo tamaño utilizar len para calcular el largo
    # y recorrer con indices.

    lista7 = []  # Lista vacía

    # Sumar listas
    for i in range(len(lista1)):
        suma = lista1[i] + lista6[i]
        lista7.append(suma)

    print('7.1:', lista1)
    print('7.6:', lista6)
    print('7:', lista7)

    # 8) De la lista1 multiplicar por dos todos los números.

    lista8 = []  # Lista vacía

    # Multiplicar por dos
    # for i in range(len(lista1)):
    #     producto = lista1[i] * 2
    #     lista8.append(producto)

    # Ahora Usando Compresión de Listas:
    lista8 = [(numerito * 2) for numerito in lista1]
    
    print('8:', lista8)


if __name__ == '__main__':
    print("\n\n\nBienvenidos a otra clase de Inove con Python.\n")
    practica_listas()
    print('\n\n')
