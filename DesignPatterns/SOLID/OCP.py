from enum import Enum
from abc import ABC, abstractmethod

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size) -> None:
        self.name = name
        self.color = color
        self.size = size

class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p
    
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    def filter_by_size_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p

#above principal breaks the open closed principle
# what if there are 3 different things then filter methods become too tedious 
# to implement. To mitigate that issue, we have enterprise patterns and one o
# of such patterns is called Specification.


class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

class Filter:
    def filter(self, items, spec):
        pass

class ColorSpecification(Specification):
    def __init__(self, color) -> None:
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

        
class SizeSpecification(Specification):
    def __init__(self, size) -> None:
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


#this is called combinator
class AndSpecification(Specification):
    def __init__(self, *args) -> None:
        self.args = args
    
    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))



class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


"""
Simpler example
"""

class Person:
    def __init__(self, name) -> None:
        self.name = name

class PersonStorage:
    def save_to_database(self, person):
        print(f"Saving {person.name} to database")

    def save_to_json(self, person):
        print(f"Saving {person.name} to json")

# now above class implemenation violates the open closed principle
# so we have to change it.
# what if we need to add another storage method?
# we need to modify the existing class instead of extending it.
class Storage:
    @abstractmethod
    def save(self, person):
        pass

class StorageDatabase(Storage):
    def save(self, person):
        print(f"Saving {person.name} to database")
    
class StorageJSON(Storage):
    def save(self, person):
        print(f"Saving {person.name} to json")

class StorageXML(Storage):
    def save(self, person):
        print(f"Saving {person.name} to xml")




if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    for p in pf.filter_by_color(products, Color.GREEN):
        print(p.name)

    cs = ColorSpecification(Color.GREEN)
    bf = BetterFilter()
    for p in bf.filter(products, cs):
        print(p.name)

    # LARGE AND BLUE
    large_blue = AndSpecification(SizeSpecification(Size.LARGE),
    ColorSpecification(Color.BLUE))
    for p in bf.filter(products, large_blue):
        print(p.name)
