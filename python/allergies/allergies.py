from enum import IntFlag


class Allergy(IntFlag):
    # pylint:disable=invalid-name
    eggs = 1
    peanuts = 2
    shellfish = 4
    strawberries = 8
    tomatoes = 16
    chocolate = 32
    pollen = 64
    cats = 128
    # pylint:enable=invalid-name


class Allergies:
    def __init__(self, score):
        self._allergy = Allergy(score)

    def allergic_to(self, item):
        return bool(self._allergy & getattr(Allergy, item))

    @property
    def lst(self):
        return [
            allergen.name for allergen in Allergy if self.allergic_to(allergen.name)
        ]
