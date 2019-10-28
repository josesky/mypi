def change():
    global a
    a = 90
    print(a)
a = 100
print('Before the function call', a)
print('inside change function', end=' ')    
change()
print('After the funcation call', a)