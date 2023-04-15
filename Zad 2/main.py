import wczytywanie
import obliczanie_fixed

if __name__ == '__main__':

    kontynuuj = True
    while (kontynuuj):
        ite = 9999999999
        eps = -1
        obliczanie_fixed.wyswietlanie()
        plik = int(input("Wybierz numer od 1 do 10, który układ chcesz wczytać \n"))
        wybor = int(input("1. Iteracje 2. Epsilon \n"))
        if (wybor == 1):
            ite = int(input("Podaj ilosc iteracji \n"))
        else:
            eps = float(input("Podaj dokladnosc epsilon \n"))

        A = wczytywanie.przypisywanie_macierzyA(plik)
        b = wczytywanie.przypisywanie_macierzyB(plik)

        print(obliczanie_fixed.algortimhJacobi(A, b, ite, eps))

        if(obliczanie_fixed.dominujaca_przekatna(A)):
            print("Macierz spełnia warunek wystarczajacy zbieznosci")
        else:
            print("Macierz nie spełnia warunku wystarczajacego zbieznosci")

        wybor = str(input("Czy chcesz obliczyc inna macierz T/N: \n"))
        if (wybor == 'T' or wybor == 't'):
            kontynuuj = True
        else:
            kontynuuj = False
