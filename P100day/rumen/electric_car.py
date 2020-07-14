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

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def fill_gas_tank():
        """电动车没有油箱"""
        print("This car doesn't need a gas tank!")
        
my_tesla = ElectricCar('tesla', 'mode s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()