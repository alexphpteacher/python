"""Основы описания классов 5"""


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

class People(Named, Aged):
    def __init__(self, name, age):
        Named.__init__(self, name)
        Aged.__init__(self, age)

    def __str__(self):
        return Named.__str__(self) + " " + Aged.__str__(self)

class SexPeople(People):
    def who(self):
        return self.sex + " " + self.name

class Man(SexPeople):
    def __init__(self, *arg):
        super().__init__(*arg)
        self.sex = "Mr"

class Woman(SexPeople):
    def __init__(self, *arg):
        super().__init__(*arg)
        self.sex = "Ms"

if __name__ == "__main__":
    print("""
        m = Man("alex", 22)
        w = Woman("olga", 34)

        print(m)
        print(w)

        print(m.who())
        print(w.who())
    """)

    m = Man("alex", 22)
    w = Woman("olga", 34)

    print(m)
    print(w)

    print(m.who())
    print(w.who())