import numpy
import numpy as np
from numpy import cos

import Rysowanie

e = 2.7182818284585634


def wartosc_funkcji(x, wybor_funkcji):
    wartosc = None
    if wybor_funkcji == "A":
        wartosc = horner([2, -4, 8, -3], x)
    elif wybor_funkcji == "B":
        wartosc = abs(x)
    elif wybor_funkcji == "C":
        wartosc = x + 4
    elif wybor_funkcji == "D":
        wartosc = cos(x)
    elif wybor_funkcji == "E":
        wartosc = x ** 3
    elif wybor_funkcji == "F":
        wartosc = 1 - e ** (-x)
    return wartosc

def horner(tab, x):
    b = tab[0]
    for i in range(len(tab) - 1):
        b = tab[i + 1] + x * b
    return b


def wspolczynniki(liczba_wezlow, numer_wezla):
    dane = (
        ((0.585789, 0.853553), (3.414214, 0.146447)),
        ((0.415775, 0.711093), (2.294280, 0.278518), (6.289945, 0.010389)),
        ((0.322548, 0.603154), (1.745761, 0.357419), (4.536620, 0.038888), (2.395071, 0.000539)),
        ((0.263560, 0.521756), (1.413403, 0.398667), (3.596426, 0.075942), (7.085810, 0.003612), (12.640801, 0.000032))
    )
    return dane[liczba_wezlow - 2][numer_wezla]


# def gauss(wybor_funkcji, liczba_wezlow):
#     calka = 0
#     for i in range(liczba_wezlow):
#         x = (wspolczynniki(liczba_wezlow, i)[0])
#         w = (wspolczynniki(liczba_wezlow, i)[1])
#         calka += w * wartosc_funkcji(x, wybor_funkcji)
#     return calka

def silnia(n):
    wynik = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            wynik *= i
        return wynik

def wielomianLaguerra(stopienWielomianu, x):
    if (stopienWielomianu == 0):
        return 1
    elif (stopienWielomianu == 1):
        return (x - 1)
    else:
        L = np.zeros(stopienWielomianu + 1)
        L[0] = 1
        L[1] = x - 1
        for i in range(1, stopienWielomianu):
            L[i + 1] = (((x - (2 * i) - 1) * L[i]) - ((i * i) * L[i - 1]))
    return L[stopienWielomianu]

def Ck(wybor_funkcji, liczba_wezlow, stopienWielomianu):
    mianownik = silnia(stopienWielomianu)**2
    licznik = 0
    for i in range(liczba_wezlow):
        x = (wspolczynniki(liczba_wezlow, i)[0])
        w = (wspolczynniki(liczba_wezlow, i)[1])
        licznik += w * wartosc_funkcji(x, wybor_funkcji) * wielomianLaguerra(stopienWielomianu, x)
    return (licznik/mianownik)


def tablicaCk(wybor_funkcji, liczba_wezlow, stopienWielomianu):
    tabCk = numpy.zeros(stopienWielomianu + 1)
    for i in range(stopienWielomianu + 1):
        tabCk[i] = Ck(wybor_funkcji, liczba_wezlow, i)
    return tabCk


def aproksymacjaFunkcja(wybor_funkcji, liczba_wezlow, stopienWielomianu, x):
    Ck = tablicaCk(wybor_funkcji, liczba_wezlow, stopienWielomianu)
    y = 0
    for i in range(stopienWielomianu + 1):
        y += Ck[i] * wielomianLaguerra(i, x)
    return y


def blad(wybor_funkcji, liczba_wezlow, stopien_wielomianu):
    tabCk = tablicaCk(wybor_funkcji, liczba_wezlow, stopien_wielomianu)
    w = np.zeros(liczba_wezlow)
    wynik = 0
    for i in range(liczba_wezlow):
        for j in range(stopien_wielomianu + 1):
            w[i] += tabCk[j] * wielomianLaguerra(j, (wspolczynniki(liczba_wezlow, i)[0]))

    for i in range(liczba_wezlow):
        Ak = wspolczynniki(liczba_wezlow, i)[1]
        x = wspolczynniki(liczba_wezlow, i)[0]
        wynik += Ak * ((wartosc_funkcji(x, wybor_funkcji) - w[i]) ** 2)
    return wynik ** (0.5)


def wariantStopienWielomianu(wybor_funkcji, liczba_wezlow, a, b, stopien_wielomianu):
    Rysowanie.wyswietl(wybor_funkcji, a, b, liczba_wezlow, stopien_wielomianu)
    print(blad(wybor_funkcji, liczba_wezlow, stopien_wielomianu))


def wariantEpsilon(wybor_funkcji, liczba_wezlow, a, b, epsilon):
    stopien_wielomianu = -1
    for i in range(1, 95):
        wartoscBledu = blad(wybor_funkcji, liczba_wezlow, i)
        if wartoscBledu < epsilon:
            stopien_wielomianu = i
    if stopien_wielomianu > 0 and stopien_wielomianu < 95:
        Rysowanie.wyswietl(wybor_funkcji, a, b, liczba_wezlow, stopien_wielomianu)
        print("Stopien wielomianu: " + (str)(stopien_wielomianu))
        print(blad(wybor_funkcji, liczba_wezlow, stopien_wielomianu))
    else:
        print("Nie udało sie znalezc wielomianu stopnia mniejszego niz 95 ktory spelnialby zadana dokladnosc")