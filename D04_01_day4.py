#while a < 10:
#    a = a + 1
#    if a == 5:
#        continue
#    print(a)

#while True:
#	print(a)
#	a = a + 1
#	if a == 10:
#		break
#print("Koniec")

#spr czy liczba jest parzysta

for number in range(10):
    if number % 2 != 0:
        pass
    else:
        print(number)

for number in range(10):
    if number % 2 != 0:
        continue
        print(number)
    else:
        print(number)
        
for number in range(10):
    if number % 2 != 0:
        break
        print(number)
    else:
        print(number)