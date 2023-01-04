from PassengerCar import PassengerCar
from Truck import Truck


def main():

    passenger_car: PassengerCar = PassengerCar("Chevrolet", 253)
    truck: Truck = Truck("Volvo", 700)

    passenger_car.drive()
    passenger_car.stop()
    passenger_car.say_manufacturer()

    truck.drive()
    truck.stop()
    truck.say_manufacturer()

    passenger_car.jump()

    truck.load_cargo(10)
    truck.unload_cargo(4)

    truck.get_fullness()


if __name__ == "__main__":
    main()
