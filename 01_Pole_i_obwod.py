from math import pi
from math import sqrt
Figura = input ("Wybierz figurę (podaj cyfrę): Kwadrat 1 ; Prostokąt 2 ; Trójkąt 3 ; Romb 4 ; Koło 5  : ")
Figura = int (Figura)
if Figura == 1:
    print ("Wybrałeś Kwadrat")
    a = input ("Podaj długość boku a = ")
    a = float (a)
    P = a ** 2
    O = a * 4
    print ("Pole =", P)
    print ("Obwód =", O)
elif Figura == 2:
    print ("Wybrałeś Prostokąt")
    a = input ("Podaj długość krótszego boku a = ")
    a = float (a)
    b = input ("Podaj długość dłuższego boku b = ")
    b = float (b)
    P = a * b
    O = 2 * a + 2 * b
    print ("Pole =", P)
    print ("Obwód =", O)
elif Figura == 3:
    print ("Wybrałeś Trójkąt")
    Trojkat = input ("Wybierz trójkąt: Równoramienny 1 ; Prostokątny 2 : ")
    Trojkat = int (Trojkat)
    if Trojkat == 1:
        print ("Wybrałeś trójkąt równoramienny")
        a = input ("Podaj podstawę a = ")
        a = float (a)
        h = input ("Podaj wysokość h = ")
        h = float(h)
        b = sqrt (a ** 2 + h ** 2)
        P = round (1 / 2 * a * h , 2)
        O = round (a + 2 * b , 2)
        print ("Pole =", P)
        print("Obwód =", O)
    elif Trojkat == 2:
        print ("Wybrałeś Trójkąt prostokątny")
        a = input ("Podaj podstawę a = ")
        a = float (a)
        h = input ("Podaj wysokość h = ")
        h = float(h)
        b = sqrt (a ** 2 + h ** 2)
        P = round (1 / 2 * a * h , 2)
        O = round (a + b + h , 2)
        print ("Pole =", P)
        print("Obwód =", O)
    else:
        print ("Wybrałeś niepoprawnie")
elif Figura == 4:
    print ("Wybrałeś Romb")
    a = input ("Podaj bok a = ")
    a = float (a)
    h = input ("Podaj wysokość h = ")
    h = float(h)
    P = a * h
    O = 4 * a
    print("Pole =", P)
    print("Obwód =", O)
elif Figura == 5:
    print ("Wybrałeś Koło")
    r = input ("Podaj promień r = ")
    r = float (r)
    P = round (2 * pi * r , 2)
    O = round (pi * r ** 2 ,2)
    print("Pole =", P)
    print("Obwód =", O)
else:
    print ("Wybrałeś niepoprawnie")
print ("Koniec")
import sys
sys.exit();