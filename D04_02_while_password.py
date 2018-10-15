password = input("Podaj hasło: ")
while len(password) < 6:
    print("Hasło za krótkie")
    password = input("Podaj hasło: ")