def horner2(lista_wspolczynnikow, arg_x):
    wynik = 0
    for item in reversed(lista_wspolczynnikow):
        wynik = wynik * arg_x + item
    return wynik