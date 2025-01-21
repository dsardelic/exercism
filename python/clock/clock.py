class Clock:
    def __init__(self, hour, minute):
        self._minute = minute % 60
        self._hour = (minute // 60 + hour) % 24

    def __repr__(self):
        return f"{self.__class__.__name__}({self._hour}, {self._minute})"

    def __str__(self):
        return f"{self._hour:02}:{self._minute:02}"

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self._hour == other._hour
            and self._minute == other._minute
        )

    def __add__(self, minutes):
        return self.__class__(self._hour, self._minute + minutes)

    def __sub__(self, minutes):
        return self + -minutes

    def __hash__(self) -> int:
        return hash((self._hour, self._minute))
