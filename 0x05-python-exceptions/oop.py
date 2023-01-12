class Person:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print("My name is ", self.name)

p = Person("David")
p.sayHi()
