#print("PYTHON"[::-1]) #odwraca kolejnosc
#print("PYTHON"[1::-1])
#print("PYTHON"[:-3:-1])
#print("PYTHON"[:-3:-2])

#str = "xoooxxxox"

str = input("wprowadz: ")
if str[0] == str[4] == str[8]:
    if str[0] == 'x':
        print("Wygral x")
    else:
        print("Wygral o")
elif str[2] == str[4] == str[6]:
    if str[0] == 'x':
        print("Wygral x")
    else:
        print("Wygrał o")
elif str[0] == str[1] == str[2]:
    if str[0] == 'x':
        print("Wygral x")
    else:
        print("Wygrał o")
elif str[3] == str[4] == str[5]:
    if str[3] == 'x':
        print("Wygral x")
    else:
        print("Wygrał o")
elif str[6] == str[7] == str[8]:
    if str[6] == 'x':
        print("Wygral x")
    else:
        print("Wygral o")
elif str[0] == str[3] == str[6]:
    if str[0] == 'x':
        print("Wygral x")
    else:
        print("Wygral o")
elif str[1] == str[4] == str[7]:
    if str[1] == 'x':
        print("Wygral x")
    else:
        print("Wygral o")
elif str[2] == str[5] == str[8]:
    if str[2] == 'x':
        print("Wygral x")
    else:
        print("Wygral o")
else:
    print("remis")
