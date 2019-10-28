def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number bwtween 0 and 1: "))
    for i in range(10000000):
        x = 3.9 * x * (1-x)
        print(x)

main()