sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

sum1 = 0

for x in list(range(101)):
    sum1 = sum1 + x
print(sum1)


sum2 = 0
n = 99999
while n > 0:
    sum2 = sum2 + n
    n = (n * 2)/4 - 1
print(sum2)
