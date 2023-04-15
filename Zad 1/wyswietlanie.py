import math

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import obliczenia

def wyswielt(numer, a, b, x0):
    podzialka = (b - a) / 100
    x = np.arange(a, b + podzialka, podzialka)
    y = np.zeros(x.size)
    for i in range(len(x)):
        y[i] = obliczenia.funkcje(x[i], numer)

    plt.plot(x0, obliczenia.funkcje(x0, numer),'ro')

    plt.xlabel('oś x')
    plt.ylabel('oś y')

    plt.axhline(y=0, color="#cccccc")
    if 0 >= a and 0 <= b:
        plt.axvline(x=0, color="#cccccc")

    title(numer)

    plt.plot(x, y)
    plt.show()

def wyswietl_calosc(numer):
    x = np.linspace(-30, 30, 1000)
    y = np.zeros(x.size)

    if numer == 1 or numer == 5:
        x = np.linspace(-15, 15, 1000)
        plt.ylim(-100,100)
    for i in range(len(x)):
        y[i] = obliczenia.funkcje(x[i], numer)

    title(numer)

    plt.plot(x,y)
    plt.xlabel('oś x')
    plt.ylabel('oś y')
    plt.axhline(y=0, color="#cccccc")
    plt.axvline(x=0, color="#cccccc")
    plt.show()

def opis():
    function = int(input("Wybor funkcji \n 1. x^3 - x^2 - 2x + 1 \n "
                         "2. sin(x) + x - 1 \n 3. cos(x) - x / 2 "
                         "\n 4. sin(x) - x(cos(x)) "
                         "\n 5. 2^x - 3x  \n"))
    return function

def title(numer):

    if numer == 1:
        plt.title("x^3 - x^2 - 2x + 1")



