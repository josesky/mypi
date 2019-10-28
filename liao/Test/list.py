# print(list(range(101)))



g = ((x * x for x in range(1, 11)))
for i in g:
    print(i)

print(next(g))

print(list(range(10)))

