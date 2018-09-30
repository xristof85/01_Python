# 1. wczytac dane od usera
# 2. porownac dane z dzielenai do 0
# 3. wyswietlic wiadomosc

input_usera = input("Podaj liczbe: ")
input_usera = int (input_usera) # 123 int
if input_usera % 2 == 0:
    print("Jest podzielna")
else:
    print("Nie jest podzielna")