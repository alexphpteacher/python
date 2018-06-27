"""Основы описания классов 2"""

class Robot:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(self.name + " is busy")

class SmartRobot(Robot):
    def start(self):
        print("I will begin")

    def work(self):
        print("I am preparing to work")
        super().work()

    def finish(self):
        print("I have finished")

class CleverRobot(SmartRobot):
    def work(self):
        self.start()
        super().work()
        self.finish()

    def __str__(self):
        return "I am " + self.name

if __name__ == "__main__":
    print("""
        r1 = Robot()
        r2 = SmartRobot()
        r3 = CleverRobot()

        print('-'*30)
        r1.work()
        print('-'*30)
        r2.work()
        print('-'*30)
        r3.work()
        print('-'*30)

        print(r1)
        print(r2)
        print(r3)
    """)

    r1 = Robot("Tom")
    r2 = SmartRobot("Jerry")
    r3 = CleverRobot("Donald")

    print('-'*30)
    r1.work()
    print('-'*30)
    r2.work()
    print('-'*30)
    r3.work()
    print('-'*30)

    print(r1)
    print(r2)
    print(r3)