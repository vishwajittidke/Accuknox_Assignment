class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# example usage
rect = Rectangle(10, 5)

# iterate over the rectangle instance
for dimension in rect:
    print(dimension)
