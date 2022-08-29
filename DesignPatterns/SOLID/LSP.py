from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class Parrot(Bird):
    def fly(self):
        print("Parrot can fly")

class Ostrich(Bird):
    def fly(self):
        print("Ostric can't fly")

# OStrict class violates Liskov Substitution Principle

class Bird(ABC):
    pass

class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass

class NonFlyingBird(Bird):
    pass

class Parrot(FlyingBird):
    def fly(self):
        print("Parrot can fly")

    
class Ostrich(NonFlyingBird):
    pass

