class SpaceAge:
    ORBITAL_PERIOD_RATIOS = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    EARTH_YEAR_DURATION = 31_557_600

    def __new__(cls, seconds):
        obj = object.__new__(cls)
        for planet, ratio in cls.ORBITAL_PERIOD_RATIOS.items():
            setattr(
                obj,
                f"on_{planet}",
                lambda ratio=ratio: round(seconds / cls.EARTH_YEAR_DURATION / ratio, 2),
            )
        return obj
