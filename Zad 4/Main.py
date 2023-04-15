from calkowanie import newton_cotes, gauss

liczba_wezlow = 0
eps = 0.0
wybor_funkcji = ''
menu = True

print("Witaj w programie obliczajacym kwadratury Newtona-Cotes'a oraz Gaussa-Laguerre'a wybranej funkcji ")
while menu:
    print(" 1.wybor funkcji \n 2.zakonczenie programu")
    wybor_menu = input("Dokonaj wyboru: ")
    if wybor_menu == '2':
        print("Zakonczenie programu...")
        menu = False
    elif wybor_menu == '1':
        print("Wybor funkcji: \n A: f(x) = e^(-x) * (x^4 - x^3 - x^2 - x + 1) \n B: f(x) = e^(-x) * |x - 5| \n C: f(x) = e^(-x) * 2^x \n D: f(x) = e^(-x) * sin(x) \n E: f(x) = e^(-x) * (cos(x) - x^3)")
        jest = True
        while jest:
            wybor_funkcji = input("Dokonaj wyboru: ").upper()
            if wybor_funkcji in "ABCDE":
                jest = False
            else:
                print("Prosze wybrac poprawnie funkcje z powyzszych")
        jest = True
        while jest:
            try:
                eps = float(input("Dokladnosc kwadratur Newtona-Cotesa: "))
                jest = False
            except ValueError:
                print("Prosze podac poprawna wartosc dokladnosci")
        if wybor_funkcji in "A":
            print("Funkcja: e^(-x)*(x^4 - x^3 - x^2 - x + 1)")
        elif wybor_funkcji in "B":
            print("Funkcja: e^(-x)*|x - 5|")
        elif wybor_funkcji in "C":
            print("Funkcja: e^(-x)*2^x")
        elif wybor_funkcji in "D":
            print("Funkcja: e^(-x)*sin(x)")
        elif wybor_funkcji in "E":
            print("Funkcja: e^(-x)*(cos(x)-x^3)")
        dokladna_wartosc = round(newton_cotes(wybor_funkcji, 1e-8), 8)
        # obliczenie dokładnej wartości całki. Później bedziemy obliczać na tej podstawie błąd metod
        print(f"Dokladna wartosc: {dokladna_wartosc}")
        for liczba_wezlow in range(2, 6):
            wartosc_gauss = round(gauss(wybor_funkcji, liczba_wezlow), 5)   # obliczenie kwadratury Gaussa
            gaus_proc = round(abs((wartosc_gauss - dokladna_wartosc) / dokladna_wartosc * 100), 2)
            print(f"Liczba węzłów: {liczba_wezlow}, Gauss - Laguerre: {wartosc_gauss}, Blad Gauss - Laguerre: {gaus_proc}%")
        wartosc_newton = round(newton_cotes(wybor_funkcji, eps), 5)  # obliczenie kwadratury Newtona-Cotes'a
        newt_proc = round(abs((wartosc_newton - dokladna_wartosc) / dokladna_wartosc * 100), 2)
        print(f"Wynik dla metody Newtona-Cotesa: {wartosc_newton}, blad Newton-Cotes: {newt_proc}%")
    else:
        print("Prosze wybrac 1 lub 2")

