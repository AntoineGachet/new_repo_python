class triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def add(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter


triangle1 = triangle(2, 5, 6)
perimeter = triangle1.add()
print(perimeter)
