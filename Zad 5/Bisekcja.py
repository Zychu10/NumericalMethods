# import numpy as np
# import Aproksymacja
# import numpy as np
#
# import Aproksymacja
#
#
# def funkcje(x, stopienWielomianu):
#     return Aproksymacja.wielomianLaguerra(stopienWielomianu, x)
#
#
# def bisekcja(stopienWielomianu, poczatek, koniec, eps):
#     fa = funkcje(poczatek, stopienWielomianu)
#     fb = funkcje(koniec, stopienWielomianu)
#     x0 = 0
#     if (fa * fb > 0):
#         return 0
#     else:
#         for licznik in range(1, 99999999):
#             x1 = x0
#             x0 = (poczatek + koniec) / 2
#             if ((abs(x1 - x0) < eps) and licznik > 1):
#                 return x0
#             else:
#                 fx = funkcje(x0, stopienWielomianu)
#             if (fa * fx) <= 0:
#                 koniec = x0
#             else:
#                 poczatek = x0
#                 fa = fx
#
#
# def tablicaWezlow(stopienWielomianu):
#     tablica = np.zeros(stopienWielomianu)
#     epsilon = 0.001
#     licznik = 0
#     x = -99
#     while licznik < stopienWielomianu:
#         a = round(Aproksymacja.wielomianLaguerra(stopienWielomianu, x), 4)
#         if(a < 0.0001 and a > -0.0001):
#             tablica[licznik] = x
#             licznik += 1
#         x += 0.0001
#     return tablica
