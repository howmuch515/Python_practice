class Person():
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def greet(self):
        print("{0} {1} sai!".format(self.name, self.age))

p = Person(17, "Tamura Yukari")
p.greet()
