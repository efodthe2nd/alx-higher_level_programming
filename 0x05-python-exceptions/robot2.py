class Robot:
    def __init__(self, name=None):
        self.name = name
    def say_hi(self):
        if self.name:
            print("Hi, I am: " + self.name)
        else:
            print("Hi, I am without a Name")
    def set_name(self, name):
        self.name = name
    def set_buildyear(self, build_year):
        self.build_year = build_year
    def get_name(self):
        return self.name
    def get_buildyear(self):
        return self.build_year

x = Robot()
x.say_hi()
x.set_name('David')
x.set_buildyear(1998)
print(x.get_buildyear())
y = Robot()
y.set_name(x.get_name())
print(y.get_name())
y.set_buildyear(1996)
print(y.get_buildyear())
