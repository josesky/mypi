class Dog():
    """模拟小狗的尝试"""
    def __init__(self, name, age):
        """初始化属性name 和 age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title() + " is now siting.")

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + " rolled over!")


my_dog = Dog("qiqi", 6)
my_dog.sit()
my_dog.roll_over()

your_dog = Dog("lucy", 3)


print("My dog's name is  " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

print("Your dog's name is  " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
