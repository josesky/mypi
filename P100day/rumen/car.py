class Car():
    """模拟汽车"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """打印汽车里程数"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读书设置为指定的值
        禁止里程表回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back odometer")

    def increment_odometer(self, milege):
        """将里程表增加的量"""
        self.odometer_reading += milege


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(33)
my_new_car.read_odometer()

my_new_car.increment_odometer(300)
my_new_car.read_odometer()