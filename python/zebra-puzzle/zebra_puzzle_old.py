import collections
import itertools
from enum import Enum


class Nationality(Enum):
    ENGLISH = "English"
    NORWEGIAN = "Norwegian"
    SPANISH = "Spanish"
    UKRAINIAN = "Ukrainian"
    JAPANESE = "Japanese"


Color = Enum("Color", "RED GREEN YELLOW BLUE IVORY")
Pet = Enum("Pet", "DOG SNAILS FOX HORSE ZEBRA")
Cigarettes = Enum("Cigarettes", "OLD_GOLD KOOLS CHESTERFIELDS LUCKY_STRIKE PARLIAMENTS")
Beverage = Enum("Beverage", "COFFEE TEA MILK ORANGE_JUICE WATER")

Solution = collections.namedtuple(
    "Solution", "nationalities house_colors pets cigarettes beverages"
)


def find_solution():
    for nationalities, beverages, house_colors, pets, cigarettes in itertools.product(
        itertools.permutations(Nationality),
        itertools.permutations(Beverage),
        itertools.permutations(Color),
        itertools.permutations(Pet),
        itertools.permutations(Cigarettes),
    ):
        if all(
            (
                nationalities.index(Nationality.NORWEGIAN)  # pylint:disable=C1805,I0023
                == 0,
                beverages.index(Beverage.MILK) == 2,
                nationalities.index(Nationality.ENGLISH)
                == house_colors.index(Color.RED),
                nationalities.index(Nationality.SPANISH) == pets.index(Pet.DOG),
                beverages.index(Beverage.COFFEE) == house_colors.index(Color.GREEN),
                nationalities.index(Nationality.UKRAINIAN)
                == beverages.index(Beverage.TEA),
                abs(house_colors.index(Color.GREEN) - house_colors.index(Color.IVORY))
                == 1,
                cigarettes.index(Cigarettes.OLD_GOLD) == pets.index(Pet.SNAILS),
                cigarettes.index(Cigarettes.KOOLS) == house_colors.index(Color.YELLOW),
                abs(cigarettes.index(Cigarettes.CHESTERFIELDS) - pets.index(Pet.FOX))
                == 1,
                abs(cigarettes.index(Cigarettes.KOOLS) - pets.index(Pet.HORSE)) == 1,
                cigarettes.index(Cigarettes.LUCKY_STRIKE)
                == beverages.index(Beverage.ORANGE_JUICE),
                nationalities.index(Nationality.JAPANESE)
                == cigarettes.index(Cigarettes.PARLIAMENTS),
                abs(
                    nationalities.index(Nationality.NORWEGIAN)
                    - house_colors.index(Color.BLUE)
                )
                == 1,
            )
        ):
            return Solution(
                nationalities=nationalities,
                house_colors=house_colors,
                pets=pets,
                cigarettes=cigarettes,
                beverages=beverages,
            )


def drinks_water():
    solution = find_solution()
    return solution.nationalities[solution.beverages(Beverage.WATER)].value


def owns_zebra():
    solution = find_solution()
    return solution.nationalities[solution.pets(Pet.ZEBRA)].value


if __name__ == "__main__":
    find_solution()
