class Vector:
    def __init__(self, *elements):
        self.elements = elements

    def scale(self, amount):
        return Vector(*(e * amount for e in self.elements))

    def norm(self):
        return sum((e ** 2 for e in self.elements)) ** 0.5

    def __add__(self, other):
        return Vector(*(a + b for a, b in zip(self.elements, other.elements)))
