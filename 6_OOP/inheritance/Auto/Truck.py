from Auto import Auto


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
