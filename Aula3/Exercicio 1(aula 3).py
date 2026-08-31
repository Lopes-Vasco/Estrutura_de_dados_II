a = [10, 20, 30]
b = a.copy()

b.append(40)

print("a:", a)
print("b:", b)
print("id(a):", id(a))
print("id(b):", id(b))