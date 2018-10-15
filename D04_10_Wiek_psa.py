a = 10.5
b = 4
year = int(input("Podaj wiek ludzki: "))
if year <= 2:
    year = a * year
else:
    year = 2 * a + (year - 2) * b
print("Wiek psa: ", year)