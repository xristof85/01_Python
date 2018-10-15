# 1. zliczanie liczb parzystych i nieparzystych w zakresie do 100
# 2. ciąg Fibonacciego do 100
# 3. silnia (n)

a = 0
b = 0
for c in range(100):
    if c % 2 == 0:
        a += 1   #zamiast a = a + 1 zamiennie można użyć a += 1 oraz doodejmij-= domnóż *= dodziel/=
    else:
        b += 1   #zamiast b = b + 1 zamiennie można użyć b += 1
print("Ilosc parzystych", a)
print("Ilosc nieparzystych", b)

c = "Ilosc parzystych {}. Ilosc nieparzystych {}" .format(a, b)
print(c)

d = f"Ilosc parzystych {a}. Ilosc nieparzystych {b}"
print(d)