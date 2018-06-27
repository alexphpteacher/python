"""Основы описания классов 3"""

class Named:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name

class Aged:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return "I am " + str(self.age) + " years old"

class Man(Named, Aged):
    def __init__(self, name, age):
        Named.__init__(self, name)
        Aged.__init__(self, age)

    def __str__(self):
        return Named.__str__(self) + " " + Aged.__str__(self)

if __name__ == "__main__":
    print("""
        man1 = Man("alex", 22)
        man2 = Man("tom", 34)

        print(man1.name)
        print(man1.age)

        print(man1)
        print(man2)
    """)

    man1 = Man("alex", 22)
    man2 = Man("tom", 34)

    print(man1.name)
    print(man1.age)

    print(man1)
    print(man2)