a = input("Wprowadz liczbe: ")
checked = False
if a.isdigit() and int(a) % 3 == 0:
    checked = True
    print("jest podzielne przez 3")
if a.isdigit() and int(a) % 5 == 0:
    checked = True
    print("jest podzielne przez 5")
if a.isdigit() and int(a) % 7 == 0:
    checked = True
    print("jest podzielne przez 7")
if a.isdigit() and not checked:
    print("Hej jestem int ale nie jestem podzielny przez 3/5/7")
else:
    print("Wprowadz liczbe")