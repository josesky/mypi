#N = 10
#sum = 0
#count = 0
#print("please input 10 number: ")
#while count < N:
#    number = float(input())
#    sum = sum + number
#    count = count + 1
#average = sum / N
#print('N = {}, sum = {}'.format(N, sum))
#print('Average = {:.2f}'.format(average))


#sum = 0
#for i in range(1,11):
#    sum += 1 / i
#    print('{:2d} {:6.4f}'.format(i, sum))
sticks = 21

print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
print("Whoever will take the last stick will loose")

while True:
    print("Sticks left: ", sticks)
    sticks_taken = int(input("Take sticks(1-4):"))
    if sticks == 1:
        print("You took the last stick, you loose")
        break
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong choice")
        continue
    print("Computer took: ", (5 - sticks_taken), "\n")
    sticks -= 5
