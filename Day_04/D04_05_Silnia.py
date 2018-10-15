a = 1
n = int(input("Podaj liczbe: "))
if n <= 1:
    a = 1
else:
    for i in range(2, n + 1):
        a *= i
print(n, "! =", a)





#a = 1
#n = input("Podaj liczbe: ")
#n = int(n)
#for i in range(0, n + 1):
#    if n >= 1:
#        a = i
#    else:
#        for i in range(2, n + 1):
#           a *= i
#    print(n, "! =", a)
#    break