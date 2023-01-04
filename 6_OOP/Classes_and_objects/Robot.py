class Robot:
    __power = None

    def __init__(self, power):
        self.__power = power

    power = property()

    @power.getter
    def power(self):
        return self.__power

    @power.setter
    def power(self, value) -> None:
        self.__power = value if value > 0 else 0

    @power.deleter
    def power(self):
        print(f"deleting power in {self.__class__}")
        self.__power = None

    def __str__(self):
        return f"{self.__power=}"


if __name__ == '__main__':
    robot = Robot(3)

    robot.power = -2
    print(robot)

    del robot.power