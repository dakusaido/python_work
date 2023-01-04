from datetime import datetime


class Event:
    __description = None
    __date = None

    def __init__(self) -> None: ...

    @classmethod
    def from_string(cls, event_and_date: str):
        event_and_date = list(map(lambda string: string.strip(), event_and_date.split("*")))
        cls.__description = event_and_date[0]
        cls.__date = datetime.strptime(event_and_date[1], "%d-%m-%Y").date()
        return super().__new__(cls)

    def __str__(self):
        return f"Description: {self.__description}\n" \
               f"Day:{self.__date.day}\tMonth:{self.__date.month}\tYear:{self.__date.year}"


if __name__ == '__main__':
    new_event = Event.from_string("Meeting with friends * 12-11-2001")
    print(new_event)

