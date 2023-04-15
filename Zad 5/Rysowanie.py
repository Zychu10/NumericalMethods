import numpy as np
from matplotlib import pyplot as plt

import Aproksymacja


def wyswietl(wybor_funkcji, a, b, licza_wezlow, stopienWielonianu):
    x = np.linspace(a, b, 1000)
    y = []
    y2 = []
    for i in x:
        y.append(Aproksymacja.wartosc_funkcji(i, wybor_funkcji))
    x2 = np.linspace(a, b, 1000)
    for i in x2:
        y2.append(Aproksymacja.aproksymacjaFunkcja(wybor_funkcji, licza_wezlow, stopienWielonianu, i))
    plt.plot(x, y)
    plt.plot(x2, y2)
    plt.xlabel('oś x')
    plt.ylabel('oś y')
    plt.grid()
    plt.show()
