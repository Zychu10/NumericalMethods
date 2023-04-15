import numpy as np
import sympy as sympy
from numpy.linalg import inv

import wczytywanie


def matrixD(A):
    D = np.diag(np.diag(A))
    return D


def matrixDreverse(D):
    return inv(D)


def matrixLU(A, D):
    LU = A - D
    return LU


def matrixT(reverseD, LU):
    return (-(reverseD)) @ LU


def matrixC(reverseD, b):
    return reverseD @ b


def algortimhJacobi(A, b, iteracje, eps):

    licznik = 0
    if not(np.linalg.det(matrixD(A))):
        return "Macierz diagonalna powstala z macierzy A, jest macierza osobliwa"
    else:
        print("Macierz diagonalna powstala z macierzy A, jest macierza nieosobliwa")
    mT = matrixT(matrixDreverse(matrixD(A)), matrixLU(A, matrixD(A)))
    mC = matrixC(matrixDreverse(matrixD(A)), b)
    xNew = np.zeros_like(b)
    xOld = xNew

    while not (((np.allclose(xNew, xOld, atol=eps)) and licznik > 1) or licznik >= iteracje):
                xOld = xNew
                xNew = (mT @ xOld) + mC
                licznik += 1

    print(f'Ilosc iteracji {licznik}')
    return xNew


def dominujaca_przekatna(macierz):
    dominujaca = True
    diagonal = np.diag(macierz)
    for i in range(macierz.shape[0]):
        temp = 0
        for j in range(macierz.shape[1]):
            if i != j:
                temp += abs(macierz[i][j])
        if np.absolute(diagonal[i]) < np.absolute(temp):
            return False
    return dominujaca

def wyswietlanie():
    for i in range(1,11):
        A = wczytywanie.przypisywanie_macierzyA(i)
        b = wczytywanie.przypisywanie_macierzyB(i)
        print(f'Układ {i}')
        for i in range(A.shape[0]):
            row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
            print(f'{" + ".join(row)} = {b[i]}')
        print()

