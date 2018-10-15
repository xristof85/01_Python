a = "*"
b = 1
height = int(input("Podaj wysokość: "))
for b in range(0, height + 1):
    c = b * a
    print((height - b) * " ", c)

