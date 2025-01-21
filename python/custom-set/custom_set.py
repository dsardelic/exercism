class CustomSet:
    def __init__(self, elements: list = None):
        self._elements = elements if elements else []

    def isempty(self):
        return not self._elements

    def __contains__(self, element):
        return element in self._elements

    def issubset(self, other):
        return all(element in other for element in self)

    def isdisjoint(self, other):
        return all(element not in other for element in self)

    def __eq__(self, other):
        return (
            isinstance(other, CustomSet)
            and len(self) == len(other)
            and all(element in other for element in self)
            and all(element in self for element in other)
        )

    def add(self, element):
        if element not in self:
            self._elements.append(element)
        return self

    def intersection(self, other):
        return CustomSet([element for element in self if element in other])

    def __sub__(self, other):
        result = CustomSet(self._elements)
        for element in other:
            if element in result:
                result._elements.remove(element)
        return result

    def __add__(self, other):
        return CustomSet(
            self._elements + [element for element in other if element not in self]
        )

    def __repr__(self):
        return f"CustomSet({self._elements})"

    def __hash__(self):
        return hash(self._elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        return iter(self._elements)

    def __next__(self):
        return next(self._elements)
