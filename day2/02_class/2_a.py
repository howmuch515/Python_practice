class Person():
    age = 17
    name = "Tamura Yukari"

    def greet(self):
        print("{0} {1} sai!".format(self.name, self.age))

p = Person()
p.greet()

p.age = 41
p.greet()
