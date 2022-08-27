from abc import abstractmethod
from enum import Enum


class  Realtionship(Enum):
    PARENT = 1
    CHILD = 2
    SIBLING = 3

class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrower:
    @abstractmethod
    def find_all_children_of(self, name): pass
        

class Relationships(RelationshipBrower):
    def __init__(self) -> None:
        self.relations = []

    def add_parent_child(self, parent, child):
        self.relations.append(
            (parent, Realtionship.PARENT, child)
        )
        self.relations.append(
            (child, Realtionship.CHILD, parent)

        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Realtionship.PARENT:
                yield r[2]


class Research:
    # Research is a high-level module that works with the low-level modules
    # and exposes a simple interface to the client.
    # The client should not be forced to depend on the low-level modules directly.
    # Research should work with any implementation of the low-level modules.
    # So instead of depending on the low level module it depennded on the abstractmethod
    # defined in the abstract method.
    # def __init__(self, relationships):
    #     self.relations = relationships.relations
    #     for r in self.relations:
    #         print(f"{r[0].name} is {r[1].name} of {r[2].name}")
    def __init__(self, browser) -> None:
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p.name}")


   


parent = Person("John")
child1 = Person("Mary")
child2 = Person("Mark")
relationships = Relationships()
relationships.add_parent_child(parent, child1)
relationships.add_parent_child(parent, child2)

r = Research(relationships)
