class Auto:
    __Manufacturer: str = ""

    def __init__(self, manufacturer: str):
        self.__Manufacturer = manufacturer if isinstance(manufacturer, str) else ""

    def say_manufacturer(self):
        print(self.__Manufacturer)
        return self.__Manufacturer

    def drive(self):
        print("Driving")
        ...

    def stop(self):
        print("Stop")
        ...


class PassengerCar(Auto):
    __horsepower: int = 0

    def __init__(self, manufacturer: str, horsepower: int):
        super().__init__(manufacturer)
        self.__horsepower = horsepower if isinstance(horsepower, int) else 0

    def jump(self):
        print("Jumping")
        ...


class Truck(Auto):
    __fullness: int = 0

    def __init__(self, manufacturer: str, fullness: int):
        super().__init__(manufacturer)
        self.__fullness = fullness if isinstance(fullness, int) else 0

    def load_cargo(self, cargo: int):
        print("Loading")
        self.__fullness += cargo if isinstance(cargo, int) else 0

    def unload_cargo(self, cargo: int):
        print("Unloading")
        self.__fullness -= cargo if isinstance(cargo, int) else 0

    def get_fullness(self) -> int:
        print(self.__fullness)
        return self.__fullness


if __name__ == '__main__':
    # passenger_car: PassengerCar = PassengerCar("Chevrolet", 253)
    # truck: Truck = Truck("Volvo", 700)
    #
    # passenger_car.drive()
    # passenger_car.stop()
    # passenger_car.say_manufacturer()
    #
    # truck.drive()
    # truck.stop()
    # truck.say_manufacturer()
    #
    # passenger_car.jump()
    #
    # truck.load_cargo(10)
    # truck.unload_cargo(4)
    #
    # truck.get_fullness()

    print(
        isinstance(Auto(''), Truck),
        isinstance(Truck('', 123), Auto),
        isinstance(Truck, Truck)
    )
