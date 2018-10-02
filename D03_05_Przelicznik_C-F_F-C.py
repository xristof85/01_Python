temperature = input("Podaj temeperature i jednostkę: ")
if temperature.endswith("C"):
    F = round((float(temperature[:-1])) * 1.8 + 32, 2)
    print(F, 'F')
elif temperature.endswith("F"):
    C = round(((float(temperature[:-1])) - 32) / 1.8, 2)
    print(C, 'C')
else:
    print("Cos poszlo nie tak")