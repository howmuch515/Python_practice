class Student():
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def showData(self):
        print(self.id)
        print(self.name)
        print(self.age)


s = Student("15fi000", "DendaiTaro", 22)
s.showData()
