dana = input("Podaj imie i numer: ")
x = len(str(dana[:-2]))
y = len(str(dana[-2:]))
print('Liczba liter: ', x)
print('Liczba cyfr: ', y)



# tutaj luźne przemyślenia i pomysły, ale nie działają
#dana = input("Podaj imie i numer: ")
#for i in range(0, len(dana)):
#    if






#dana = input("Podaj imie i numer: ")
#for i in range(0, len(dana)):
#    if dana[:len(dana)-3] == '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
#        x = len(str(dana[:-3]))
#        y = len(str(dana[-3:]))
#    elif dana[:len(dana)-2] == '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
#        x = len(str(dana[:-2]))
#        y = len(str(dana[-2:]))
#    elif dana[:len(dana)-1] == '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
#        x = len(str(dana[:-1]))
#        y = len(str(dana[-1:]))
#    print('Liczba liter: ', x)
#    print('Liczba cyfr: ', y)
#    break





