"""Основы описания классов 4"""

class Named:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name

class Aged:
    def __init__(self, age):
        self.__age = age

    def __str__(self):
        return "I am " + str(self.__age) + " years old"

    def getAge(self):
        return self.__age

if __name__ == "__main__":
    print("""
        name = Named("alex")
        age = Aged(22)

        print(name)
        print(age)

        print(name.name)
        print(age.getAge())
        print(age.age)
    """)

    name = Named("alex")
    age = Aged(22)

    print(name)
    print(age)

    print(name.name)
    print(age.getAge())
    print(age.age)