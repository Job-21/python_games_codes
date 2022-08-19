class Animal:
    def __init__(self):
        pass
    def show(self):
        print("i am from the animal class.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def show(self):
        super(Fish, self).show()
        print("But so dark")

obj = Fish()
obj.show()