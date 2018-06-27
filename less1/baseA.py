"""Основы описания классов """

class Robot:
    def work(self):
        print("I am busy")

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
    """)

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