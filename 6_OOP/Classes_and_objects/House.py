class Color:
    white: str = "white"
    red: str = "red"
    black: str = "black"


class House:
    """ Base class for initialization "House" """

    __count_floor: int = 10
    __color: str = Color.white
    __have_balcony: bool = True

    def __init__(self, count_floor: int, color: str, have_balcony: bool):
        self.__count_floor = count_floor
        self.__color = color
        self.__have_balcony = have_balcony

    def __str__(self) -> str:
        return f"{self.__color.capitalize()} House have {self.__count_floor} floor/floors " \
               f"and {'dont have' if not self.__have_balcony else ''} balcony"

    def get_floor(self) -> int:
        return self.__count_floor

    def get_color(self) -> str:
        return self.__color

    def get_having_balcony(self) -> bool:
        return self.__have_balcony

    def add_floor(self, floor_count: int) -> None:
        if floor_count < 0:
            raise Exception(f"\"floor_count\" must not have a negative value. [{floor_count=}]")

        self.__count_floor += floor_count


if __name__ == "__main__":
    color: Color = Color()

    floor: int = 5
    house_color: str = color.black
    have_balcony: bool = True

    house = House(count_floor=floor,
                  color=house_color,
                  have_balcony=have_balcony)

    print(house)

    house.add_floor(floor_count=5)
    print(house)

    house.add_floor(floor_count=-4)
    print(house)
