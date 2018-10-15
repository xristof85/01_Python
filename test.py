for i in range(0, 10, 3):
    print(i)

a = ['Marysia', 'miała', 'małego', 'baranka']
for i in range(len(a)):
    print(i, a[i])

print(range(5))
print(list(range(5)))

r = range(0, 20, 2)
print(r)
print(11 in r)
print(10 in r)
print(r.index(10))
print(r[5])
print(r[:5])
print(r[-1])

#a, b = 0, 1
#while a < 10:
#print(a)
#a, b = b, a+b