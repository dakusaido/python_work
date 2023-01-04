from Auto import Auto


class PassengerCar(Auto):

    __horsepower: int = 0

    def __init__(self, manufacturer: str, horsepower: int):
        super().__init__(manufacturer)
        self.__horsepower = horsepower if isinstance(horsepower, int) else 0

    def jump(self):
        print("Jumping")
        ...

