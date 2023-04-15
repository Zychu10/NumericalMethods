import numpy as np

def przypisywanie_macierzyA(plik):
    macierz = []
    if plik == 1:
        macierz = np.genfromtxt('data1.csv', delimiter=',', dtype="float")
    if plik == 2:
        macierz = np.genfromtxt('data2.csv', delimiter=',', dtype="float")
    if plik == 3:
        macierz = np.genfromtxt('data3.csv', delimiter=',', dtype="float")
    if plik == 4:
        macierz = np.genfromtxt('data4.csv', delimiter=',', dtype="float")
    if plik == 5:
        macierz = np.genfromtxt('data5.csv', delimiter=',', dtype="float")
    if plik == 6:
        macierz = np.genfromtxt('data6.csv', delimiter=',', dtype="float")
    if plik == 7:
        macierz = np.genfromtxt('data7.csv', delimiter=',', dtype="float")
    if plik == 8:
        macierz = np.genfromtxt('data8.csv', delimiter=',', dtype="float")
    if plik == 9:
        macierz = np.genfromtxt('data9.csv', delimiter=',', dtype="float")
    if plik == 10:
        macierz = np.genfromtxt('data10.csv', delimiter=',', dtype="float")
    return macierz

def przypisywanie_macierzyB(plik):
    if plik == 1:
        b = np.array([12., 33., 8.])
    if plik == 2:
        b = np.array([1., 20., -40.])
    if plik == 3:
        b = np.array([1., 20., -40.])
    if plik == 4:
        b = np.array([1.5, -1.625, 1.0, 0.4375])
    if plik == 5:
        b = np.array([0., -4., 4., 6.])
    if plik == 6:
        b = np.array([-13., 1., 21., -5.])
    if plik == 7:
        b = np.array([3., 7., 5.])
    if plik == 8:
        b = np.array([3., -4., 19.])
    if plik == 9:
        b = np.array([4., 11., 13.5])
    if plik == 10:
        b = np.array([1.5, 0.8, 0.7])
    return b


