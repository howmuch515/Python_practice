class Professor():
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print("I'am {}!".format(self.name))


class Ryoichi(Professor):
    def __init__(self):
        super().__init__("Ryoichi")

    def greet2(self):
        print("I love Security!")


inomata = Professor("Atsuo")
inomata.greet()

sasaki = Ryoichi()
sasaki.greet()
sasaki.greet2()
