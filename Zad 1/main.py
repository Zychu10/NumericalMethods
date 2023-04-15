import obliczenia
import wyswietlanie

eps = -1
ite = 999999999
function = 1
wyborStopu = -1
przedzialA = -1
przedzialB = -1
DOKLADNOSC = 1
ITERACJE = 2

def startWyswietl():

    global function, wyborStopu, przedzialA, przedzialB, eps, ite

    kontynuuj = True

    function = wyswietlanie.opis()
    wyswietlanie.wyswietl_calosc(function)

def startOblicz():

        global function, wyborStopu, przedzialA, przedzialB, eps, ite

        function = wyswietlanie.opis()
        wyborStopu = int(input(
            "Wybor kryterium stopu \n 1. Osiągnięcie zadanej dokładności obliczeń \n 2. Wykonanie określonej przez użytkownika liczby iteracji. \n "))
        przedzialA = float(input("Wybor lewego kranca "))
        przedzialB = float(input("Wybor prawego kranca "))
        if wyborStopu == DOKLADNOSC:
            eps = float(input("Podaj dokladnosc eps "))
        if wyborStopu == ITERACJE:
            ite = int(input("Podaj ilosc iteracji "))

        x0 = obliczenia.bisekcja(function, przedzialA, przedzialB, eps, ite)

        while x0:
            wynik = int(input("Wyswietl wynik: \n 1. bisekcji \n 2. falsi \n 3. obydwie metody \n"))

            if (wynik == 1 or wynik == 3):
             print("Wynik (bisekcja) wyswietlono w postaci: Pierwsza kolumna to miejsce zerowe, a drugie to ilość iteracji")
             x0 = obliczenia.bisekcja(function, przedzialA, przedzialB, eps, ite)
             print(obliczenia.bisekcja(function, przedzialA, przedzialB, eps, ite))
             wyswietlanie.wyswielt(function, przedzialA, przedzialB, x0[0])
             x0 = False

def main():

    kontynuuj = True

    while(kontynuuj):

        numer = int(input("Co chcesz zrobić? \n 1. Narysować cały wykres funkcji? \n 2. Policzyć miejsce zerowe? \n"))

        if(numer == 1):
            startWyswietl()
        elif(numer == 2):
            startOblicz()
        else:
            print("Podano zly numer")

        decyzja = input("Czy chcesz zakonczyc program t/n: ")
        if decyzja == ("t" or "T"):
             kontynuuj = False

    return 0

if __name__ == '__main__':
    main()