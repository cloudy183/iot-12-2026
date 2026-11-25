from enum import Enum


class CandyType(Enum):
    BAR = 1
    BUTTON = 2
    POPCORN = 3
    GUM = 4


class Candy:
    def __init__(self, name="Без назви", mass=0, amount=0, price=0,
                 candy_type=CandyType.BAR):
        self.__name = name
        self.__mass = mass
        self.__amount = amount
        self.__price = price
        self.__type = candy_type

    def __del__(self):
        print("Цукерку", self.__name, "видалено")

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
            print("You're on a diet!")
        else:
            return "What delicious candies!"

    def show(self):
        print(self.__name, self.__mass, "г", self.__amount, "шт",
              self.__price, "грн", self.__type.name)


class Dinner:
    def __init__(self, day="Невідомо", time="00:00", candies=None):
        self.__day = day
        self.__time = time
        if candies is None:
            self.__candies = []
        else:
            self.__candies = candies

    def __del__(self):
        print("Вечерю", self.__day, self.__time, "видалено")

    @property
    def day(self):
        return self.__day

    @property
    def time(self):
        return self.__time

    @property
    def candies(self):
        return self.__candies

    def show(self):
        print("Вечеря:", self.__day, self.__time)
        for candy in self.__candies:
            candy.show()


def get_value(candy, parameter):
    if parameter == "name":
        return candy.name
    if parameter == "mass":
        return candy.mass
    if parameter == "amount":
        return candy.amount
    return candy.price


def sort_candies(candies, parameter):
    for i in range(len(candies)):
        for j in range(len(candies) - i - 1):
            current = get_value(candies[j], parameter)
            following = get_value(candies[j + 1], parameter)
            if current > following:
                candies[j], candies[j + 1] = candies[j + 1], candies[j]


def findTheMostExpensiveCandies(candies, name):
    suitable = []
    for candy in candies:
        if name == "" or name.lower() in candy.name.lower():
            suitable.append(candy)
    sort_candies(suitable, "price")
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

    print()
    print("Доступ через property:")
    print(candy1.name)
    print(candy1.price)
    print(candy1.type.name)

    print()
    print("Метод ate:")
    print(candy1.ate())
    candy3.ate()

    print()
    print("Топ 3 найдорожчих:")
    for candy in findTheMostExpensiveCandies(candies, ""):
        candy.show()

    print()
    print("Сортування за масою:")
    sort_candies(candies, "mass")
    for candy in candies:
        candy.show()

    print()
    dinner = Dinner("П'ятниця", "19:00", [candy1, candy2])
    dinner.show()
    print(dinner.day, dinner.time)


if __name__ == "__main__":
    main()

print()
print("Вечеря:")

candy1 = Candy("Шоколадка", 100, 5, 35.5, CandyType.BAR)
candy2 = Candy("Карамелька", 20, 10, 15, CandyType.BUTTON)
candy3 = Candy("Желейна цукерка", 30, 8, 25, CandyType.GUM)

dinner = Dinner("П'ятниця", "19:00", [candy1, candy2, candy3])

for candy in dinner.candies:
    print(candy.name)