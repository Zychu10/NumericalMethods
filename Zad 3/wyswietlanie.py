import matplotlib.pyplot as plt
import numpy as np
import main


def opis():
   print("Wybor funkcji \n 1. x^3 - x^2 - 2x + 1 \n "
                         "2. sin(x) + x - 1 \n 3. 2x + 3 "
                         "\n 4. |3x -4|"
                         "\n 5. |sinx + xcosx|  \n")



def title(numer):
    if numer == 1:
        plt.title("x^3 - x^2 - 2x + 1")
    if numer == 2:
        plt.title("sin(x) + x - 1")
    if numer == 3:
        plt.title("2x + 3")
    if numer == 4:
        plt.title("|3x -4|")
    if numer == 5:
        plt.title("|sinx + xcosx| ")



