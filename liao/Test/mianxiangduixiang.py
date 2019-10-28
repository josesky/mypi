#class Student(object):
#    pass
#bart = Student()
#print(bart)
#print(Student)
#
#bart.name = 'Bart Simpson'
#print(bart.name)
#
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

bart = Student('Bart Simpson', 59)
liu = Student('Liu li', 80)
print(bart.name)
print(bart.score)

def print_score(std):
    print('%s: 数学 = %s' % (std.name, std.score))

print_score(liu)


print((4+8)/2)

print(20 // 6)

print(1.25 % 0.5)

ra