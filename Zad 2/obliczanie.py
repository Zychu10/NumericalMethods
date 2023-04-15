import wczytywanie
import numpy as np

def tworzenie_macierzy_D(A):
    C = np.diag(A)
    D = np.diagflat(C)
    return D


def tworzenie_macierzy_R(A,D):
    R = A - D
    return R

def tworzenie_macierzy_odwrotnej_do_D(A):
    C = np.diag(A)
    D = 1 / C
    D1 = np.diagflat(D)
    return D1

def tworzenie_macierzy_T(R, D1):
    T = -R @ D1
    return T

def tworzenie_macierzy_C(D1, b):
    C = D1 @ b
    return C

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

def jacobi(A, b, T, C, ite, eps):
    licznik = 0
    x = np.zeros_like(b)
    print(x)
    x_new = np.zeros_like(x)
    if dominujaca_przekatna(A):
        for licznik in range(1, ite + 1):
            x_new = T @ x + C
            print(x_new)
            if licznik >= ite:
                #np.allclose(x, x_new, atol=1e-10, rtol=0.) or licznik >= ite:
                return x_new
            else:
                x = x_new
    else:
        print("Macierz nie ma dominujacej przekatnej")
        return dominujaca_przekatna(A)


plik = int(input("Wybierz numer od 0 do 10, który układ chcesz wczytać \n"))
A = wczytywanie.przypisywanie_macierzyA(plik)
b = wczytywanie.przypisywanie_macierzyB(plik)
D = tworzenie_macierzy_D(A)
R = tworzenie_macierzy_R(A, D)
D1 = tworzenie_macierzy_odwrotnej_do_D(A)
C = tworzenie_macierzy_C(D1, b)
T = tworzenie_macierzy_T(R, D1)
#print(dominujaca_przekatna(A))

print(jacobi(A, b, T, C, 30, -1))
#print(tworzenie_macierzy_D(A))
#print(tworzenie_macierzy_R(A,D))
#print(tworzenie_macierzy_odwrotnej_do_D(A))
#print(tworzenie_macierzy_T(R, D1))
