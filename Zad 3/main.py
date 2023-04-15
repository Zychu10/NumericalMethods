import obliczanie
import wyswietlanie


if __name__ == '__main__':
    kontynuuj = True
    while(kontynuuj):
        wyswietlanie.opis()
        numer = int(input("Wybierz numer funkcji \n"))
        poczatek = float(input("Wybierz poczatek przedzialu \n"))
        koniec = float(input("Wybierz koniec przedzialu \n"))
        wezel = True
        while(wezel):
            wezly = int(input("Wybierz  liczbe wezlow  \n"))
            if (wezly == 1):
                print("Liczba wezłów musi być większa od 1!")
                wezel = False
            else:
                obliczanie.interpolacja(poczatek, koniec, wezly - 1, numer)
                wezel = False
        wybor = str(input("Czy chcesz narysowac inna funkcje? T/N \n" ))
        if (wybor == 'T' or wybor == 't'):
            kontynuuj = True
        else:
            kontynuuj = False
