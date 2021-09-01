def quadrado(x):
    return x ** 2

x = [1, 2, 3, 4, 5]

y = list(map(quadrado, x))

print(y)
print(type(y))