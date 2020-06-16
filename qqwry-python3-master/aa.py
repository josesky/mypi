from qqwry import QQwry


q = QQwry()
q.load_file('qqwry.dat')
result = q.lookup('223.5.5.5')
