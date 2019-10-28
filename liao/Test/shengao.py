
height = 1.75
weight = 80.5

bmi = (weight/height**2)

if bmi < 18.5:
    print('过轻')
elif 18.5 < bmi < 25:
    print('正常')
elif 25 < bmi < 28:
    print('过重')
else:
    print('哈哈，我不说你了')

print(bmi)