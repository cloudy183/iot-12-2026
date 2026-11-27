
from enum import Enum


class CandyType(Enum):
    BAR = 1
    BUTTON = 2
    POPCORN = 3
    GUM = 4


class Candy:
    def __init__(self, name, mass, amount, price, candy_type):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(mass, (int, float)) or mass <= 0:
            raise ValueError("Mass must be a positive number")
        if not isinstance(amount, int) or isinstance(amount, bool) or amount <= 0:
            raise ValueError("Amount must be a positive integer")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number")
        if not isinstance(candy_type, CandyType):
            raise TypeError("Invalid candy type")

        self.__name = name
        self.__mass = mass
        self.__amount = amount
        self.__price = price
        self.__type = candy_type

    @property
    def name(self):
        return self.__name

    @property
    def mass(self):
        return self.__mass

    @property
    def amount(self):
        return self.__amount

    @property
    def price(self):
        return self.__price

    @property
    def type(self):
        return self.__type

    def ate(self):
        if self.__mass * self.__amount > 2000:
            return "You're on a diet!"
        return "What delicious candies!"

    def show(self):
        print(
            self.__name,
            self.__mass, "г",
            self.__amount, "шт",
            self.__price, "грн",
            self.__type.name
        )


class Dinner:
    def __init__(self, day="Невідомо", time="00:00", candies=None):
        self.__day = day
        self.__time = time
        self.__candies = list(candies) if candies is not None else []

        if not all(isinstance(candy, Candy) for candy in self.__candies):
            raise TypeError("All elements must be Candy objects")

    @property
    def day(self):
        return self.__day

    @property
    def time(self):
        return self.__time

    @property
    def candies(self):
        return self.__candies.copy()

    def show(self):
        print("Вечеря:", self.__day, self.__time)
        for candy in self.__candies:
            candy.show()


def get_value(candy, parameter):
    if parameter == "name":
        return candy.name
    elif parameter == "mass":
        return candy.mass
    elif parameter == "amount":
        return candy.amount
    elif parameter == "price":
        return candy.price
    else:
        raise ValueError("Unknown sorting parameter")


def sort_candies(candies, parameter):
    return sorted(
        candies,
        key=lambda candy: get_value(candy, parameter)
    )


def find_the_most_expensive_candies(candies, name):
    suitable = [
        candy for candy in candies
        if name == "" or name.lower() in candy.name.lower()
    ]

    suitable = sort_candies(suitable, "price")
    suitable.reverse()

    return suitable[:3]


def main():
    candy1 = Candy("Шоколадка", 100, 5, 35.5, CandyType.BAR)
    candy2 = Candy("Ґудзики", 20, 10, 12, CandyType.BUTTON)
    candy3 = Candy("Попкорн", 150, 20, 60, CandyType.POPCORN)
    candy4 = Candy("Жуйка", 15, 4, 25, CandyType.GUM)

    candies = [candy1, candy2, candy3, candy4]

    print("Усі цукерки:")
    for candy in candies:
        candy.show()

    print("\nДоступ через property:")
    print(candy1.name)
    print(candy1.price)
    print(candy1.type.name)

    print("\nМетод ate:")
    print(candy1.ate())
    print(candy3.ate())

    print("\nТоп 3 найдорожчих:")
    for candy in find_the_most_expensive_candies(candies, ""):
        candy.show()

    print("\nСортування за масою:")
    sorted_candies = sort_candies(candies, "mass")
    for candy in sorted_candies:
        candy.show()

    print("\nВечеря:")
    dinner = Dinner("П'ятниця", "19:00", [candy1, candy2])
    dinner.show()

    print("\nДоступ до властивостей вечері:")
    print(dinner.day, dinner.time)


if __name__ == "__main__":
    main()
