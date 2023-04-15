import Aproksymacja

menu = True

while menu:

    liczba_wezlow = -1
    eps = -1
    stopienWielomianu = -1
    wybor_funkcji = "Brak"
    przedzialA = -1
    przedzialB = -1

    wariant = -1

    print(" 1.wybor funkcji \n 2.zakonczenie programu")
    wybor_menu = input("Dokonaj wyboru: ")

    if wybor_menu == '2':
        print("Zakonczenie programu...")
        menu = False
    elif wybor_menu == '1':
        print("Wybor funkcji: \n A: f(x) = 2x^3-4x^2+8x-3 \n B: f(x) = |x| \n C: f(x) = x + 4 \n D: f(x) = cos(x) \n E: f(x) = x^3 \n F: f(x) = 1-exp^(-x)")
        jest = True

        while jest:

            jest = False
            while wybor_funkcji not in "A B C D E F":
                wybor_funkcji = (input("Dokonaj wyboru: ").upper())

            while (przedzialA == -1 and przedzialB == -1):
                przedzialA = (int)(input("Podaj poczatek przedzialu: "))
                przedzialB = (int)(input("Podaj koniec przedzialu: "))

            while not (liczba_wezlow > 1 and liczba_wezlow < 6):
                liczba_wezlow = (int)(input("Podaj liczbe wezlow: "))

            while not (wariant == 1 or wariant == 2):
                wariant = (int)(input("Wybierz wariant: 1. Podana dokladnosc 2. Z gory okreslony stopien wielomianu "))

                if wariant == 1:
                    eps = (float)(input("Podaj dokladnosc: "))

                elif wariant == 2:
                    while not (stopienWielomianu > 0 and stopienWielomianu < 95):
                        stopienWielomianu = (int)(input("Podaj stopien wielomianu: "))

            if wybor_funkcji in "A":
                print("Funkcja: 2x^3-4x^2+8x-3")
            elif wybor_funkcji in "B":
                print("Funkcja: |x|")
            elif wybor_funkcji in "C":
                print("Funkcja: x+4")
            elif wybor_funkcji in "D":
                print("Funkcja: cos(x)")
            elif wybor_funkcji in "E":
                print("Funkcja: x^3)")
            elif wybor_funkcji in "F":
                print("Funkcja: 1-exp^(-x)")

            if wariant == 1:
                Aproksymacja.wariantEpsilon(wybor_funkcji, liczba_wezlow, przedzialA, przedzialB, eps)
            elif wariant == 2:
                Aproksymacja.wariantStopienWielomianu(wybor_funkcji, liczba_wezlow, przedzialA, przedzialB,
                                                      stopienWielomianu)
    else:
        print("Prosze wybrac 1 lub 2")