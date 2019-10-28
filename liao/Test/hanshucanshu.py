def power(x,n=1):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(15))
print(power(135,100))