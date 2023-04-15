import math

import matplotlib

def horner(tab, x): #Do funkcji dajemy tablicę współczynników [1, -1, -2, 1] oraz jakas tam wartosc x [w naszym przypadku jest to wartosc poczatkowa i koncowa rozwazanego przedziału]
    b = tab[0]      # b = 1
    for i in range(len(tab)-1): #Po całej tablicy lecimy:
       b = tab[i+1] + x * b     # b = -1 + 0 * -1 = -1 , b = -2 + 0 * -1, b = 1
    return b #zwracamy wartość końcową b
# Powiedzmy, że mamy wyrażenie x^3 - x^2 - 2x + 1

def funkcje(x, numer):
    if numer == 1:
         tabWspol = [1.0,-1.0,-2.0,1.0]
         return horner(tabWspol, x)
    if numer == 2:
        return float(math.sin(x) + x - 1)
    if numer == 3:
        return math.cos(x) - x / 2
    if numer == 4:
        return math.sin(x) - x * math.cos(x)
    if numer == 5:
        return pow(2,x) - 3 * x



def potega(podstawa, potega):
    wynik = 1
    for i in range(potega):
        wynik *= podstawa
    return wynik

def bisekcja(numer, poczatek, koniec, eps, iteracje):
    licznik = 0
    fa = funkcje(poczatek,numer)
    fb = funkcje(koniec, numer)
    x0 = 0
    wynik = False
    if (fa * fb > 0):
        print("Błąd! Znaki funkcji na krańcach nie są różne! bisekcja")
        return wynik
    else:
        wynik = True
        while(wynik):
            for licznik in range(1,iteracje + 1):
                x1 = x0
                x0 = (poczatek + koniec) / 2
                if ((abs(x1 - x0) < eps) and licznik > 1) or licznik >= iteracje:
                    return x0, licznik
                else:
                    fx = funkcje(x0,numer)
                if (fa * fx) <= 0:
                    koniec = x0
                else:
                    poczatek = x0
                    fa = fx

def falsi(numer, poczatek, koniec, eps, iteracje):
    licznik = 0
    fa = funkcje(poczatek, numer)
    fb = funkcje(koniec, numer)
    x0 = 0
    wynik = False
    if (fa * fb > 0):
        print("Błąd! Znaki funkcji na krańcach nie są różne!")
        return wynik
    else:
        wynik = True
        while(wynik):
            for licznik in range(1,iteracje + 1):
                x1 = x0
                x0 = (fa * koniec - fb * poczatek) / (fa - fb)
                fx = funkcje(x0, numer)
                if ((abs(x1 - x0) < eps) and licznik > 1) or licznik >= iteracje:
                    return x0, licznik
                else:
                    if fa * fx < 0:
                        koniec = x0
                        fb = fx
                    else:
                        poczatek = x0
                        fa = fx