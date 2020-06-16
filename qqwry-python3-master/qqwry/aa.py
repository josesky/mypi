from qqwry import QQwry

with open('ip.txt', 'r') as f:
    #print(f.readline())

    for line in f.readlines():
        #llip = print(line.strip())
    #    print(line)

        q = QQwry()
        q.load_file('qqwry.dat')
        print(line)
        result = q.lookup(line)
        print(result)
