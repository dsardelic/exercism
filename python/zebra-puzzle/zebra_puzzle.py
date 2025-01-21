import copy
import itertools
from dataclasses import dataclass, field
from enum import Enum


class Nationality(Enum):
    ENGLISH = "English"
    NORWEGIAN = "Norwegian"
    SPANISH = "Spanish"
    UKRAINIAN = "Ukrainian"
    JAPANESE = "Japanese"


Beverage = Enum("Beverage", "COFFEE TEA MILK ORANGE_JUICE WATER")
Color = Enum("Color", "RED GREEN YELLOW BLUE IVORY")
Pet = Enum("Pet", "DOG SNAILS FOX HORSE ZEBRA")
Cigarettes = Enum("Cigarettes", "OLD_GOLD KOOLS CHESTERFIELDS LUCKY_STRIKE PARLIAMENTS")


@dataclass
class Solution:
    nationalities: list[Nationality] = field(default_factory=lambda: [None] * 5)
    beverages: list[Beverage] = field(default_factory=lambda: [None] * 5)
    house_colors: list[Color] = field(default_factory=lambda: [None] * 5)
    pets: list[Pet] = field(default_factory=lambda: [None] * 5)
    cigarettes: list[Cigarettes] = field(default_factory=lambda: [None] * 5)


# pylint:disable=W0105,I0023
"""
nationalities.index(Nationality.NORWEGIAN) == 0,
nationalities.index(Nationality.JAPANESE) == cigarettes.index(Cigarettes.PARLIAMENTS),
abs(nationalities.index(Nationality.NORWEGIAN) - house_colors.index(Color.BLUE)) == 1,
beverages.index(Beverage.MILK) == 2,
beverages.index(Beverage.COFFEE) == house_colors.index(Color.GREEN),
cigarettes.index(Cigarettes.LUCKY_STRIKE) == beverages.index(Beverage.ORANGE_JUICE),
nationalities.index(Nationality.ENGLISH) == house_colors.index(Color.RED),
nationalities.index(Nationality.SPANISH) == pets.index(Pet.DOG),
nationalities.index(Nationality.UKRAINIAN) == beverages.index(Beverage.TEA),
abs(house_colors.index(Color.GREEN) - house_colors.index(Color.IVORY)) == 1,
cigarettes.index(Cigarettes.OLD_GOLD) == pets.index(Pet.SNAILS),
cigarettes.index(Cigarettes.KOOLS) == house_colors.index(Color.YELLOW),
abs(cigarettes.index(Cigarettes.CHESTERFIELDS) - pets.index(Pet.FOX)) == 1,
abs(cigarettes.index(Cigarettes.KOOLS) - pets.index(Pet.HORSE)) == 1,
"""


def find_solution():
    solution = None

    def resolve_nationalities(solution):
        solution.nationalities[0] = Nationality.NORWEGIAN
        indices = [
            i for i, nationality in enumerate(solution.nationalities) if not nationality
        ]
        unassigned = set(Nationality) - {
            nationality for nationality in solution.nationalities if nationality
        }
        if not unassigned:
            return
        for permutation in itertools.permutations(unassigned):
            solution_copy = copy.deepcopy(solution)
            for i, index in enumerate[indices]:
                solution.nationalities[index] = permutation[i]

    def resolve_beverages(solution):
        ...

    def resolve_house_colors(solution):
        ...

    def resolve_pets(solution):
        ...

    def resolve_cigarettes(solution):
        ...

    solution = Solution()
    resolve_nationalities(solution)
    return solution


def drinks_water():
    solution = find_solution()
    return solution.nationalities[solution.beverages(Beverage.WATER)].value


def owns_zebra():
    solution = find_solution()
    return solution.nationalities[solution.pets(Pet.ZEBRA)].value


if __name__ == "__main__":
    find_solution()
