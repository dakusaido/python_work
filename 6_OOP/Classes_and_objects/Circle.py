from math import pi
from decimal import Decimal


class Operation:
    __dict: dict = {}
    __result = Decimal('0')

    def __init__(self, **kwargs):
        self.__dict = kwargs

    def area_circle(self) -> Decimal:
        self.__result = Decimal(pi) * Decimal(self.__dict.get("radius") or 0).__pow__(2)
        return self.__result

    def perimeter_circle(self) -> Decimal:
        self.__result = Decimal(2) * Decimal(pi) * Decimal(self.__dict.get("radius") or 0)
        return self.__result


class Circle:
    __X: int = 0
    __Y: int = 0
    __radius: int = 1
    __arguments: dict = {}
    __operation = None
    __other_radius = None
    __other_x = None
    __other_y = None

    def __init__(self, **kwargs):
        self.__arguments = kwargs

        self.__X = kwargs.get("x") or self.__X
        self.__Y = kwargs.get("y") or self.__Y
        self.__radius = kwargs.get("radius") or self.__radius

        self.__operation = Operation(**kwargs)

    def info(self) -> str:
        return f"Circle position - ({self.__X}, {self.__Y}), radius - {self.__radius}"

    def get_area(self) -> Decimal:
        return self.__operation.area_circle()

    def get_perimeter(self) -> Decimal:
        return self.__operation.perimeter_circle()

    def get_x(self):
        return self.__X

    def get_y(self):
        return self.__Y

    def get_radius(self):
        return self.__radius

    def is_intersection(self, other) -> bool:
        self.__other_radius = other.get_radius()
        self.__other_x = other.get_x()
        self.__other_y = other.get_y()

        return Decimal(self.__radius - self.__other_radius).__pow__(2) <= (
                Decimal(self.__X - self.__other_x).__pow__(2) + Decimal(self.__Y - self.__other_y).__pow__(2)
        ) <= Decimal(self.__radius + self.__other_radius).__pow__(2)


if __name__ == '__main__':
    X: int = 5
    Y: int = 3
    Radius: int = 3

    circle = Circle(
        x=X,
        y=Y,
        radius=Radius
    )

    first_other_circle = Circle(
        x=X + 1,
        y=Y + 2,
        radius=Radius + 1
    )

    second_other_circle = Circle(
        x=X + 2,
        y=Y + 3,
        radius=Radius + 4
    )

    print(circle.info())
    print(first_other_circle.info())
    print(second_other_circle.info())

    print(circle.get_area())
    print(circle.get_perimeter())

    print(circle.is_intersection(first_other_circle))
    print(circle.is_intersection(second_other_circle))
    print(first_other_circle.is_intersection(second_other_circle))
