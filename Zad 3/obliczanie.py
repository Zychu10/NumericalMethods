import math
import numpy as np
import matplotlib.pyplot as plt

import wyswietlanie


def przesuw(poczatek, koniec, liczba_wezlow):
    return abs(koniec - poczatek) / liczba_wezlow


def horner(tab, x):
    b = tab[0]
    for i in range(len(tab) - 1):
        b = tab[i + 1] + x * b
    return b


def funkcje(x, numer):
    if numer == 1:
        tabWspol = [1.0, -1.0, -2.0, 1.0]
        return horner(tabWspol, x)
    if numer == 2:
        return math.sin(x) + x - 1
    if numer == 3:
        return 2 * x + 3
    if numer == 4:
        return abs(3 * x - 4)
    if numer == 5:
        return abs(math.sin(x) + x * math.cos(x))


def tworzenie_danych(poczatek, koniec, numer, liczba_wezlow):
    x = []
    y = []
    n = przesuw(poczatek, koniec, liczba_wezlow)
    while (poczatek <= koniec):
        x.append(poczatek)
        poczatek = poczatek + n
    for element in x:
        wynik = funkcje(element, numer)
        y.append(wynik)
    return x, y


def interpolacja(poczatek, koniec, liczba_wezlow, numer):
    x = np.array(tworzenie_danych(poczatek, koniec, numer, liczba_wezlow)[0])
    y = np.array(tworzenie_danych(poczatek, koniec, numer, liczba_wezlow)[1])
    xplt = np.linspace(x[0], x[-1])
    yplt = np.array([])
    for xp in xplt:
        yp = 0
        for xi, yi in zip(x, y):
            yp += yi * np.product((xp - x[x != xi]) / (xi - x[x != xi]))
        yplt = np.append(yplt, yp)


    podzialka = (koniec - poczatek) / 100
    x1 = np.arange(poczatek, koniec + podzialka, podzialka)
    y1 = np.zeros(x1.size)
    for i in range(len(x1)):
        y1[i] = funkcje(x1[i], numer)
    wyswietlanie.title(numer)
    plt.plot(xplt, yplt, 'r--', label = 'interpolacja')
    plt.plot(x, y, 'ro', label = 'wezły')
    plt.plot(x1, y1, label='funkcja bazowa')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(y=0, color="#cccccc")
    plt.axvline(x=0, color="#cccccc")
    plt.legend()
    plt.show()


# wynik = tworzenie_danych(0, 5, 1, 5)
# print(wynik)
# print(interpolacja(0, 5, 5, 1))
