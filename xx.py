n = input("Podaj liczbe: ")
n = int(n)
for i in range(0, n + 1):
    i = 1
    wynik = 1
    for i in range(2, n + 1):
        wynik = wynik * i
    print(n, "! =", wynik)
    break


wynik = 1
n = input("Podaj liczbe: ")
n = int(n)
for i in range(0, n + 1):
    if (n == 0 or n == 1):
        wynik = wynik
    else:
        for i in range(2, n + 1):
            wynik = wynik * i
    print(n, "! =", wynik)
    break