year = input("Podaj rok: ")
year = int(year)
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Jest przestepny")
else:
    print("Nie jest przestepny")