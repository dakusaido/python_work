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

