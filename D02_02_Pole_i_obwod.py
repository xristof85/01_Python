from math import pi
from math import sqrt
Figure = input("Wybierz figurę (podaj cyfrę): Kwadrat 1 ; Prostokąt 2 ; Trójkąt 3 ; Romb 4 ; Koło 5  : ")
if Figure == '1':
    print("Wybrałeś Kwadrat")
    a = input("Podaj długość boku a = ")
    a = float(a)
    Surface = a ** 2
    Circuit = a * 4
    print("Pole =", Surface)
    print("Obwód =", Circuit)
elif Figure == '2':
    print("Wybrałeś Prostokąt")
    a = input("Podaj długość krótszego boku a = ")
    a = float(a)
    b = input("Podaj długość dłuższego boku b = ")
    b = float(b)
    Surface = a * b
    Circuit = 2 * a + 2 * b
    print("Pole =", Surface)
    print("Obwód =", Circuit)
elif Figure == '3':
    print("Wybrałeś Trójkąt")
    Triangle = input("Wybierz trójkąt: Równoramienny 1 ; Prostokątny 2 : ")
    if Triangle == '1':
        print("Wybrałeś trójkąt równoramienny")
        a = input("Podaj podstawę a = ")
        a = float(a)
        h = input("Podaj wysokość h = ")
        h = float(h)
        b = sqrt(a ** 2 + h ** 2)
        Surface = round(0.5 * a * h, 2)
        Circuit = round(a + 2 * b, 2)
        print("Pole =", Surface)
        print("Obwód =", Circuit)
    elif Triangle == '2':
        print("Wybrałeś Trójkąt prostokątny")
        a = input("Podaj podstawę a = ")
        a = float(a)
        h = input("Podaj wysokość h = ")
        h = float(h)
        b = sqrt(a ** 2 + h ** 2)
        Surface = round(1 / 2 * a * h, 2)
        Circuit = round(a + b + h, 2)
        print("Pole =", Surface)
        print("Obwód =", Circuit)
    else:
        print("Coś poszło nie tak!")
elif Figure == '4':
    print("Wybrałeś Romb")
    a = input("Podaj bok a = ")
    a = float(a)
    h = input("Podaj wysokość h = ")
    h = float(h)
    Surface = a * h
    Circuit = 4 * a
    print("Pole =", Surface)
    print("Obwód =", Circuit)
elif Figure == '5':
    print("Wybrałeś Koło")
    r = input("Podaj promień r = ")
    r = float(r)
    Surface = round(2 * pi * r, 2)
    Circuit = round(pi * r ** 2, 2)
    print("Pole =", Surface)
    print("Obwód =", Circuit)
else:
    print("Coś poszło nie tak!")
print("Koniec")
import sys
sys.exit();