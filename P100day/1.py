# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))
# 
# 
# a = 10
# b = 3
# a += b  # 相当于：a = a + b
# a *= a + 2  # 相当于：a = a * (a + 2)
# print(a)  # 想想这里会输出什么
# 


import random

answer = random.randint(1,100)
counter = 0
while True:
    counter += 1
    number = int(input("请输入您猜的字："))
    if number < answer:
        print("您需要在大一点")
    elif number > answer:
        print("您需要在小一点")
    else:
        print('恭喜您答对了！')
        break
print("您总共猜了%d次" % counter)

if counter > 10:
    print("请给智商充值")

