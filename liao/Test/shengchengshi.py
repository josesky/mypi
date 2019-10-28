L = []
for x in range(1, 10):
    L.append(x * x)
print(sum(L))

def add_number(num):
    def adder(number):
        return num + number
    return adder
a_10 = add_number(10)
print(a_10(21))

print(add_number(10))


